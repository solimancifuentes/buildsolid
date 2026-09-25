#!/usr/bin/env python3
"""Read-only local Git worktree facts; never decides whether a worktree is disposable."""

from __future__ import annotations

import argparse
import json
import math
import os
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Sequence


class InventoryError(Exception):
    pass


class GitReader:
    def __init__(self, deadline: float, command_timeout: float) -> None:
        self.deadline = deadline
        self.command_timeout = command_timeout

    def run(self, root: Path, *args: str, allow_failure: bool = False) -> bytes | None:
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise InventoryError("overall deadline expired")
        env = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0", GIT_NO_LAZY_FETCH="1")
        process = None
        try:
            process = subprocess.Popen(
                ["git", "-c", "core.fsmonitor=false", *args], cwd=root, env=env, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, start_new_session=(os.name == "posix"),
            )
            stdout, stderr = process.communicate(timeout=min(remaining, self.command_timeout))
        except subprocess.TimeoutExpired as error:
            self._stop(process)
            raise InventoryError(f"git {args[0]} timed out") from error
        except KeyboardInterrupt:
            self._stop(process)
            raise
        except OSError as error:
            raise InventoryError(f"git unavailable: {error}") from error
        if process.returncode:
            if allow_failure:
                return None
            detail = stderr.decode("utf-8", "replace").strip()
            raise InventoryError(f"git {args[0]} failed: {detail or process.returncode}")
        return stdout

    @staticmethod
    def _stop(process: subprocess.Popen[bytes] | None) -> None:
        if process is None:
            return
        if os.name == "posix":
            # The Git leader may have exited while a child still holds a pipe.
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        elif process.poll() is None:
            process.kill()
        try:
            process.communicate(timeout=1)
        except subprocess.TimeoutExpired:
            for stream in (process.stdout, process.stderr):
                if stream is not None:
                    stream.close()


def decode(value: bytes) -> str:
    return os.fsdecode(value)


def worktree_records(raw: bytes) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for block in raw.split(b"\0\0"):
        if not block:
            continue
        fields = [field for field in block.split(b"\0") if field]
        if not fields or not fields[0].startswith(b"worktree "):
            raise InventoryError("unrecognized NUL-delimited worktree record")
        row: dict[str, Any] = {"path": decode(fields[0][9:])}
        for field in fields[1:]:
            key, _, value = field.partition(b" ")
            name = decode(key)
            row[name] = decode(value) if value else True
        records.append(row)
    return records


def status_entries(raw: bytes) -> dict[str, list[dict[str, str]]]:
    output: dict[str, list[dict[str, str]]] = {
        "tracked_changes": [], "untracked": [], "ignored": []
    }
    fields = raw.split(b"\0")
    index = 0
    while index < len(fields) and fields[index]:
        field = fields[index]
        if len(field) < 4 or field[2:3] != b" ":
            raise InventoryError("unrecognized NUL-delimited status record")
        state = decode(field[:2])
        row = {"path": decode(field[3:]), "status": state}
        if b"R" in field[:2] or b"C" in field[:2]:
            index += 1
            if index >= len(fields) or not fields[index]:
                raise InventoryError("rename/copy status lacks second path")
            row["other_path"] = decode(fields[index])
        if state == "??":
            output["untracked"].append(row)
        elif state == "!!":
            output["ignored"].append(row)
        else:
            output["tracked_changes"].append(row)
        index += 1
    return output


