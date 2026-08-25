---
name: qa-reviewer
description: Review project implementation against spec, plan, and tasks — functional correctness, design parity with user-journeys.md and design.md, intelligence-layer adherence, and acceptance-criteria coverage. Use this skill in Stage 10 (QA and Review) once tasks have been implemented and need to be checked against their contracts.
---

# qa-reviewer

> A BuildSolid skill. Drives Phase 10 (QA and Review — functional / design pass) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Review implementation against the project's spec, plan, and tasks. Confirm each task's acceptance criterion is met, each spec §10 acceptance checkbox is checked, each design principle (`design.md` §1) holds in the implementation, and each user journey (`user-journeys.md`) walks end-to-end.

The skill does **not** perform security review (that is `security-reviewer`), implement code, or deploy. It produces a verdict and a punch list.

## 2. Trigger conditions

Invoke this skill when:

- A direct caller names `qa-reviewer`, or the requested outcome matches its purpose, and the current in-scope implementation plus accepted applicable acceptance inputs are available.
- The orchestrator routes the project to Phase 10 with those same prerequisites satisfied.
- A user asks to "QA this," "review against spec," "check the acceptance criteria," "walk the journeys," or "do a functional pass."
- Implementation work is about to merge and the spec/tasks need to be checked one more time.
- A substantive Phase 13 iteration changes accepted criteria; previously accepted work must be re-checked against them.
- Stage 9 has completed the `framework/docs/context-package.md` §8E implementation-support handoff, with in-scope `tasks.md` items marked `Status: Done` or explicitly blocked/deferred.

Direct invocation is valid only when the implementation and genuine accepted acceptance inputs are current, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when no in-scope implementation exists or when genuine acceptance inputs are missing, stale, or conflicting. Block or route to the owning skill; route through the orchestrator only when cross-stage coordination or continuity is needed.

## 3. Inputs

Required artifacts:

- `spec.md` — for goals, required capabilities, acceptance criteria.
- `tasks.md` — for the per-task acceptance criteria and review gates.
- The implementation itself (code, artifacts, configuration) the tasks produced.

Optional context:

- `plan.md` — for the validation strategy (`plan.md` §10) and merge criteria (`plan.md` §11).
- `user-journeys.md` and `design.md` — for design parity and journey walks.
- `intelligence-layer.md` — for AI-layer eval status (the eval design lives there; the *check* happens here).
- `decisions.md` — for accepted deviations from the original spec.
- `known-issues.md` if it exists — for items already accepted as known debt.
- Existing task, review, or pull-request provenance for the ordinary verdict.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference; ask only if ambiguity materially changes the review.

User context the skill expects:

- Which tasks / capabilities are in scope when accepted task, review, or pull-request context does not make that clear.
- Any acceptance deviations the user wants logged rather than blocked.

## 4. Outputs

The skill returns a review verdict and punch list to the caller. Durable recording follows the effect of the result:

- Ordinary pass/fail results and same-scope remediation use existing task, review, or pull-request provenance; they do not require a `decisions.md` entry or Stage 13 record.
- Append to `decisions.md` only when the review resolves a meaningful acceptance, rejection, exception, or tradeoff that needs durable rationale.
- Append to `known-issues.md` only when a bug, gap, or accepted debt must persist across sessions.
- The acceptance checkboxes in `spec.md` §10 may be checked or unchecked when their literal state is verified. Pair the change with a `decisions.md` entry only when it reflects a meaningful exception or acceptance judgment rather than routine verification.
- Where the review surfaces a missing or vague task, report the finding through current review provenance and hand it to `task-breakdown` for the actual `tasks.md` edit. **`qa-reviewer` does not write or modify `tasks.md` directly** — `task-breakdown` owns that file (single-purpose ownership per `framework/docs/constitution.md` §5).

The skill is read-only with respect to implementation code: it reports findings and never fixes them. Fixes are routed back to Build Mode against accepted tasks.

Shape rules:

- The review verdict names the scope, evidence checked, per-area outcome, and punch list in the current task, review, or pull-request record.
- Any durable `known-issues.md` entry is concrete (not "the gallery is buggy" — name the bug, the journey it breaks, the smallest reproduction).
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Review acceptance criteria one by one, explaining what "met" requires and recording partials clearly; ask where the answer teaches or materially changes the verdict.
- **Founder Mode.** Pressure-test whether the implementation proves the thesis and whether partial passes hide product risk.
- **Expert Mode.** Run the review directly; report failures and partials in detail, with passes summarized concisely.
- **Build Mode.** Use only when an acceptance question blocks implementation; clarify that criterion's intent without running a broad QA pass.

In every mode, the skill returns the verdict to the caller and records ordinary results in current task, review, or pull-request provenance. Durable artifact edits follow only the conditions in §4.

## 6. Question policy

What the skill **must resolve**, asking only when accepted inputs and current review context do not safely determine the answer and the ambiguity would materially change the verdict:

