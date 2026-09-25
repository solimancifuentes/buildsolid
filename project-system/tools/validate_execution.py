#!/usr/bin/env python3
"""Optional, read-only Markdown task structure and receipt identity checker.

This checks a documented subset, not acceptance, authority, test execution or the
semantic adequacy of prose. Ordinary Markdown/manual review remains sufficient.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time
from dataclasses import dataclass, field

ID = r"[A-Za-z][A-Za-z0-9_-]*[0-9][A-Za-z0-9_-]*"
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+)?\s*$")
TASK_TITLE = re.compile(rf"^({ID})(?:(?:\s+[—–-]\s+|:\s+|\s+)(.+))?$")
FIELD = re.compile(r"^\s*(?:[-*]\s+)?(?:\*\*([^*]+):\*\*|\*\*([^*]+)\*\*:|([A-Za-z][A-Za-z /_-]*):)\s*(.*)$")
STATUSES = {"not started", "in progress", "blocked", "done"}
ALIASES = {"task id": "id", "acceptance criteria": "acceptance", "done condition": "acceptance", "depends on": "dependencies", "verification receipt": "receipt", "command": "procedure", "tested revision": "revision", "relevant base": "base", "allowed effects": "effects"}
MINIMUM = {"status", "acceptance", "dependencies"}
FULL = MINIMUM | {"description", "files", "inputs", "parallelizable", "review"}
RECEIPT = {"repository", "revision", "base", "environment", "procedure", "expected", "outcome", "evidence", "verifier", "snapshot"}


@dataclass
class Task:
    id: str
    title: str
    line: int
    level: int
    fields: dict[str, str] = field(default_factory=dict)


def issue(kind: str, message: str, task: str | None = None, line: int | None = None) -> dict:
    return {key: value for key, value in {"kind": kind, "task": task, "line": line, "message": message}.items() if value is not None}


def content_lines(text: str):
    """Ignore fenced examples and HTML comments, retaining source line numbers."""
    fence = None
    comment = False
    for number, raw in enumerate(text.splitlines(), 1):
        if fence:
            if re.match(r"^ {0,3}" + re.escape(fence[0]) + "{" + str(fence[1]) + r",}\s*$", raw):
                fence = None
            continue
        line = ""
        remaining = raw
        while remaining:
            if comment:
                end = remaining.find("-->")
                if end < 0:
                    remaining = ""
                else:
                    comment = False
                    remaining = remaining[end + 3:]
            else:
                start = remaining.find("<!--")
                if start < 0:
                    line += remaining
                    remaining = ""
                else:
                    line += remaining[:start]
                    remaining = remaining[start + 4:]
                    comment = True
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if opening:
            token = opening.group(1)
            fence = (token[0], len(token))
            continue
        if not line.lstrip().startswith(">"):
            yield number, line
    if fence or comment:
        raise ValueError("unclosed fenced example or HTML comment makes parsing ambiguous")


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().strip("` ").rstrip(".")).casefold()


def parse(text: str) -> tuple[list[Task], list[dict]]:
    tasks: list[Task] = []
    issues: list[dict] = []
    current = None
    current_field = None
    orphan = None
    for number, line in content_lines(text):
        heading = HEADING.match(line)
        if heading:
            level, title = len(heading.group(1)), heading.group(2)
            candidate = TASK_TITLE.match(title)
            if candidate:
                current = Task(candidate.group(1), candidate.group(2) or candidate.group(1), number, level)
                tasks.append(current)
                current_field = None
                orphan = None
            elif current and level > current.level:
                current_field = None  # receipt subsections may hold the same task's fields
            else:
                current = None
                current_field = None
                orphan = (number, title)
            continue
        match = FIELD.match(line)
        if match:
            name = normalize(next(part for part in match.groups()[:3] if part is not None))
            name = ALIASES.get(name, name)
            value = match.group(4).strip()
            if current is None:
                if name in {"status", "acceptance", "dependencies"}:
                    issues.append(issue("invalid", "task fields have no recognized task ID heading", line=orphan[0] if orphan else number))
                continue
            if name in current.fields:
                issues.append(issue("invalid", f"ambiguous repeated field: {name}", current.id, number))
            else:
                current.fields[name] = value
            current_field = name
        elif current and current_field and line.strip():
            current.fields[current_field] += "\n" + line.strip()
    return tasks, issues


def dependencies(value: str) -> list[str]:
    raw = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value).replace("`", "").strip()
    if normalize(raw) in {"none", "no dependencies", "no prerequisite tasks", "independent"}:
        return []
    found = re.findall(rf"(?<![A-Za-z0-9_-]){ID}(?![A-Za-z0-9_-])", raw)
    remainder = re.sub(rf"(?<![A-Za-z0-9_-]){ID}(?![A-Za-z0-9_-])", "", raw)
    remainder = re.sub(r"\b(?:and|after)\b", "", remainder, flags=re.I)
    if not found or remainder.strip(" ,;.&\n\t-"):
        raise ValueError("dependency prose is outside the checker subset; use IDs or manual review")
    return found


def check_structure(tasks: list[Task], full: bool) -> tuple[list[dict], dict[str, list[str]]]:
    issues = []
    graph = {}
    if not tasks:
        issues.append(issue("invalid", "no task IDs found; expected a heading such as '### A1 — Outcome'"))
    for task in tasks:
        if task.id in graph:
            issues.append(issue("invalid", "duplicate task ID", task.id, task.line))
        for name in sorted((FULL if full else MINIMUM) - task.fields.keys()):
            issues.append(issue("invalid", f"missing required field: {name}", task.id, task.line))
        for name, value in task.fields.items():
            if not value.strip() and name in (FULL if full else MINIMUM):
                issues.append(issue("invalid", f"empty required field: {name}", task.id, task.line))
        if "status" in task.fields and normalize(task.fields["status"]) not in STATUSES:
            issues.append(issue("invalid", "unsupported or ambiguous task status", task.id, task.line))
        try:
            graph[task.id] = dependencies(task.fields.get("dependencies", "None"))
        except ValueError as error:
            issues.append(issue("unknown", str(error), task.id, task.line))
            graph[task.id] = []
    for task_id, deps in graph.items():
        for dep in deps:
            if dep not in graph:
                issues.append(issue("invalid", f"unknown dependency: {dep}", task_id))
    # Iterative topological removal supports large task lists without recursion.
    indegree = {key: 0 for key in graph}
    children = {key: [] for key in graph}
    for task_id, deps in graph.items():
        for dep in set(deps):
            if dep in graph:
                indegree[task_id] += 1
                children[dep].append(task_id)
    ready = [key for key, count in indegree.items() if count == 0]
    while ready:
        node = ready.pop()
        for child in children[node]:
            indegree[child] -= 1
            if not indegree[child]:
                ready.append(child)
    cyclic = sorted(key for key, count in indegree.items() if count)
    if cyclic:
        issues.append(issue("invalid", "dependency cycle or dependent on a cycle: " + ", ".join(cyclic)))
    states = {task.id: normalize(task.fields.get("status", "")) for task in tasks}
    for task_id, deps in graph.items():
        if states[task_id] == "done":
            for dep in deps:
                if dep in states and states[dep] != "done":
                    issues.append(issue("unknown", f"Done claim depends on unfinished {dep}; status alone is not verification", task_id))
    return issues, graph


class ReadFailure(Exception):
    pass


def git(repo: Path, arguments: list[str], deadline: float) -> str:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise ReadFailure("overall Git-read deadline exceeded")
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0", GIT_NO_LAZY_FETCH="1")
    process = None
    try:
        process = subprocess.Popen(["git", "-c", "core.fsmonitor=false", "-C", str(repo), *arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, start_new_session=(os.name == "posix"))
        stdout, stderr = process.communicate(timeout=min(5, remaining))
    except (subprocess.TimeoutExpired, KeyboardInterrupt) as error:
        if process is not None:
            if os.name == "posix":
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            else:
                process.kill()
            process.wait(timeout=1)
            if process.stdout:
                process.stdout.close()
            if process.stderr:
                process.stderr.close()
        if isinstance(error, KeyboardInterrupt):
            raise
        raise ReadFailure("Git read deadline exceeded") from error
    except OSError as error:
        raise ReadFailure(f"Git read unavailable: {type(error).__name__}") from error
    if process.returncode:
        raise ReadFailure("Git read failed: " + stderr.decode("utf-8", "replace").strip())
    return stdout.decode("utf-8", "strict").rstrip("\n")


def artifacts(value: str, root: Path, task_id: str, label: str, deadline: float) -> list[dict]:
    issues = []
    rows = [line.strip().removeprefix("- ") for line in value.splitlines() if line.strip()]
    for row in rows:
        if time.monotonic() >= deadline:
            raise ReadFailure("overall identity-read deadline exceeded")
        match = re.fullmatch(r"(.+?)\s+(?:sha256:|sha256=)([a-fA-F0-9]{64})", row)
        if not match:
            issues.append(issue("invalid", f"{label} needs a local path and SHA-256 per line", task_id))
            continue
        raw = match.group(1).strip("` ")
        link = re.fullmatch(r"\[[^]]+\]\((?:<([^>]+)>|([^)]*))\)", raw)
        if link:
            raw = link.group(1) or link.group(2)
        path = (root / raw).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError:
            issues.append(issue("unknown", f"{label} leaves the explicit root; not read: {raw}", task_id))
            continue
        try:
            # Avoid a directory, device, external symlink or an unbounded artifact.
            if not path.is_file() or path.stat().st_size > 32 * 1024 * 1024:
                raise OSError("missing, non-file or over 32 MiB")
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                while chunk := stream.read(1024 * 1024):
                    if time.monotonic() >= deadline:
                        raise ReadFailure("overall identity-read deadline exceeded")
                    digest.update(chunk)
            actual = digest.hexdigest()
        except OSError:
            issues.append(issue("unknown", f"{label} unavailable: {raw}", task_id))
            continue
        if actual != match.group(2).lower():
            issues.append(issue("stale", f"{label} digest changed: {raw}", task_id))
    return issues


def check_receipts(tasks: list[Task], material: set[str], root: Path, repo: Path | None, base: str | None, deadline: float) -> list[dict]:
    issues = []
    for unknown in material - {task.id for task in tasks}:
        issues.append(issue("invalid", "unknown --material-task ID", unknown))
    for task in tasks:
        fields = task.fields
        if task.id not in material and "receipt" not in fields:
            continue
        missing = sorted(name for name in RECEIPT if not fields.get(name, "").strip())
        if missing:
            issues.append(issue("invalid", "material receipt missing: " + ", ".join(missing), task.id))
            continue
        outcome = normalize(fields["outcome"])
        if outcome not in {"passed", "failed", "unverified", "inconclusive"}:
            issues.append(issue("invalid", "unsupported receipt outcome", task.id))
        elif outcome != "passed":
            issues.append(issue("unknown", "material observation is " + outcome, task.id))
        snapshot = normalize(fields["snapshot"])
        if snapshot not in {"clean", "dirty"}:
            issues.append(issue("invalid", "snapshot must state clean or dirty", task.id))
        if snapshot == "dirty" and not fields.get("source files"):
            issues.append(issue("invalid", "dirty receipt needs source files with observed digests", task.id))
        issues += artifacts(fields["evidence"], root, task.id, "evidence", deadline)
        if fields.get("source files"):
            issues += artifacts(fields["source files"], root, task.id, "source input", deadline)
        revision = fields["revision"].strip("` ")
        if not re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", revision):
            issues.append(issue("invalid", "receipt revision must be a full immutable commit ID", task.id))
            continue
        if repo is None:
            issues.append(issue("unknown", "receipt Git identity not checked; supply --repo or review manually", task.id))
            continue
        try:
            actual = git(repo, ["rev-parse", "--verify", "--end-of-options", revision + "^{commit}"], deadline)
            head = git(repo, ["rev-parse", "--verify", "HEAD"], deadline)
            declared_repo = fields["repository"].strip("` ")
            if Path(declared_repo).expanduser().resolve() != repo.resolve():
                remote = git(repo, ["config", "--get", "remote.origin.url"], deadline)
                if declared_repo != remote:
                    issues.append(issue("unknown", "receipt repository identity differs from supplied repository", task.id))
            if actual.lower() != revision.lower() or head.lower() != revision.lower():
                issues.append(issue("stale", "tested revision differs from current HEAD; scoped reuse needs manual evidence", task.id))
            status = git(repo, ["status", "--porcelain=v1", "-z", "--untracked-files=all"], deadline)
            if status and snapshot == "clean":
                issues.append(issue("stale", "clean receipt cannot establish current dirty snapshot identity", task.id))
            elif not status and snapshot == "dirty":
                issues.append(issue("stale", "dirty receipt cannot establish current clean snapshot identity", task.id))
            stated_base = fields["base"].strip("` ")
            if normalize(stated_base) not in {"none", "not applicable"}:
                if not re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", stated_base):
                    issues.append(issue("invalid", "receipt base must be immutable or explicitly not applicable", task.id))
                else:
                    git(repo, ["cat-file", "-e", stated_base + "^{commit}"], deadline)
                    if base is None:
                        issues.append(issue("unknown", "relevant base freshness not checked; supply --base", task.id))
                    elif git(repo, ["rev-parse", "--verify", "--end-of-options", base + "^{commit}"], deadline).lower() != stated_base.lower():
                        issues.append(issue("stale", "relevant base changed", task.id))
            elif base is not None:
                issues.append(issue("unknown", "current base supplied but receipt declares none", task.id))
        except (ReadFailure, UnicodeError) as error:
            issues.append(issue("unknown", str(error), task.id))
    return issues


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=Path, help="existing Markdown with task headings and fields")
    parser.add_argument("--full", action="store_true", help="check all full-template task fields, not just the compact subset")
    parser.add_argument("--root", type=Path, help="allowed root for receipt artifacts; default: contract directory")
    parser.add_argument("--repo", type=Path, help="explicit local Git checkout for material receipt identity reads")
    parser.add_argument("--base", help="current relevant local base ref to compare to immutable receipt base; never fetches")
    parser.add_argument("--material-task", action="append", default=[], help="require receipt identity for this task; repeat as needed")
    parser.add_argument("--timeout", type=float, default=30, help="total Git-read budget in seconds (default 30)")
    args = parser.parse_args(argv)
    if not 0 < args.timeout <= 300:
        parser.error("--timeout must be greater than 0 and at most 300")
    deadline = time.monotonic() + args.timeout
    try:
        if args.contract.stat().st_size > 4 * 1024 * 1024:
            raise ValueError("contract exceeds the 4 MiB checker limit")
        tasks, issues = parse(args.contract.read_text(encoding="utf-8"))
        structure, graph = check_structure(tasks, args.full)
        issues += structure
        issues += check_receipts(tasks, set(args.material_task), args.root or args.contract.resolve().parent, args.repo, args.base, deadline)
        code = 1 if any(item["kind"] == "invalid" for item in issues) else 2 if issues else 0
        result = {"structure": "invalid" if any(item["kind"] == "invalid" for item in issues) else "valid", "evidence_identity": "incomplete_or_stale" if issues else ("matching_supplied_records_only" if args.material_task or any("receipt" in task.fields for task in tasks) else "not_requested"), "semantic_acceptance": "not_evaluated", "test_execution": "not_asserted", "tasks": [task.id for task in tasks], "dependencies": graph, "issues": issues}
    except (OSError, UnicodeError, ValueError, ReadFailure) as error:
        code = 2
        result = {"structure": "unknown", "semantic_acceptance": "not_evaluated", "issues": [issue("unknown", str(error))]}
    except KeyboardInterrupt:
        code = 2
        result = {"structure": "unknown", "semantic_acceptance": "not_evaluated", "issues": [issue("unknown", "cancelled; no acceptance claim")]}
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
