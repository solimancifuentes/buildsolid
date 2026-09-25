#!/usr/bin/env python3
"""Check the small, staged Git fixture described by the execution pilot."""

from __future__ import annotations

import argparse
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import signal
import subprocess
import sys
import threading
import time
from typing import BinaryIO


GIT_BUDGET_SECONDS = 8.0
GIT_CALL_SECONDS = 2.0
GIT_STDOUT_LIMIT = 64 * 1024
GIT_STDERR_LIMIT = 8 * 1024
README = "README.md"
SKILL = "skills/example/SKILL.md"
LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")


class FixtureError(Exception):
    """A root, Git read, or fixture format cannot be evaluated."""


def git(root: Path, arguments: list[str], deadline: float) -> bytes:
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise FixtureError("Git read deadline exceeded")
    command = ["git", "-C", str(root), *arguments]
    try:
        process = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(
                os.environ,
                GIT_OPTIONAL_LOCKS="0",
                GIT_TERMINAL_PROMPT="0",
                GIT_NO_LAZY_FETCH="1",
            ),
            start_new_session=(os.name == "posix"),
        )
    except OSError as error:
        raise FixtureError(f"Git unavailable: {error.strerror or type(error).__name__}") from error
    output = bytearray()
    errors = bytearray()
    overflow = threading.Event()
    read_errors: list[OSError] = []

    def read_pipe(pipe: BinaryIO, buffer: bytearray, limit: int) -> None:
        try:
            while True:
                chunk = os.read(pipe.fileno(), 8192)
                if not chunk:
                    return
                available = limit + 1 - len(buffer)
                buffer.extend(chunk[:available])
                if len(buffer) > limit:
                    overflow.set()
                    return
        except OSError as error:
            read_errors.append(error)

    assert process.stdout is not None and process.stderr is not None
    readers = [
        threading.Thread(target=read_pipe, args=(process.stdout, output, GIT_STDOUT_LIMIT), daemon=True),
        threading.Thread(target=read_pipe, args=(process.stderr, errors, GIT_STDERR_LIMIT), daemon=True),
    ]
    for reader in readers:
        reader.start()
    end = time.monotonic() + min(GIT_CALL_SECONDS, remaining)
    try:
        while process.poll() is None or any(reader.is_alive() for reader in readers):
            if overflow.is_set():
                raise FixtureError("Git output limit exceeded")
            if time.monotonic() >= end:
                raise FixtureError("Git read deadline exceeded")
            overflow.wait(timeout=min(0.02, max(0, end - time.monotonic())))
        if overflow.is_set():
            raise FixtureError("Git output limit exceeded")
        if read_errors:
            raise FixtureError("Git pipe read failed")
    except FixtureError:
        if process.poll() is not None:
            for reader in readers:
                reader.join(timeout=0.2)
        if os.name == "posix":
            if process.poll() is None or any(reader.is_alive() for reader in readers):
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                except PermissionError as error:
                    if process.poll() is None:
                        process.kill()
                    for reader in readers:
                        reader.join(timeout=0.2)
                    if any(reader.is_alive() for reader in readers):
                        raise FixtureError("owned Git process group could not be stopped") from error
        else:
            if process.poll() is None:
                process.kill()
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            pass
        for reader in readers:
            reader.join(timeout=0.2)
        raise
    finally:
        process.stdout.close()
        process.stderr.close()
    if process.returncode:
        detail = errors.decode("utf-8", "replace").strip().splitlines()
        raise FixtureError(f"Git read failed ({arguments[0]}): {detail[0] if detail else 'unknown error'}")
    return output


def indexed_text(root: Path, name: str, deadline: float) -> str:
    try:
        return git(root, ["show", f":{name}"], deadline).decode("utf-8", "strict")
    except UnicodeError as error:
        raise FixtureError(f"indexed {name} is not UTF-8") from error


def local_target(raw: str) -> str | None:
    # The fixture uses bare local paths. Other URL forms are outside this example.
    if raw.startswith(("#", "http://", "https://", "mailto:")):
        return None
    if raw.startswith("/") or "?" in raw or "#" in raw or "\\" in raw:
        raise FixtureError(f"unsupported fixture link: {raw}")
    target = posixpath.normpath(raw)
    if target in (".", "..") or target.startswith("../"):
        raise FixtureError(f"link leaves fixture root: {raw}")
    return target


def has_description(skill: str) -> bool:
    lines = skill.splitlines()
    if not lines or lines[0] != "---":
        return False
    try:
        end = lines.index("---", 1)
    except ValueError:
        return False
    for line in lines[1:end]:
        if line.startswith("description:") and line.partition(":")[2].strip().strip('"\''):
            return True
    return False


def inspect(root: Path) -> list[str]:
    if not root.is_dir():
        raise FixtureError("root is not an existing directory")
    root = root.resolve()
    deadline = time.monotonic() + GIT_BUDGET_SECONDS
    try:
        top = git(root, ["rev-parse", "--show-toplevel"], deadline).decode("utf-8", "strict").strip()
    except UnicodeError as error:
        raise FixtureError("Git root is not UTF-8") from error
    if Path(top).resolve() != root:
        raise FixtureError("root must be the repository top level, not a nested directory")
    indexed = {
        path.decode("utf-8", "strict")
        for path in git(root, ["ls-files", "--cached", "-z"], deadline).split(b"\0")
        if path
    }
    if README not in indexed or SKILL not in indexed:
        raise FixtureError("fixture README.md and skills/example/SKILL.md must be in the Git index")
    readme = indexed_text(root, README, deadline)
    skill = indexed_text(root, SKILL, deadline)
    issues: list[str] = []
    for raw in LINK.findall(readme):
        target = local_target(raw)
        if target is None:
            continue
        if target in indexed:
            continue
        path = root.joinpath(*PurePosixPath(target).parts)
        if not path.resolve().is_relative_to(root):
            raise FixtureError(f"link target leaves fixture root: {target}")
        if path.is_file():
            issues.append(f"untracked link target: {target}")
        else:
            issues.append(f"missing link target: {target}")
    if not has_description(skill):
        issues.append(f"missing skill description: {SKILL}")
    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="top level of the tiny Git fixture")
    args = parser.parse_args(argv)
    if sys.version_info < (3, 10):
        print("fixture-error: Python 3.10 or newer is required", file=sys.stderr)
        return 2
    try:
        issues = inspect(args.root)
    except (FixtureError, OSError, UnicodeError) as error:
        print(f"fixture-error: {error}", file=sys.stderr)
        return 2
    if issues:
        for issue in issues:
            print(issue)
        return 1
    print("fixture-validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
