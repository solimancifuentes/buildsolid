---
name: implementation-executor
description: Implement accepted project tasks in Stage 9, proving feature, bug, refactor, or bounded experiment outcomes while preserving scope and review authority. Route read-only investigation to project-investigator.
---

# implementation-executor

> A BuildSolid Stage 9 skill under `framework/docs/context-package.md` §8E and the Skill Quality Standard in `framework/docs/constitution.md` §11.

**Purpose:** Carry one or more actionable, accepted project tasks into implemented and verified behavior. This skill does not invent product intent, perform independent QA acceptance, or authorize deployment or merge.

**Inputs:** Current accepted intent, approach, actionable tasks, acceptance and allowed effects in either the full `spec.md` / `plan.md` / `tasks.md` stack or an adequate compact Markdown contract; relevant project code, decisions, dependencies, and actual Git/review state. A disposable experiment additionally needs its accepted bounded brief.

**Outputs:** Scoped implementation changes; reproducible validation results tied to the actual revision or dirty snapshot; honest task status and material outcome in the owning Markdown task section; an explicit Stage 10 handoff or blocker.

**Success:** The applicable task's intended behavior and critical invariants have been exercised with evidence, scope and effects remain inside the accepted contract, and every outcome or unverified condition is accurately recorded for review. Implementation alone does not establish independent acceptance.

## 1. Single purpose

Implement actionable accepted Stage 9 tasks and establish the observed result for the affected behavior. This skill does not write missing intent, conduct a read-only investigation, issue an independent QA verdict, or turn a disposable experiment into production code.

## 2. Trigger conditions

Use this skill when a direct caller or the orchestrator has an actionable accepted feature, bug, refactor, or bounded experiment task in the applicable lifecycle slice. Direct entry is valid when its genuine prerequisites and effects authority are clear; an orchestrator pass is not required. Use the [task-type procedures](references/task-types.md) for the matching task.

For a task with accepted visual requirements, use the optional [visual-parity procedure](references/visual-parity.md), including actual renders, interaction and accessibility observations. A non-UI task needs no screenshot ritual.

For an accepted performance or runtime-diagnosis question, use the optional [bounded performance and forensics procedure](references/performance.md): locate the relevant path, freeze the workload and decision rule, check correctness, and compare the result with observed noise before keeping a change.

For current PR/check facts, use the optional [bounded read-only observation procedure](references/observation.md). The [local helper guide](../../tools/README.md) also offers task-structure checks and factual worktree inventory with manual fallbacks. Their outputs support judgment; they never establish semantic acceptance, merge permission or cleanup authority.

Route a question whose requested outcome is explanation or diagnosis without production edits to `project-investigator`. A missing or ambiguous implementation contract routes to its owning planning skill; do not start code changes to discover acceptance criteria.

## 3. Inputs

- Accepted intent, scope and non-goals, approach and dependencies, actionable task, observable acceptance and review, and allowed effects. These may live in one adequate Markdown contract (§8B) or the full project artifact stack. Read only affected upstream artifacts; no duplicate empty files are required.
- Current project repository and code, relevant decisions, tests or manual verification procedures, and available Git/review state. Establish the actual revision, dirty changes, relevant base and dependencies, and environment before using an earlier result.
- For a bug, the expected behavior and a concrete symptom or reproduction target. For a refactor, the public behavior and invariants to preserve. For an experiment, its accepted question, boundary, observable result, time/cost/resource budget and disposal or promotion rule.
- A resolved project profile and interaction mode from current instruction, accepted durable project choice or unambiguous context. State any material inference; ask only if competing choices materially change scope, risk, acceptance or output.

Chat, handoffs and generated summaries may guide investigation but cannot establish accepted intent, completion, or current Git state.

## 4. Outputs

- Only the code, tests, configuration or documentation named or reasonably implied by the accepted task and its affected consumers. Keep one active writer per file. Reuse project harnesses; request `project-verifier` help only when a project-specific verification procedure is needed.
- A task outcome in the owning Markdown task section or existing full `tasks.md`: honest `Not started`, `In progress`, `Blocked` or `Done` status; changed surface; passed, failed, unverified or inconclusive checks; and material limits. Do not mark Done merely because code was written.
- A compact receipt for material verification: repository, tested revision or identified dirty snapshot, relevant base/dependencies/environment, command or manual procedure, observed outcome, evidence location and verifier. The receipt does not claim a clean commit when work is dirty.
- A Stage 10 handoff stating implemented scope, acceptance evidence, critical invariants checked, open failures and unverified areas. A review may inspect incomplete work without treating it as complete.

Ordinary implementation and remediation use task, review or pull-request provenance. Log a `decisions.md` entry only for a meaningful accepted change or tradeoff; use `known-issues.md` when a persistent issue needs a future reader.

