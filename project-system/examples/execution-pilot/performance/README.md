# Local performance and forensics fixture

This synthetic Python workload exercises one bounded question: does indexing a Markdown task batch once reduce repeated status/dependency lookup time while returning the same records? It is a method demonstration, not a benchmark of repository validators, BuildSolid users or production latency.

Run from a normal repository checkout with Python 3; no package install, service, network, Git write or customer data is needed:

```sh
python3 project-system/examples/execution-pilot/performance/workload.py
```

The command prints JSON. Save it to a task-owned location if the current task needs durable evidence. Record the command, repository revision or dirty snapshot, fixture SHA-256, Python/platform identity, competing load and verifier in the owning task or QA result. Do not copy raw host details into public examples. The fixture itself does not write output files.

The frozen local case uses 600 deterministic task blocks and 1,200 lookups per batch, seven alternating-order paired rounds, a 20-second measurement deadline, and `perf_counter_ns`. It compares a document rescan per requested ID with a one-pass in-memory index. Two separately labeled baseline calls form the null control. Before timing, both implementations must produce the same exact record sequence; a mismatch stops measurement. No artificial wait occurs in a timed path.

Read `samples_ns` before the summaries: medians, MADs and min/max spreads describe the observed run, not a universal speedup. The `decision` section reports each paired saving and the largest concurrent null difference. It calls the known change discriminated only when the smallest paired saving exceeds that null fluctuation. The null path uses identical code and never establishes a code improvement from a timing difference. A `profile_diagnostic` section lists cumulative hot functions from separate `cProfile` passes; those instrumented numbers are not compared as wall-time samples.

If the deadline is exceeded, correctness fails, or the known change cannot be separated from null fluctuation, report the result as inconclusive or failed as appropriate. Improve a weak harness only with a newly frozen measurement plan before rerunning. Keep a candidate only if it preserves behavior and its evidence supports the stated outcome; otherwise discard/revert it. The applicable [executor method](../../../skills/implementation-executor/references/performance.md) explains how to use this pattern for a real accepted project task without imposing it on every change.
