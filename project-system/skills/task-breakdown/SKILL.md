---
name: task-breakdown
description: Turn accepted intent and approach into concrete, verifiable tasks in a full tasks.md backlog or adequate compact Markdown contract. Use in Stage 8 once the affected contract is current.
---

# task-breakdown

> A BuildSolid skill. Drives Phase 8 (Task Breakdown) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Produce or update actionable, verifiable tasks for a downstream BuildSolid project. Use `tasks.md` with the full spec/plan stack, or the task section of one adequate compact Markdown contract for bounded work (`framework/docs/context-package.md` §8B). Each task remains reviewable against accepted intent, approach, and allowed effects.

The skill does **not** execute tasks (that is downstream of Build Mode), implement code, or review completed work (that is `qa-reviewer`).

## 2. Trigger conditions

Invoke this skill when:

- A direct caller names `task-breakdown`, or the requested outcome matches its purpose, and the accepted full spec/plan or adequate compact intent/approach is semantically ready for the selected profile.
- The orchestrator routes the project to Phase 8 with those same prerequisites satisfied.
- A user asks to "break this down," "draft the backlog," "write tasks.md," or "make this buildable."
- A later-phase skill (`qa-reviewer`, `security-reviewer`) reports it cannot ground a review because tasks are missing or non-verifiable.
- A substantive Phase 13 iteration changes the accepted plan and tasks must be re-aligned.
- Stage 9 implementation drift or a missing requirement routes back under the `framework/docs/context-package.md` §8E execution procedure, and the owning accepted intent/approach has been updated first where required (`framework/docs/constitution.md` §6).

Direct invocation is valid only when the accepted full or adequate compact intent/approach is current, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when material accepted intent or approach is missing, stale, or conflicting. Block or route to `spec-planner`; route through the orchestrator only when cross-stage coordination or continuity is needed.

## 3. Inputs

Required accepted information, in full artifacts or adequate named compact sections:

- `spec.md`: for goals, non-goals, required capabilities, acceptance criteria.
- `plan.md`: for build phases, artifact dependencies, build order, validation strategy, merge criteria.
- For bounded work, the owning Markdown artifact's intent/outcome, scope/non-goals, approach/dependencies, acceptance/verification, and allowed-effects sections provide these responsibilities. A named experiment brief also provides its question, observable result, bounded budget and disposal/promotion rule.

Optional context:

- `architecture.md`: for the components tasks touch.
- `intelligence-layer.md`: for AI-layer-specific tasks (eval setup, prompt files, fallback wiring).
- `decisions.md`: for prior task-shape decisions and supersedes.
- An existing `tasks.md`: if iterating, not greenfielding.
- For Existing Project Change, the compact §8E impact outcome as carried by accepted `spec.md`, `plan.md`, `tasks.md`, or another owning artifact. It must make the direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions clear before tasks are produced.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference; ask only if ambiguity materially changes the work.

User context the skill expects:

- The phase letter scheme (typically `A`, `B`, `C`, … matching `plan.md` §5) when it is already established; ask only if ambiguity materially changes task identity or dependencies.
- Any tasks the user wants explicitly bundled or split that the skill's defaults would not.

## 4. Outputs

Files this skill produces or updates:

- `tasks.md` (project-level): filled per `project-system/templates/tasks.md`: a per-task block for every unit of work with the standard shape `### <ID> — <Title>` plus Description / Files / Inputs / Acceptance / Status / Parallelizable / Review / Dependencies. Tasks are grouped by phase letter matching `plan.md` §5.
- For bounded work, the existing owning artifact's task section may hold the actionable units, dependencies, status, acceptance/verification and review. Keep enough identity to link each unit to evidence; phase letters and all full-stack fields apply only when the full backlog is used.

Shape rules:

- One task = one verifiable outcome. If a task cannot be verified in one pass, split it (`project-system/templates/tasks.md` rule).
- Each task names the affected files or read surface, required inputs, and acceptance criterion. A read-only investigation may inspect without modifying files.
- For a full backlog, each task names its parallelizability (`yes`, `no`, `yes-after-<ID>`) and review gate (a checkpoint from `plan.md` §9). In compact form, name ownership/dependency and review when they materially affect execution.
- Dependencies are stated as task IDs that must be **accepted** first, not just authored. The draft-vs-acceptance distinction lets parallel work happen.
- When revising implementation tasks, preserve and maintain each task's `Status` field using only `Not started`, `In progress`, `Blocked`, or `Done` so Stage 9 state remains reconstructable.
- For the full backlog, phase letters match `plan.md` §5; reject ID schemes that drift from the plan. A compact single task need not invent phases.
- An optional task index by phase is added when the backlog grows past a few dozen items.
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Break work down at the selected contract's depth, tying each task acceptance criterion to accepted intent and explaining split/merge tradeoffs; ask where the answer teaches or materially shapes the backlog.
- **Founder Mode.** Pressure-test whether each task has one verifiable outcome and whether bundled tasks should be split.
- **Expert Mode.** Draft the full backlog or compact task section from accepted intent and approach; surface only choices that materially change ordering, dependencies, or parallelizability.
- **Build Mode.** Use only when implementation is blocked by an unclear or missing task; add or sharpen that task without broadly re-breaking the backlog.

