# <Project> — Tasks

> **Purpose.** Discrete, verifiable work units that turn [`plan.md`](plan.md) into a buildable backlog. Tasks are organized by phase. Each task is small enough for a single agent session and is reviewed against [`plan.md`](plan.md), [`spec.md`](spec.md), and the project's principles.
>
> **Workflow phase.** Phase 8 — Task Breakdown.
>
> **Driving skill.** `task-breakdown`.
>
> **How to use this template.**
> - Replace `<Project>` and any `<…>` placeholder with project-specific content.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the file filled.
> - Stable headings — the QA reviewer and security reviewer skills rely on them.
> - **One task = one verifiable outcome.** If a task is too big to verify in one pass, split it.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Required after impact analysis** for Existing Project Change, and **Required** for Lightweight/Internal Build before Build Mode or implementation begins. Include only the implementation phases and task groups in the applicable lifecycle slice.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it decomposes the plan into small verifiable tasks with files, inputs, acceptance, dependencies, parallelization, and review gates, at the depth selected by the profile. Placeholder cleanup alone is not enough.
> - **Stage 9 support.** During implementation, use each task's `Status` field per `framework/docs/context-package.md` §8E's Stage 9 implementation-support procedure.
> - **Reference example fill:** `project-system/examples/photographer-saas/tasks.md`.

Project-level governing artifacts, subject to the BuildSolid Framework, use this precedence:

1. [`decisions.md`](decisions.md), when present
2. [`spec.md`](spec.md)
3. [`plan.md`](plan.md)
4. This task file

If these sources conflict, stop and name the conflict. Update the stale owning artifact in place before implementation; no narrower task, plan, or spec silently overrides a higher-precedence accepted source.

---

## How to read this file

Each task uses this shape:

```
### <ID> — <Title>
**Description:** what the task does and why.
**Files:** the files created or modified.
**Inputs:** what the agent must read before starting.
**Acceptance:** the verifiable outcome.
**Status:** Not started / In progress / Blocked / Done.
**Parallelizable:** yes / no / yes-after-<ID>.
**Review:** which Checkpoint or review gate applies (plan §9).
**Dependencies:** task IDs that must be accepted first.
```

**ID format.** Use a phase-letter + number scheme (e.g., `A1`, `B2`, `C3`). Choose phase letters that match [`plan.md`](plan.md) §5.

**Default rules every task inherits.**

- The project's [`spec.md`](spec.md) governs scope. Accepted non-goals in the spec, plan, or another applicable owning artifact hold throughout; [`non-goals.md`](non-goals.md) applies when present and relevant to the affected work.
- Task decomposition depth follows the project profile resolved and stated for the current work. Use a durable choice in [`founder-intent.md`](founder-intent.md) when one exists; ordinary session posture need not be persisted. Do not add a fourth profile or numeric risk tier.
- Include only applicable implementation phases and task groups. Remove unused example phase headings; do not create an N/A-only task group or full lifecycle ledger. Existing `N/A - reason: <reason>` records remain valid, while material exclusions belong in the compact impact outcome or another accepted owning artifact.
- For Existing Project Change, confirm that the direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions are clear in the accepted [`spec.md`](spec.md), [`plan.md`](plan.md), this file, or another owning artifact. Carry an item into tasks only when it affects task execution; do not duplicate the compact outcome across every artifact.
- Task `Status` uses only these values: `Not started`, `In progress`, `Blocked`, or `Done`.
- Ask only when missing intent, authority, safety context, or another genuine prerequisite is materially ambiguous and cannot be inferred safely from accepted artifacts or current instruction. State safe inferences and do not re-ask questions already answered on disk.
- Meaningful accepted choices, overrides, deferrals, rejections, and tradeoffs are recorded in [`decisions.md`](decisions.md). Ordinary same-scope correction keeps task, review, pull-request, or change provenance instead.
- Irreversible or high-impact actions require explicit human confirmation regardless of mode.

> Add any project-specific default rules here (e.g., a project-wide testing requirement, a convention for commit messages). Keep them short.

---

## Phase A — <name>

### A1 — <task title>

**Description:** <…>.
**Files:** <…>.
**Inputs:** <…>.
**Acceptance:** <…>.
**Status:** Not started.
**Parallelizable:** <…>.
**Review:** <Checkpoint A>.
**Dependencies:** <…>.

### A2 — <task title>

**Description:** <…>.
**Files:** <…>.
**Inputs:** <…>.
**Acceptance:** <…>.
**Status:** Not started.
**Parallelizable:** <…>.
**Review:** <…>.
**Dependencies:** <…>.

> Add more tasks per applicable phase as needed. Repeat the same shape for each phase letter, and remove unused example phase headings rather than filling them with N/A-only groups.

---

## Phase B — <name>

> Add tasks for Phase B.

---

## Phase C — <name>

> Add tasks for Phase C.

---

## Task index

> Optional running index of tasks by phase. Useful when the backlog grows beyond a few dozen items.

| Phase | Count |
|---|---|
| A — <…> | <n> |
| B — <…> | <n> |
| C — <…> | <n> |
| **Total** | <n> |
