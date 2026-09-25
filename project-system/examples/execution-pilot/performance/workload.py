#!/usr/bin/env python3
"""Bounded synthetic Markdown-task lookup measurement; no production writes."""

from __future__ import annotations

import cProfile
import hashlib
import json
import platform
import pstats
import re
import statistics
import sys
import time
from pathlib import Path
from typing import Callable


TASK_COUNT = 600
ROUNDS = 7
MAX_SECONDS = 20
STATUSES = ("Not started", "In progress", "Blocked", "Done")
TASK_RE = re.compile(
    r"(?ms)^### (?P<id>T\d{4}) — [^\n]+\n(?P<body>.*?)(?=^### T\d{4} — |\Z)"
)
STATUS_RE = re.compile(r"(?m)^\*\*Status:\*\* ([^\n]+)$")
DEPENDENCIES_RE = re.compile(r"(?m)^\*\*Dependencies:\*\* ([^\n]+)$")
Record = tuple[str, str, tuple[str, ...]]
Batch = tuple[Record, ...]


def task_id(number: int) -> str:
    return f"T{number:04d}"


def build_document(count: int = TASK_COUNT) -> str:
    if count < 1 or count > 9999:
        raise ValueError("task count must fit the four-digit fixture ID")
    blocks = []
    for number in range(1, count + 1):
        dependencies = (
            "None" if number <= 2
            else f"{task_id(number - 2)}, {task_id(number - 1)}"
        )
        blocks.append(
            f"### {task_id(number)} — Local task {number}\n"
            f"**Status:** {STATUSES[(number - 1) % len(STATUSES)]}\n"
            f"**Dependencies:** {dependencies}\n"
        )
    return "\n".join(blocks)


def parse_record(match: re.Match[str]) -> Record:
    body = match.group("body")
    status_match = STATUS_RE.search(body)
    dependencies_match = DEPENDENCIES_RE.search(body)
    if status_match is None or dependencies_match is None:
        raise ValueError(f"incomplete task block {match.group('id')}")
    raw = dependencies_match.group(1)
    dependencies = () if raw == "None" else tuple(item.strip() for item in raw.split(","))
    return match.group("id"), status_match.group(1), dependencies


def baseline_batch(document: str, queries: tuple[str, ...]) -> Batch:
    """Find each requested task by scanning the document again."""
    records = []
    for query in queries:
        for match in TASK_RE.finditer(document):
            if match.group("id") == query:
                records.append(parse_record(match))
                break
        else:
            raise KeyError(query)
    return tuple(records)


def indexed_batch(document: str, queries: tuple[str, ...]) -> Batch:
    """Build one in-memory index for the same batch of requests."""
    index: dict[str, Record] = {}
    for match in TASK_RE.finditer(document):
        record = parse_record(match)
        if record[0] in index:
            raise ValueError(f"duplicate task ID {record[0]}")
        index[record[0]] = record
    return tuple(index[query] for query in queries)


def queries_for(count: int) -> tuple[str, ...]:
    ids = tuple(task_id(number) for number in range(1, count + 1))
    return tuple(reversed(ids)) + ids


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def summarize(samples: list[int]) -> dict[str, int | float]:
    center = statistics.median(samples)
    return {
        "median_ns": center,
        "mad_ns": statistics.median(abs(sample - center) for sample in samples),
        "min_ns": min(samples),
        "max_ns": max(samples),
    }


def classify(baseline: list[int], indexed: list[int], null_a: list[int], null_b: list[int]) -> dict[str, object]:
    if not (len(baseline) == len(indexed) == len(null_a) == len(null_b)) or not baseline:
        raise ValueError("paired timing arrays must have the same nonzero length")
    paired_savings = [left - right for left, right in zip(baseline, indexed)]
    null_differences = [left - right for left, right in zip(null_a, null_b)]
    null_fluctuation = max(abs(value) for value in null_differences)
    return {
        "paired_savings_ns": paired_savings,
        "null_differences_ns": null_differences,
        "null_fluctuation_bound_ns": null_fluctuation,
        "known_change_discriminated": min(paired_savings) > null_fluctuation,
        "null_code_change": False,
    }


def profile_once(function: Callable[[str, tuple[str, ...]], Batch], document: str, queries: tuple[str, ...]) -> list[dict[str, int | float | str]]:
    profiler = cProfile.Profile()
    profiler.runcall(function, document, queries)
    stats = pstats.Stats(profiler)
    ordered = sorted(stats.stats.items(), key=lambda item: item[1][3], reverse=True)
    return [
        {
            "function": key[2],
            "calls": value[1],
            "cumulative_seconds": round(value[3], 6),
        }
        for key, value in ordered[:6]
    ]


def measure() -> dict[str, object]:
    document = build_document()
    queries = queries_for(TASK_COUNT)
    expected = baseline_batch(document, queries)
    improved = indexed_batch(document, queries)
    if expected != improved or len(expected) != len(queries):
        raise AssertionError("correctness mismatch; no timing claim is permitted")
    output_bytes = json.dumps(expected, separators=(",", ":")).encode("utf-8")

    cases: dict[str, Callable[[str, tuple[str, ...]], Batch]] = {
        "baseline": baseline_batch,
        "indexed": indexed_batch,
        "null_a": baseline_batch,
        "null_b": baseline_batch,
    }
    for name in ("baseline", "indexed"):
        cases[name](document, queries)

    started = time.monotonic()
    samples: dict[str, list[int]] = {name: [] for name in cases}
    orders: list[list[str]] = []
    for round_number in range(ROUNDS):
        order = list(cases) if round_number % 2 == 0 else list(reversed(cases))
        orders.append(order)
        for name in order:
            if time.monotonic() - started > MAX_SECONDS:
                return {"outcome": "inconclusive", "reason": "measurement deadline exceeded", "samples_ns": samples, "orders": orders}
            before = time.perf_counter_ns()
            observed = cases[name](document, queries)
            elapsed = time.perf_counter_ns() - before
            if observed != expected:
                raise AssertionError(f"correctness changed during timing: {name}")
            samples[name].append(elapsed)
    if time.monotonic() - started > MAX_SECONDS:
        return {"outcome": "inconclusive", "reason": "measurement deadline exceeded", "samples_ns": samples, "orders": orders}

    classification = classify(samples["baseline"], samples["indexed"], samples["null_a"], samples["null_b"])
    return {
        "outcome": "measured",
        "question": "Does a one-pass index improve repeated Markdown task lookups without changing records?",
        "fixture": {"tasks": TASK_COUNT, "queries_per_batch": len(queries), "rounds": ROUNDS, "max_seconds": MAX_SECONDS},
        "identity": {
            "fixture_sha256": sha256(Path(__file__).read_bytes()),
            "input_sha256": sha256(document.encode("utf-8")),
            "output_sha256": sha256(output_bytes),
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "processor": platform.processor() or "unavailable",
        },
        "orders": orders,
        "samples_ns": samples,
        "summaries_ns": {name: summarize(values) for name, values in samples.items()},
        "decision": classification,
        "profile_diagnostic": {
            "baseline": profile_once(baseline_batch, document, queries),
            "indexed": profile_once(indexed_batch, document, queries),
        },
    }


if __name__ == "__main__":
    result = measure()
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["outcome"] == "measured" else 2)