In every mode, the skill writes the owning task section to disk; `tasks.md` is the owner when the full stack is used.

## 6. Question policy

What the skill **must** ask:

- Confirmation of the phase letter scheme when a full backlog uses one and ambiguity materially affects task identity.
- What done looks like when a vague acceptance criterion cannot be resolved from accepted full or compact intent and approach.
- Whether to split a task when bundled outcomes create a material ambiguity in ownership, sequencing, or acceptance.
- Human authority before a destructive or otherwise high-impact rewrite of a signed-off `tasks.md` (per `framework/docs/constitution.md` §9). Same-scope in-place sharpening under the accepted task envelope does not require a separate confirmation.

What the skill **may assume**:

- Every applicable capability needs actionable work and acceptance; a full backlog covers each spec §7 capability and plan §5 phase.
- Tasks default to `Parallelizable: yes` unless a real dependency exists; over-serializing is a common failure.

Resolve and state profile and mode from the sources in §3. Ask about either only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output; do not persist ordinary session posture.

How the skill **confirms before destructive actions**:

- Same-scope removal or merging of a previously accepted task uses ordinary task, review, pull-request, or change provenance. If it changes scope, acceptance, sequencing, or authority; records a rejection; or resolves a meaningful tradeoff, stop at the applicable human gate and append to `decisions.md` only when the resulting rationale has durable value.
- Renumbering after acceptance is avoided where possible. If necessary, preserve the supersede mapping in ordinary provenance unless the mapping itself reflects a meaningful accepted decision or tradeoff.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- The full `tasks.md` backlog covers each applicable spec §7 capability and plan §5 phase, with every standard field filled.
- An adequate compact contract has actionable tasks, affected surface, required inputs/dependencies, allowed effects, honest status, verifiable acceptance and appropriate review; missing material information blocks Stage 9.
- Every acceptance criterion is concrete enough that a reviewer can say "yes, met" or "no, not met."
- Every dependency is a real task ID, not a phantom.
- When using the full backlog, phase letters match `plan.md` §5 exactly.
- The optional task index is included when the backlog has more than ~30 items.
- Cross-references resolve.
- The caller receives the Phase 8 result and any actual Stage 9 entry gate. Return to the orchestrator only when cross-stage routing or continuity is needed.

## 8. Failure modes

- **Material intent or approach missing.** Stop and hand back to `spec-planner`; absent separate filenames alone do not block an adequate compact contract.
- **Existing Project Change impact analysis missing.** Stop before drafting or updating tasks until accepted artifacts make the §8E direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions clear. Current `spec.md`, `plan.md`, or `tasks.md` may satisfy this compact record; do not require a duplicate decision entry or full unaffected-stage ledger. Route to the orchestrator only when cross-stage diagnosis is needed.
- **Acceptance criterion is vague.** Reject the task. "Implement the gallery" is not a task; "Implement the gallery component such that journey §1 step 2 succeeds end-to-end" is.
- **Task with no affected surface or inputs.** Reject until the read or write surface and genuine inputs are clear; do not invent file mutations for a read-only investigation.
- **Dependency cycle.** Detect and refuse. Surface the cycle to the user; rebreak.
- **Task introduces work outside accepted intent or approach.** Reject. Update the owning contract first through `spec-planner` and record a meaningful changed decision when required, or drop the task.
- **Stage 9 task adjustment would hide drift.** Stop. Follow the §8E execution procedure: update affected accepted contract sections with rationale before implementation continues, and preserve task status history needed for Stage 10 review.
- **More than ~50 tasks for a v0.1 MVP.** Push back. Either the plan is over-detailed or the MVP is not minimal.
- **Out-of-scope request.** If the user asks the skill to also implement or review tasks, redirect. Implementation is Build Mode against the tasks; review is `qa-reviewer`.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** A reviewer subagent may be used to check each task's acceptance criterion against `spec.md` §10 in parallel while the main agent continues drafting. Fallback: inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.

No Conductor- or Spec-Kit-only assumptions. The artifact lives in tracked project files, never in `.context/`.

## 10. Reference example

See the freelance-photographer reference project's Stage 8 fill:

- `project-system/examples/photographer-saas/tasks.md`: the photographer backlog, broken into phases that match `project-system/examples/photographer-saas/plan.md` §5, with each task's acceptance criterion tied back to `project-system/examples/photographer-saas/spec.md` §10.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
