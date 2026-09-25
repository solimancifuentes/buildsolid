# Stage 9 task-type procedures

Use the shared entry, scope, evidence and handoff rules in [the executor skill](../SKILL.md). Select only the procedure matching the accepted task. A project-specific verifier can supply runnable instructions, but the task's accepted behavior remains the standard for interpreting output.

## Feature

1. Identify the user-visible outcome, affected entry points and indirect consumers. List critical invariants and failure or edge states that the feature must preserve.
2. Implement the smallest accepted behavior. Exercise at least one realistic success path and the material boundary or regression cases with the project's actual harness or a reproducible manual procedure.
3. Compare observed behavior with acceptance, including excluded effects. Record what ran, what failed and what remains unverified; do not infer a pass from compilation, a mock alone, or a description of expected behavior.

## Bug

1. State expected behavior and reproduce the reported symptom against the relevant baseline. Confirm that the baseline check fails for the intended defect, not a missing dependency, malformed fixture or unrelated assertion. Preserve the baseline command, inputs and observed failure.
2. Make the smallest scope-conforming fix and rerun the same check. Then exercise a nearby regression or indirect consumer when the failure path could affect it.
3. If the baseline cannot be reproduced safely or deterministically, record the attempted procedure, actual observation and reason. Use another observable comparison when available, but label the missing failure-before proof; never invent it. A passing post-fix check alone does not prove the reported bug was present or fixed.

## Refactor

1. Name the behavior and interfaces that must remain stable, including callers, data shape, errors and side effects relevant to the accepted task. Identify the reason for the internal change and the files that own it.
2. Capture an adequate pre-change public-behavior baseline. Make the internal change without broadening feature scope; rerun the same checks against representative success and failure paths and affected consumers.
3. Report any deliberate observable change as contract drift. If the owning contract accepts that deliberate change, classify and verify it as changed behavior; it is no longer a semantics-preserving refactor.

## Disposable experiment

1. Read the accepted brief: question, scope/non-goals, observable result, allowed effects, bounded time/cost/resource budget and disposal or promotion rule. Isolate task-owned state and choose a measurement that can answer the question.
2. Run only within those bounds; preserve observations, uncertainty, environment and resource use. Stop at the budget or boundary even if the result is inconclusive.
3. Dispose of only state the task owns, if the brief calls for disposal and the action is authorized. Propose any production use through an adequate accepted production contract before moving experiment code or behavior into production.

## Illustrative examples

These are hypothetical records to clarify the distinct obligations. They are not executed BuildSolid evidence.

- **Feature:** A task accepts an empty search state. The executor adds that state, drives a query with zero results, checks the visible message and verifies the normal results path still works. The record names the tested revision, command or manual steps, observed states and an untested screen-reader announcement if accessibility tooling was unavailable.
- **Bug:** A saved-filter task reports that refresh drops the selected filter. A baseline browser check first demonstrates the filter disappears after refresh for the intended reason; the fix keeps it, and the same check plus a fresh-session check pass. An unrelated test failure would be recorded separately and would not satisfy the baseline proof.
- **Refactor:** A cache extraction is accepted with unchanged API behavior. Pre-change and post-change checks use the same representative success, missing-key and error cases. A changed error status is a failed invariant, even when internal unit tests pass.
- **Experiment:** A throwaway index prototype tests whether a bounded sample query gets faster within a named local budget. The result records measured timings and noise, leaves production paths untouched and follows the brief's state-disposal rule. Adoption requires a new accepted production task with correctness and migration acceptance.
