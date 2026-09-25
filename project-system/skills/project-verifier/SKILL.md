---
name: project-verifier
description: Create and maintain project-specific instructions that launch, diagnose, exercise, observe, and clean a real project target, with criterion-linked coverage and honest evidence. Use for Stage 9 verification and Stage 10 review support.
---

# project-verifier

> A BuildSolid verification skill under `framework/docs/context-package.md` §8E and the Skill Quality Standard in `framework/docs/constitution.md` §11.

**Purpose:** Make an accepted project's observable behavior repeatably checkable by a fresh agent. This skill does not change intended behavior, accept an unproved criterion, or substitute for independent QA review.

**Inputs:** The adequate accepted full or compact project contract, its actual implementation and existing harnesses, affected criteria and invariants, and the current repository/revision, environment, dependencies and allowed effects.

**Outputs:** Project-specific Markdown launch, doctor, drive, evidence and owned-resource cleanup instructions; a criterion-linked feature map; actual observations and an honest passed, failed, unverified or inconclusive outcome for each attempted check.

**Success:** A fresh agent can execute the instructions on the real target, reproduce the evidence and limits, identify unexecuted coverage, and clean only task-owned disposable state without weakening the accepted outcome or baseline.

## 1. Single purpose

Create and maintain project-specific procedures that exercise accepted behavior and expose what was actually verified. This skill does not implement the feature under test, declare independent Stage 10 acceptance, or make a failing outcome pass by editing its expectation.

## 2. Trigger conditions

Use directly or through Stage 9/10 routing when a project has accepted behavior to verify, a runnable target or manual observation path, and incomplete or stale verification instructions. Direct invocation needs no orchestrator preamble when the relevant contract, profile, mode and effects authority are clear. Existing verification instructions are updated in place when the project command, environment or feature map changes.

If the target cannot run, this skill still records a truthful `unverified` or `inconclusive` coverage entry and the specific missing prerequisite. It cannot claim execution from a plausible procedure alone.

## 3. Inputs

- Current accepted criteria and critical invariants from full `spec.md` / `plan.md` / `tasks.md` artifacts or adequate compact sections (§8B), plus affected journeys, design and AI requirements where applicable.
- Actual project code, existing tests, local scripts and supported commands. Read the relevant command's help or source and discover dependencies before writing instructions; do not invent a setup command or silently install tools.
- Repository, actual revision or dirty snapshot, relevant base/dependencies, runtime and environment identity, and the task's allowed effects and resource ownership. An earlier receipt is a lead to recheck, not proof of current behavior.
- Resolved profile and mode from current instruction or accepted state. Ask only when the distinction materially changes procedure depth, scope or authority.

## 4. Outputs

Write or maintain a project-local Markdown verification entry point with five usable parts:

1. **Launch:** prerequisites, exact commands, expected ready signal, bounded startup and resource owner. For a CLI, launch may simply mean invoke its actual entry point; do not create a server by default.
2. **Doctor:** independent prerequisite and health checks that distinguish a broken environment from a product failure.
3. **Drive:** concrete inputs and steps for representative success, failure/edge and relevant regression states tied to accepted criteria. A command that only lists tests is not a drive.
4. **Evidence:** expected condition, actual output or state, command/procedure, revision and environment, verifier, and evidence location. Mark each observed result `passed`, `failed`, `unverified` or `inconclusive`.
5. **Cleanup:** list only task-owned disposable processes, worktrees, files or ports and how to confirm they stopped. Preserve unknown or user-owned state.

Maintain a feature map keyed to accepted criterion or feature ID with the observation procedure, current outcome, evidence identity and unexecuted coverage. Keep this in the existing task/QA record or a linked project-local Markdown file when it helps a fresh agent. These verification files are guidance and evidence indexes, not a new canonical authority type; accepted intent remains in the owning project contract.

The [execution pilot](../../examples/execution-pilot/README.md) illustrates a project-local verification skill and feature map without a required BuildSolid runtime.

## 5. Mode behavior