def resolve_base(reader: GitReader, root: Path, explicit: str | None) -> tuple[str | None, str]:
    if explicit:
        resolved = reader.run(root, "rev-parse", "--verify", f"{explicit}^{{commit}}", allow_failure=True)
        if resolved is None:
            raise InventoryError(f"explicit base is not a local commit: {explicit}")
        return resolved.decode().strip(), f"explicit:{explicit}"
    remotes_raw = reader.run(root, "remote") or b""
    candidates: set[str] = set()
    for remote in remotes_raw.decode("utf-8", "replace").splitlines():
        symbolic = reader.run(root, "symbolic-ref", "--quiet", f"refs/remotes/{remote}/HEAD", allow_failure=True)
        if symbolic:
            candidates.add(symbolic.decode().strip())
    if len(candidates) == 1:
        ref = next(iter(candidates))
        resolved = reader.run(root, "rev-parse", "--verify", f"{ref}^{{commit}}", allow_failure=True)
        if resolved:
            return resolved.decode().strip(), f"remote-head:{ref}"
    if len(candidates) > 1:
        return None, "unknown:multiple remote HEADs"
    configured = reader.run(root, "config", "--get", "init.defaultBranch", allow_failure=True)
    if configured:
        branch = configured.decode().strip()
        ref = f"refs/heads/{branch}"
        resolved = reader.run(root, "rev-parse", "--verify", f"{ref}^{{commit}}", allow_failure=True)
        if resolved:
            return resolved.decode().strip(), f"local-config:{ref}"
    return None, "unknown:no local remote HEAD or usable configured default"


def worktree_facts(reader: GitReader, row: dict[str, Any], base: str | None) -> dict[str, Any]:
    path = Path(row["path"])
    facts: dict[str, Any] = {
        "path": row["path"], "head": row.get("HEAD"),
        "branch": row.get("branch"), "detached": bool(row.get("detached")),
        "locked": row.get("locked", False), "prunable": row.get("prunable", False),
        "pr_state": "unknown:not queried",
        "tracked_changes": [], "untracked": [], "ignored": [],
        "commits_not_in_base": None, "upstream": None,
        "commits_not_in_upstream": None,
    }
    if not path.is_dir() or row.get("prunable"):
        facts["availability"] = "unavailable:worktree path missing or prunable"
        return facts
    facts["availability"] = "available"
    parsed = status_entries(reader.run(path, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignored=matching") or b"")
    facts.update(parsed)
    if base and facts["head"]:
        count = reader.run(path, "rev-list", "--count", f"{base}..{facts['head']}", allow_failure=True)
        if count is not None:
            facts["commits_not_in_base"] = int(count.strip())
    if not facts["detached"] and facts["branch"]:
        upstream = reader.run(path, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}", allow_failure=True)
        if upstream:
            facts["upstream"] = upstream.decode().strip()
            count = reader.run(path, "rev-list", "--count", f"{facts['upstream']}..HEAD", allow_failure=True)
            if count is not None:
                facts["commits_not_in_upstream"] = int(count.strip())
    return facts


def inventory(root: Path, base: str | None, timeout: float, command_timeout: float) -> dict[str, Any]:
    reader = GitReader(time.monotonic() + timeout, command_timeout)
    top_raw = reader.run(root, "rev-parse", "--show-toplevel")
    assert top_raw is not None
    if not top_raw.endswith(b"\n"):
        raise InventoryError("git rev-parse returned an unterminated root path")
    top = Path(decode(top_raw[:-1])).resolve()
    selected_base, base_source = resolve_base(reader, top, base)
    raw = reader.run(top, "worktree", "list", "--porcelain", "-z")
    assert raw is not None
    rows = worktree_records(raw)
    return {
        "repository": str(top), "base": selected_base, "base_source": base_source,
        "worktrees": [worktree_facts(reader, row, selected_base) for row in rows],
        "notes": [
            "Counts are relative to the named local ref; they do not prove publication or PR status.",
            "Untracked and ignored paths may contain valuable data; no disposal decision is made.",
        ],
    }


def main(arguments: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="path inside a local Git worktree")
    parser.add_argument("--base", help="explicit local commit/ref for comparison")
    parser.add_argument("--timeout", type=float, default=20.0, help="overall seconds (default 20)")
    parser.add_argument("--command-timeout", type=float, default=5.0, help="per Git command seconds (default 5)")
    args = parser.parse_args(arguments)
    if not all(math.isfinite(value) and value > 0 for value in (args.timeout, args.command_timeout)):
        parser.error("timeouts must be finite and positive")
    try:
        result = inventory(args.root.resolve(), args.base, args.timeout, args.command_timeout)
    except KeyboardInterrupt:
        print("inventory interrupted", file=sys.stderr)
        return 130
    except InventoryError as error:
        print(f"inventory unavailable: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
