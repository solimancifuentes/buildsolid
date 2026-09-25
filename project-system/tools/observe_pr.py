#!/usr/bin/env python3
"""Optional, read-only, one-PR GitHub observer. Python 3.10+; no installation."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA = re.compile(r"^[0-9a-fA-F]{40}$")
THREAD_QUERY = """query($owner:String!,$name:String!,$number:Int!,$cursor:String){
  repository(owner:$owner,name:$name){pullRequest(number:$number){
    reviewThreads(first:100,after:$cursor){nodes{id isResolved}
      pageInfo{hasNextPage endCursor}}
  }}
}"""


class ObservationError(Exception):
    def __init__(self, message: str, kind: str = "unknown") -> None:
        super().__init__(message)
        self.kind = kind


class Deadline(ObservationError):
    def __init__(self) -> None:
        super().__init__("observation deadline expired", "timeout")


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def object_at(value: Any, keys: tuple[str, ...]) -> Any:
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            raise ObservationError("missing or malformed API field: " + ".".join(keys))
        value = value[key]
    return value


def required_str(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ObservationError("missing or malformed API field: " + label)
    return value


def status_url_matches(value: Any, repo: str, head: str) -> bool:
    """Bind a REST list-status item to its immutable requested endpoint."""
    if not isinstance(value, str):
        return False
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    expected = f"/repos/{repo}/statuses/{head}"
    return (parsed.scheme == "https" and parsed.netloc == "api.github.com"
            and parsed.path.casefold() == expected.casefold()
            and not parsed.query and not parsed.fragment)


def load_requirements(path: str | None) -> dict[str, Any] | None:
    if path is None:
        return None
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ObservationError("requirements unavailable or malformed: " + str(exc)) from exc
    fields = {"required_checks", "required_approvals", "merge_gate_required", "resolved_threads_required", "dependencies", "unsupported_requirements"}
    if not isinstance(data, dict) or set(data) != fields:
        raise ObservationError("requirements must contain exactly required_checks, required_approvals, merge_gate_required, resolved_threads_required, dependencies, unsupported_requirements")
    checks = data["required_checks"]
    if not isinstance(checks, list) or any(not isinstance(x, str) or not x for x in checks) or len(set(checks)) != len(checks):
        raise ObservationError("required_checks must be distinct nonempty strings")
    if type(data["required_approvals"]) is not int or data["required_approvals"] < 0:
        raise ObservationError("required_approvals must be a nonnegative integer")
    for key in ("merge_gate_required", "resolved_threads_required"):
        if not isinstance(data[key], bool):
            raise ObservationError(key + " must be boolean")
    unsupported = data["unsupported_requirements"]
    if not isinstance(unsupported, list) or any(not isinstance(x, str) or not x for x in unsupported):
        raise ObservationError("unsupported_requirements must be a list of nonempty strings")
    deps = data["dependencies"]
    if not isinstance(deps, list):
        raise ObservationError("dependencies must be a list")
    seen: set[tuple[str, int]] = set()
    for dep in deps:
        if not isinstance(dep, dict) or set(dep) != {"repo", "pr", "head"}:
            raise ObservationError("each dependency requires repo, pr, head")
        if not isinstance(dep["repo"], str) or not REPO.fullmatch(dep["repo"]):
            raise ObservationError("invalid dependency repo")
        if type(dep["pr"]) is not int or dep["pr"] < 1 or not isinstance(dep["head"], str) or not SHA.fullmatch(dep["head"]):
            raise ObservationError("invalid dependency number or immutable head")
        key = (dep["repo"], dep["pr"])
        if key in seen:
            raise ObservationError("duplicate dependency")
        seen.add(key)
    return data


class Client:
    def __init__(self, deadline: float, retries: int) -> None:
        self.deadline = deadline
        self.retries = retries
        self.calls = 0

    def remaining(self) -> float:
        remaining = self.deadline - time.monotonic()
        if remaining <= 0:
            raise Deadline()
        return remaining

    def sleep(self, seconds: float) -> None:
        time.sleep(min(seconds, self.remaining()))
        self.remaining()

    def api(self, args: list[str]) -> Any:
        for attempt in range(self.retries + 1):
            self.remaining()
            cmd = ["gh", "api", *args]
            try:
                proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        start_new_session=(os.name == "posix"))
            except OSError as exc:
                raise ObservationError("gh unavailable: " + str(exc)) from exc
            self.calls += 1
            try:
                stdout, stderr = proc.communicate(timeout=self.remaining())
            except (Deadline, subprocess.TimeoutExpired, KeyboardInterrupt):
                self._stop(proc)
                raise
            if proc.returncode == 0:
                try:
                    return json.loads(stdout)
                except (ValueError, UnicodeDecodeError) as exc:
                    raise ObservationError("malformed gh JSON") from exc
            message = stderr.decode("utf-8", "replace").strip()[:300]
            transient = any(word in message.lower() for word in ("rate limit", "secondary rate", "http 429", "http 502", "http 503", "http 504", "timed out"))
            if transient and attempt < self.retries:
                self.sleep(min(2 ** attempt, 5))
                continue
            # Avoid reproducing provider/user text from stderr in a durable receipt.
            label = "rate_limit_or_transient" if transient else "unavailable_or_denied"
            raise ObservationError("gh read failed: " + label)
        raise AssertionError("unreachable")

    @staticmethod
    def _stop(proc: subprocess.Popen[bytes]) -> None:
        try:
            if os.name == "posix":
                # The gh leader may have exited while a child still owns its
                # stdout/stderr pipes. Its process group remains our child group.
                os.killpg(proc.pid, signal.SIGKILL)
            elif proc.poll() is None:
                proc.kill()
        except ProcessLookupError:
            pass
        try:
            proc.communicate(timeout=1)
        except subprocess.TimeoutExpired as exc:
            for pipe in (proc.stdout, proc.stderr):
                if pipe is not None:
                    pipe.close()
            raise ObservationError("owned process cleanup incomplete") from exc


def pages(client: Client, endpoint: str, array_key: str | None = None) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen_ids: set[int] = set()
    for page in range(1, 101):
        separator = "&" if "?" in endpoint else "?"
        body = client.api([f"{endpoint}{separator}per_page=100&page={page}"])
        if array_key:
            total = object_at(body, ("total_count",))
            batch = object_at(body, (array_key,))
            if type(total) is not int or total < 0:
                raise ObservationError("malformed page total")
        else:
            batch = body
            total = None
        if not isinstance(batch, list) or any(not isinstance(x, dict) for x in batch) or len(batch) > 100:
            raise ObservationError("malformed paginated response")
        for item in batch:
            ident = item.get("id")
            if type(ident) is not int or ident < 1 or ident in seen_ids:
                raise ObservationError("missing or duplicate paginated API identity")
            seen_ids.add(ident)
        out.extend(batch)
        if total is not None:
            if len(out) >= total:
                if len(out) != total:
                    raise ObservationError("pagination count changed")
                return out
            if not batch:
                raise ObservationError("incomplete paginated response")
        elif len(batch) < 100:
            return out
    raise ObservationError("pagination limit exceeded")


def threads(client: Client, repo: str, number: int) -> list[dict[str, Any]]:
    owner, name = repo.split("/")
    cursor: str | None = None
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for _ in range(100):
        args = ["graphql", "-f", "query=" + THREAD_QUERY, "-F", "owner=" + owner,
                "-F", "name=" + name, "-F", "number=" + str(number)]
        if cursor is not None:
            args += ["-f", "cursor=" + cursor]
        body = client.api(args)
        if isinstance(body, dict) and body.get("errors"):
            raise ObservationError("GraphQL review-thread read failed")
        pr = object_at(body, ("data", "repository", "pullRequest"))
        if not isinstance(pr, dict):
            raise ObservationError("PR review threads unavailable")
        conn = object_at(pr, ("reviewThreads",))
        nodes = object_at(conn, ("nodes",))
        page = object_at(conn, ("pageInfo",))
        more = object_at(page, ("hasNextPage",))
        end = object_at(page, ("endCursor",))
        if not isinstance(nodes, list) or type(more) is not bool or (end is not None and not isinstance(end, str)):
            raise ObservationError("malformed review-thread page")
        for node in nodes:
            if not isinstance(node, dict) or not isinstance(node.get("id"), str) or type(node.get("isResolved")) is not bool or node["id"] in seen:
                raise ObservationError("malformed or duplicate review thread")
            seen.add(node["id"])
            out.append(node)
        if not more:
            return out
        if not end or end == cursor:
            raise ObservationError("incomplete review-thread pagination")
        cursor = end
    raise ObservationError("review-thread pagination limit exceeded")


def pr_identity(pr: Any, repo: str, number: int) -> dict[str, Any]:
    found_number = object_at(pr, ("number",))
    found_repo = object_at(pr, ("base", "repo", "full_name"))
    if type(found_number) is not int or found_number != number or not isinstance(found_repo, str) or found_repo.casefold() != repo.casefold():
        raise ObservationError("PR response does not match requested repository and number")
    head = object_at(pr, ("head", "sha"))
    base = object_at(pr, ("base", "sha"))
    if not isinstance(head, str) or not SHA.fullmatch(head) or not isinstance(base, str) or not SHA.fullmatch(base):
        raise ObservationError("malformed PR head/base")
    result = {"head": head, "base": base}
    for key in ("state", "draft", "merged", "mergeable", "mergeable_state", "updated_at", "requested_reviewers", "requested_teams"):
        result[key] = object_at(pr, (key,))
    if result["state"] not in ("open", "closed") or type(result["draft"]) is not bool or type(result["merged"]) is not bool or result["mergeable"] not in (True, False, None) or not isinstance(result["mergeable_state"], str) or not isinstance(result["updated_at"], str) or not isinstance(result["requested_reviewers"], list) or not isinstance(result["requested_teams"], list):
        raise ObservationError("malformed PR lifecycle or gate")
    result["requested_reviewers"] = len(result["requested_reviewers"])
    result["requested_teams"] = len(result["requested_teams"])
    return result


def dependency_identity(pr: Any, repo: str, number: int) -> dict[str, Any]:
    info = pr_identity(pr, repo, number)
    return {key: info[key] for key in ("head", "base", "state", "merged", "updated_at")}


def collect(client: Client, repo: str, number: int, requirements: dict[str, Any] | None) -> dict[str, Any]:
    started = now()
    prefix = f"repos/{repo}"
    before = pr_identity(client.api([f"{prefix}/pulls/{number}"]), repo, number)
    checks = pages(client, f"{prefix}/commits/{before['head']}/check-runs", "check_runs")
    statuses = pages(client, f"{prefix}/commits/{before['head']}/statuses")
    reviews = pages(client, f"{prefix}/pulls/{number}/reviews")
    review_threads = threads(client, repo, number)
    deps: list[dict[str, Any]] = []
    if requirements:
        for declared in requirements["dependencies"]:
            if declared["repo"] == repo and declared["pr"] == number:
                raise ObservationError("PR cannot depend on itself")
            found = dependency_identity(client.api([f"repos/{declared['repo']}/pulls/{declared['pr']}"]), declared["repo"], declared["pr"])
            deps.append({"declared": declared, "observed": found})
    # Check completion can change without moving the PR head or updated_at.
    # Reconcile both paginated check surfaces before the final PR read.
    if checks != pages(client, f"{prefix}/commits/{before['head']}/check-runs", "check_runs"):
        raise ObservationError("check runs changed during observation", "stale")
    if statuses != pages(client, f"{prefix}/commits/{before['head']}/statuses"):
        raise ObservationError("status contexts changed during observation", "stale")
    if reviews != pages(client, f"{prefix}/pulls/{number}/reviews"):
        raise ObservationError("reviews changed during observation", "stale")
    if review_threads != threads(client, repo, number):
        raise ObservationError("review threads changed during observation", "stale")
    after = pr_identity(client.api([f"{prefix}/pulls/{number}"]), repo, number)
    if before != after:
        raise ObservationError("PR head/base or material gate changed during observation", "stale")
    for dep in deps:
        declared = dep["declared"]
        after_dep = dependency_identity(client.api([f"repos/{declared['repo']}/pulls/{declared['pr']}"]), declared["repo"], declared["pr"])
        if dep["observed"] != after_dep:
            raise ObservationError("dependency changed during observation", "stale")
    return {"repository": repo, "pr": number, "started_at": started, "ended_at": now(),
            "identity": after, "checks": checks, "statuses": statuses, "reviews": reviews,
            "threads": review_threads, "dependencies": deps, "api_calls": client.calls}


def evaluate(snapshot: dict[str, Any], requirements: dict[str, Any] | None) -> tuple[str, list[dict[str, str]]]:
    if requirements is None:
        return "not_evaluated", []
    items: list[dict[str, str]] = []
    def add(name: str, state: str, reason: str) -> None:
        items.append({"condition": name, "state": state, "reason": reason})
    identity = snapshot["identity"]
    if identity["state"] != "open" or identity["merged"]:
        add("lifecycle", "unmet", "PR is merged or closed")
    elif identity["draft"]:
        add("lifecycle", "unmet", "PR is draft")
    else:
        add("lifecycle", "satisfied", "open and not draft")
    check_runs: dict[str, tuple[int, str, str]] = {}
    check_counts: dict[str, int] = {}
    for check in snapshot["checks"]:
        if check.get("head_sha") != identity["head"]:
            raise ObservationError("check run head does not match observed PR head")
        name = required_str(check.get("name"), "check.name")
        status = required_str(check.get("status"), "check.status")
        conclusion = check.get("conclusion")
        if conclusion is not None and not isinstance(conclusion, str):
            raise ObservationError("malformed check conclusion")
        app_id = object_at(check, ("app", "id"))
        if type(app_id) is not int or app_id < 1:
            raise ObservationError("malformed check app identity")
        check_counts[name] = check_counts.get(name, 0) + 1
        ident = check.get("id")
        if type(ident) is not int or ident < 1:
            raise ObservationError("malformed check id")
        record = (ident, status, conclusion or "")
        if name in check_runs and ident == check_runs[name][0] and record != check_runs[name]:
            raise ObservationError("conflicting check run identity")
        if name not in check_runs or ident > check_runs[name][0]:
            check_runs[name] = record
    status_contexts: dict[str, tuple[str, str]] = {}
    ambiguous_statuses: set[str] = set()
    for status in snapshot["statuses"]:
        if not status_url_matches(status.get("url"), snapshot["repository"], identity["head"]):
            raise ObservationError("status URL does not match requested repository and head")
        name = required_str(status.get("context"), "status.context")
        state = required_str(status.get("state"), "status.state")
        key = required_str(status.get("created_at"), "status.created_at")
        record = (key, state)
        if name in status_contexts and key == status_contexts[name][0] and state != status_contexts[name][1]:
            ambiguous_statuses.add(name)
        if name not in status_contexts or key > status_contexts[name][0]:
            status_contexts[name] = record
    for name in requirements["required_checks"]:
        if name in ambiguous_statuses or check_counts.get(name, 0) > 1 or (name in check_runs and name in status_contexts):
            add("check:" + name, "unknown", "ambiguous check identity or state")
        elif name not in check_runs and name not in status_contexts:
            add("check:" + name, "unmet", "required check absent at observed head")
        else:
            if name in check_runs:
                _, status, conclusion = check_runs[name]
            else:
                _, conclusion = status_contexts[name]
                status = "completed" if conclusion not in ("pending", "expected") else "pending"
            if status == "completed" and conclusion in ("success", "neutral", "skipped"):
                add("check:" + name, "satisfied", conclusion)
            elif status in ("queued", "in_progress", "pending", "requested", "waiting") or conclusion in ("pending", "expected"):
                add("check:" + name, "unmet", "pending")
            elif status == "completed" and conclusion in ("failure", "cancelled", "timed_out", "action_required", "error"):
                add("check:" + name, "unmet", conclusion)
            else:
                add("check:" + name, "unknown", "unsupported check state")
    if requirements["required_approvals"]:
        by_reviewer: dict[str, tuple[str, str, Any]] = {}
        ambiguous_review = False
        pending_review = False
        for review in snapshot["reviews"]:
            login = required_str(object_at(review, ("user", "login")), "review.user.login")
            state = required_str(review.get("state"), "review.state").upper()
            submitted = review.get("submitted_at") or ""
            if not isinstance(submitted, str):
                raise ObservationError("malformed review submitted_at")
            if state not in ("APPROVED", "CHANGES_REQUESTED", "DISMISSED", "COMMENTED", "PENDING"):
                raise ObservationError("unsupported review state")
            if state == "COMMENTED":
                continue
            if state == "PENDING":
                pending_review = True
                continue
            commit_id = review.get("commit_id")
            if login in by_reviewer and submitted == by_reviewer[login][0] and state != by_reviewer[login][1]:
                ambiguous_review = True
            if login not in by_reviewer or submitted > by_reviewer[login][0]:
                by_reviewer[login] = (submitted, state, commit_id)
        states = [v[1] for v in by_reviewer.values()]
        stale_approval = any(v[1] == "APPROVED" and v[2] != identity["head"] for v in by_reviewer.values())
        fresh_approvals = sum(v[1] == "APPROVED" and v[2] == identity["head"] for v in by_reviewer.values())
        if ambiguous_review:
            add("review", "unknown", "conflicting review order")
        elif "CHANGES_REQUESTED" in states:
            add("review", "unmet", "changes requested")
        elif pending_review or identity["requested_reviewers"] or identity["requested_teams"]:
            add("review", "unmet", "awaiting required review")
        elif fresh_approvals < requirements["required_approvals"] and stale_approval:
            add("review", "unknown", "approval head is missing or stale")
        elif fresh_approvals < requirements["required_approvals"]:
            add("review", "unmet", "awaiting required review")
        else:
            add("review", "satisfied", f"{fresh_approvals} current-head approvals observed")
    if requirements["merge_gate_required"]:
        gate = identity["mergeable_state"]
        if identity["mergeable"] is None or gate == "unknown":
            add("merge_gate", "unknown", "mergeability unavailable")
        elif identity["mergeable"] is True and gate == "clean":
            add("merge_gate", "satisfied", "clean technical gate")
        elif gate in ("blocked", "dirty", "draft", "behind", "unstable", "has_hooks") or identity["mergeable"] is False:
            add("merge_gate", "unmet", gate)
        else:
            add("merge_gate", "unknown", "unsupported merge gate")
    if requirements["resolved_threads_required"]:
        count = sum(not x["isResolved"] for x in snapshot["threads"])
        add("threads", "unmet" if count else "satisfied", f"{count} unresolved")
    for dep in snapshot["dependencies"]:
        declared, observed = dep["declared"], dep["observed"]
        name = f"dependency:{declared['repo']}#{declared['pr']}"
        if observed["head"] != declared["head"]:
            add(name, "unknown", "dependency head differs from declared immutable head")
        elif observed["merged"] and observed["state"] == "closed":
            add(name, "satisfied", "declared head merged")
        else:
            add(name, "unmet", "dependency is not merged")
    for name in requirements["unsupported_requirements"]:
        add("unsupported:" + name, "unknown", "accepted condition cannot be evaluated by this helper")
    if any(x["state"] == "unknown" for x in items):
        return "unknown", items
    if any(x["state"] == "unmet" for x in items):
        return "unmet", items
    return "satisfied", items


def sanitized_snapshot(snapshot: dict[str, Any]) -> dict[str, Any]:
    """Expose relevant readback, never provider bodies, URLs or review text."""
    return {"repository": snapshot["repository"], "pr": snapshot["pr"],
            "started_at": snapshot["started_at"], "ended_at": snapshot["ended_at"],
            "identity": snapshot["identity"], "api_calls": snapshot["api_calls"],
            "checks": [{"name": x.get("name"), "status": x.get("status"), "conclusion": x.get("conclusion")}
                       for x in snapshot["checks"]],
            "statuses": [{"context": x.get("context"), "state": x.get("state")}
                         for x in snapshot["statuses"]],
            "reviews": [{"state": x.get("state")} for x in snapshot["reviews"]],
            "threads": [{"isResolved": x.get("isResolved")} for x in snapshot["threads"]],
            "dependencies": snapshot["dependencies"]}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="explicit owner/repository")
    parser.add_argument("--pr", required=True, type=int, help="positive PR number")
    parser.add_argument("--requirements", help="JSON transcription of accepted Markdown requirements")
    parser.add_argument("--watch", action="store_true", help="repeat until satisfied or terminal/deadline")
    parser.add_argument("--timeout", type=float, help="overall seconds; default 30 one-shot, 300 watch")
    parser.add_argument("--interval", type=float, default=15, help="watch seconds; default 15")
    parser.add_argument("--transient-retries", type=int, help="per-read retries; default 0 one-shot, 3 watch")
    args = parser.parse_args(argv)
    if (not REPO.fullmatch(args.repo) or args.pr < 1
            or (args.timeout is not None and (not math.isfinite(args.timeout) or args.timeout <= 0))
            or not math.isfinite(args.interval) or args.interval <= 0
            or (args.transient_retries is not None and args.transient_retries < 0)):
        parser.error("invalid repository, PR, timeout, interval, or retries")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    started = now()
    try:
        requirements = load_requirements(args.requirements)
        client = Client(time.monotonic() + (args.timeout or (300 if args.watch else 30)),
                        args.transient_retries if args.transient_retries is not None else (3 if args.watch else 0))
        while True:
            snapshot = collect(client, args.repo, args.pr, requirements)
            verdict, conditions = evaluate(snapshot, requirements)
            result = {"kind": "pr_observation", "status": verdict, "snapshot": sanitized_snapshot(snapshot),
                      "requirements_evaluated": requirements is not None, "conditions": conditions,
                      "merge_permission": "not_evaluated"}
            if (not args.watch or verdict == "satisfied" or requirements is None
                    or requirements["unsupported_requirements"] or snapshot["identity"]["state"] != "open"):
                print(json.dumps(result, sort_keys=True))
                return 0 if verdict == "satisfied" else 1 if verdict == "unmet" else 2
            client.sleep(args.interval)
    except KeyboardInterrupt:
        print(json.dumps({"kind": "pr_observation", "status": "cancelled", "started_at": started,
                          "merge_permission": "not_evaluated"}))
        return 2
    except (Deadline, subprocess.TimeoutExpired):
        print(json.dumps({"kind": "pr_observation", "status": "timeout", "started_at": started,
                          "merge_permission": "not_evaluated"}))
        return 124
    except ObservationError as exc:
        print(json.dumps({"kind": "pr_observation", "status": exc.kind, "reason": str(exc),
                          "started_at": started, "merge_permission": "not_evaluated"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