Follow `framework/docs/context-package.md` §5; these are verifier-specific deltas.

- **Guided Mode.** Explain each observable check and what its result can establish; distinguish missing setup from an actual behavior failure in plain language.
- **Founder Mode.** Pressure-test whether the selected checks cover the intended user outcome and material risk, especially where a green unit test misses the journey.
- **Expert Mode.** Reuse existing harnesses and summarize passing coverage while showing failures, gaps and environment limits precisely.
- **Build Mode.** Add or run only the verification needed by the accepted task; ask when a material missing prerequisite or authority boundary blocks observation.

## 6. Question policy

Derive commands, affected criteria and permitted resources from the accepted task and repository first. Ask only when an unresolved choice changes what can be run, the expected result, the allowed effects or the value of the evidence. A manual fallback is valid when it observes the same behavior; label any part that could not be executed.

Before starting a process or changing a fixture, identify its owner and cleanup path. Do not run a deployment, use customer data, install dependencies or alter a shared baseline under an implied verification permission. Apply the governing human gate for destructive or high-impact actions. A user hold stops new verification work and task-owned writes.

If a check fails, preserve the observed output and diagnose its layer before editing: a **documented command drift** calls for correcting the instruction after confirming the real command; a **missing harness capability** calls for adding or requesting the missing check without claiming product failure; an **actual product bug** calls for a finding and implementation repair. Never weaken accepted behavior, replace a valid baseline, or edit expected output just to obtain green status.

## 7. Done criteria

- A fresh agent can find prerequisites, launch/doctor/drive/observe/clean instructions and run the applicable parts on the actual target without private chat context.
- Every in-scope feature or acceptance criterion is linked to an executed observation or explicitly labeled `unverified`/`inconclusive` with a reason. A known failure remains `failed` until a relevant later result proves correction.
- Evidence records the command or manual procedure, expected and actual condition, tested revision or dirty snapshot, material environment/dependencies and verifier. Source outputs or state can be independently inspected; a claimed success is insufficient.
- Cleanup stops only owned resources and confirms their state. A test-only fixture and a synthetic example are labeled as such; neither claims production evidence.
- Stage 10 receives the map and evidence with material limits intact. Its independent reviewer decides acceptance; this skill does not silently mark criteria complete.

## 8. Failure modes

- **No accepted criterion or relevant input.** Stop the affected check and route to its owning contract. Missing separate filenames do not block an adequate compact contract.
- **Command or setup fails before behavior is exercised.** Report the exact precondition and result as `inconclusive` or `unverified` as appropriate; inspect actual help/source. Do not call it a product pass or product bug without causal evidence.
- **Harness lacks a needed state or assertion.** Record the coverage gap and extend the harness only within the accepted task. A green partial harness never proves an untested criterion.
- **Product behavior violates accepted outcome.** Mark `failed`, retain the reproduction and send it to the implementation owner. Do not change the contract or fixture baseline to hide it.
- **Receipt or environment is stale.** Compare actual head, relevant base/dependencies and environment; rerun affected checks or mark their status stale/unverified. An unrelated documented change need not invalidate independent proof.
- **Resource ownership is uncertain.** Do not kill a process, delete files or overwrite a shared artifact. Leave the result incomplete and identify the missing ownership fact.

## 9. Portability note

The skill is plain Markdown and works with one agent in a normal checkout. Use project commands and human-readable output; optional browser, CI or host tools only improve observation when available. Where a tool is absent, use a documented manual path and mark what remains unverified. A second agent can independently execute the instructions for stronger review, but multi-agent execution is never a prerequisite.

## 10. Reference example

The [execution pilot's verification entry point](../../examples/execution-pilot/verification/SKILL.md) and [feature map](../../examples/execution-pilot/verification/feature-map.md) show project-specific launch, doctor, drive, evidence and cleanup instructions for the public synthetic CLI fixture. Its commands must be executed before any pass is claimed. The historical [photographer example](../../examples/photographer-saas/README.md) shows artifact planning only; it provides no running-code verification evidence.