- The review scope (which tasks, which capabilities) if it is not already declared.
- Whether a partial is accepted debt or a blocker only when accepted criteria and authority do not already determine the disposition; record a decision only for a meaningful acceptance or tradeoff.
- How to route a fix only when current task/review context does not already establish whether `task-breakdown` must sharpen or add a task.

What the skill **may assume**:

- The artifacts on disk are the current truth; if a task is marked complete in `tasks.md` but its acceptance criterion is not met, that is a finding.
- A criterion that is binary (e.g., "the rollback procedure has been exercised") is met only when literally true.
- A `spec.md` §10 checkbox may be synchronized to its literally verified state without item-by-item user approval. That records verification; it does not accept a failing criterion, debt, deferral, or exception.
- Non-goals in `non-goals.md` are binding for the review — implementations that drift into a non-goal are findings, not bonuses.

Resolve and state profile and mode from the sources in §3. Ask about either only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output; do not persist ordinary session posture.

How the skill **confirms before destructive actions**:

- The skill does not modify implementation code or `tasks.md`. It reports needed task changes to `task-breakdown` through current review provenance.
- The skill updates `spec.md` §10 checkboxes only to match literally verified state. Actual acceptance of a failing criterion, debt, deferral, or exception remains at the applicable human gate; marking an unmet criterion checked is forbidden without that authority and a logged exception in `decisions.md`.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- Every in-scope task in `tasks.md` has been compared against its acceptance criterion; pass/fail recorded.
- Every in-scope `spec.md` §10 acceptance checkbox has been evaluated; pass/fail recorded.
- Every applicable in-scope user journey in `user-journeys.md` has been walked end-to-end; failures logged.
- Applicable design principles in `design.md` §1 have been spot-checked against the implementation when that artifact is part of the lifecycle slice.
- When AI is load-bearing, the intelligence layer has been spot-checked: a representative eval has been run against `intelligence-layer.md` §5's golden set; the result is logged.
- A review verdict is recorded in current task, review, or pull-request provenance.
- Meaningful acceptance, rejection, exception, or tradeoff decisions are appended to `decisions.md`; ordinary pass/fail results are not.
- Persistent new issues are appended to `known-issues.md`; transient or immediately remediated findings remain in ordinary review provenance.
- The caller receives the Phase 10 functional/design result and any actual security-review gate. Return to the orchestrator only when cross-stage routing or continuity is needed.

The user's signal that the skill is done is being able to point at the current review record and say "this passed, this failed, and this is deferred," with durable decisions or persistent issues recorded only where required.

## 8. Failure modes

- **Spec, tasks, or implementation missing.** Block and name the missing genuine prerequisite. Route to its owning skill, using the orchestrator only when coordination or continuity is needed.
- **Acceptance criterion is unverifiable.** Treat as a tasks-side bug. Hand back to `task-breakdown` to sharpen, then resume the review.
- **Implementation drifts from spec.** Per `framework/docs/constitution.md` §6, the spec is updated *first* (via `spec-planner` and a logged decision); only then is the implementation accepted.
- **AI-layer eval thresholds not met.** Mark the AI capability as failed; do not accept the implementation under "we'll improve the prompt later." Route back to Build Mode against `intelligence-layer.md` §5.
- **User wants to mark a failing checkbox passed.** Refuse without a logged exception in `decisions.md`. Acceptance criteria are the contract.
- **Non-goal violation in implementation.** Treat as a finding; route to `task-breakdown` for a remediation task or to `mvp-scope` if the non-goal needs revisiting (with logged decision).
- **Substantive Stage 13 re-entry reaches Stage 10 without accepted criteria.** Block until the applicable §8E human-review and accept/reject gate supplies current acceptance criteria. Same-scope bugs, review remediation, maintenance, and routine retry remain ordinary Existing Project Change and require no Stage 13 or universal decision record.
- **Out-of-scope request.** If the user asks the skill to also do a security review, redirect to `security-reviewer`. If they ask the skill to fix the bugs it finds, redirect to Build Mode.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** A reviewer subagent may be used to walk one journey end-to-end while the main agent walks another in parallel. Fallback: walk them sequentially.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.
- **Hooks / MCP.** A project may wire the QA pass into a Claude Code stop hook or an MCP-based test runner. The skill's contract is the verdict; the harness around it is optional.

No Conductor- or Spec-Kit-only assumptions. The artifacts live in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's artifact-level Stage 10 boundary:

- `project-system/examples/photographer-saas/README.md` §1 — Stage 10 has no running code or real code-review verdict and is represented at the artifact level through `known-issues.md`.
- `project-system/examples/photographer-saas/known-issues.md` — records planned gaps and intentional debt rather than observed production defects. KI-3 remains `High`/`Open` because the provider is unresolved; KI-9 is a resolved artifact-compatibility issue. No running-code or real review result is claimed.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
