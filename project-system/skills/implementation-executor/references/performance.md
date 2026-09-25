# Bounded performance and forensics procedure

Use only when an accepted task has a performance question, observed slowdown or unexplained runtime behavior that matters to its done condition. The ordinary feature, bug and refactor procedures remain sufficient when no such issue exists. This optional method introduces no new authority or universal measurement gate.

## Frame and trace the question

Name the affected user or system action, representative input, expected output and critical correctness invariants. Establish the current revision, environment and a reproducible baseline. Inspect a trace, profile or targeted timing to locate the expensive path before choosing a change; separate measured facts from hypotheses. A tool that cannot observe the relevant path leaves the cause uncertain. Do not optimize a guessed bottleneck merely because a microbenchmark is easy to build.

## Freeze a discriminating measurement

Before measuring candidates, record the workload and why it represents the task, baseline and known-change variants, a same-code null control, sample order, bounded run time or iterations, environment, correctness checks, noise summary and decision rule. Use the smallest sample set that can estimate local variation; add samples only under a revised plan when the first run is inconclusive. Do not choose a threshold after seeing results or impose a fixed percentage improvement on every project.

Measure comparable paths with `perf_counter` or a project-native tool, using identical inputs and alternating order when possible. Capture raw samples, median and spread or MAD, paired differences, and the null comparison. Run tracing/profiling separately from the wall-time comparison, because instrumentation changes timing. Use an intentional sensitivity control to show the harness can distinguish a known change; a null change should not be sold as an improvement. Artificial sleeps and one lucky sample are not evidence of performance benefit.

## Decide and preserve behavior

Run the relevant correctness tests or manual behavior checks before and after the candidate. Compare the observed speed signal against local noise and report `improved`, `no detected change`, `regressed` or `inconclusive` with the actual conditions. If the harness cannot discriminate the known control, improve it and freeze a new plan before interpreting the candidate. Keep only a scope-conforming candidate with preserved correctness and evidence supporting the accepted performance condition; otherwise revert or leave it out of the task. Record the tested revision or dirty snapshot, environment, command, trace location and limitation in the owning task/QA provenance. No test result grants deployment or merge authority.

The [synthetic local lookup fixture](../../../examples/execution-pilot/performance/README.md) shows a bounded baseline, known algorithmic change, null comparison and correctness gate. It is an executed pilot only when an actual run and source identity are recorded in the current task; the instructions alone claim no measured improvement in a real product.