## 5. Mode behavior

This skill follows `framework/docs/context-package.md` §5. These bullets describe only execution-specific differences; all four modes use the same accepted contract and evidence bar.

- **Guided Mode.** Explain the next bounded change and its observable check, then show how the result relates to the task. Ask for a material choice in a small batch when accepted inputs do not settle it.
- **Founder Mode.** Challenge a proposed implementation choice that would obscure the intended user outcome, weaken a cut, or smuggle a new product direction into a task.
- **Expert Mode.** Execute from current accepted inputs with concise decisions and evidence. Surface only a material ambiguity, risk, or tradeoff that the contract cannot resolve.
- **Build Mode.** Work directly through accepted tasks; ask only when blocked by missing or conflicting intent, authority, safety context, or a required human gate.

## 6. Question policy

Resolve the task's intended behavior, excluded effects, affected surface, dependencies, done condition and review from accepted sources first. Ask only when a missing answer would materially change the implementation or its authority. Make routine, reversible implementation choices inside the accepted envelope and state a consequential assumption in the task record.

Before each change, identify direct files and indirect consumers, critical invariants, allowed effects, one writer per file, the cheapest adequate proof, and the stop or recovery condition. A new dependency or artifact is justified only by the task's actual needs. For external, destructive or high-impact effects, apply the governing human gate and confirmation; an accepted task never implies permission for an excluded effect. Respect a user hold. For pickup, failed workers or old verification, read [resume, ownership and revision evidence](references/recovery.md).

If the observed work changes product intent, scope, acceptance or allowed effects, stop the affected implementation and update the owning contract through its required acceptance before resuming. Same-scope fixes and review remediation proceed within existing authority. Do not rewrite expected behavior or a verification baseline to hide a failing implementation.

## 7. Done criteria

- The code and any material artifact changes remain within the accepted task and affect its known direct and indirect consumers coherently.
- The relevant task-type proof in [the procedures](references/task-types.md) has actually run, or its unavailable portion is explicitly unverified or inconclusive with a reason. A bug's baseline failure is tied to the intended defect when reproducible; a refactor has public-behavior regression proof.
- The task's acceptance and applicable review condition are met before `Done` is recorded. A result remains `Blocked` if a material dependency, missing authority, or unresolved failure prevents completion.
- Evidence identifies the actual revision or dirty snapshot and relevant environment. A later change to a relevant dependency invalidates only the affected result, which is rerun or marked stale.
- The Stage 10 reviewer can reproduce or inspect the result from the owning task and linked evidence without relying on private chat memory.

## 8. Failure modes

- **Missing or conflicting contract.** Block affected files, name the missing intent, acceptance, dependency or authority, and route to `spec-planner` or `task-breakdown` as appropriate. A missing separate filename is not a blocker when the compact contract is adequate.
- **Wrong task type.** A read-only question routes to `project-investigator`; an experiment that now needs production behavior pauses for a separately accepted production contract.
- **Baseline does not reproduce.** Investigate the test or environment and explain the limit. Do not claim a bug fix from an unrelated failing test or a passing test that never exercised the defect.
- **Observed failure or weak proof.** Preserve the failure and its evidence; repair within scope, improve the harness when it cannot distinguish the result, or report unverified/inconclusive. Do not lower acceptance to obtain a pass.
- **Drift or stale result.** Stop affected implementation, reconcile current Git/review state and the owning accepted artifact, then recheck only impacted behavior. A prior receipt or handoff is not current proof.
- **Worker interruption or ownership conflict.** Apply §8E recovery: stop a failed worker and confirm potentially writing commands and processes are quiescent before reassigning files. Interruption or a late message alone is insufficient. If quiescence cannot be proved, block those files and continue independent work.
- **Out-of-envelope action.** Stop at the actual human gate. Neither task completion nor test success authorizes merge, deployment, publication or another excluded effect.

## 9. Portability note

This is plain Markdown guidance. A competent agent can apply it from one normal Git checkout using the project's existing commands and artifacts. Subagents, worktrees, host-specific test runners and browser tools may help when available, but none is a prerequisite or an authority source. With one agent, perform implementation and self-checks sequentially, then hand the result to the applicable independent Stage 10 review. If a specialized tool is unavailable, use the project's manual procedure and report what remains unverified.

## 10. Reference example

The [illustrative task-type examples](references/task-types.md#illustrative-examples) show a bounded feature, reproducible bug, behavior-preserving refactor and disposable experiment with distinct proof obligations. They are examples of decisions and expected records, not evidence that those tasks were executed. The synthetic [photographer project](../../examples/photographer-saas/README.md) demonstrates full-stack artifact compatibility. The separate [execution pilot](../../examples/execution-pilot/README.md) provides runnable validator and local browser procedures, with executed observations identified separately from instructions.
