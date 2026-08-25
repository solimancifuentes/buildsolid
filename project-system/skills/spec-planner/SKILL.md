---
name: spec-planner
description: Produce and maintain a project's spec.md and plan.md in a Spec Kit-compatible shape. Use this skill in Stage 7 (Spec Creation) when the authoritative inputs affected by the current lifecycle slice are accepted, to turn them into a builder-ready spec and plan.
---

# spec-planner

> A BuildSolid skill. Drives Phase 7 (Spec Creation) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Produce and maintain `spec.md` and `plan.md` for a downstream BuildSolid project, in a shape that is **compatible with Spec Kit conventions** but does not require Spec Kit to be installed or invoked. The skill turns the upstream artifacts (thesis, scope, journeys, intelligence layer, architecture) into a builder-ready spec (what must be true to ship) and plan (how it gets built).

The skill does **not** break the plan into individual tasks (that is `task-breakdown`), implement code, or execute the spec. It produces the contract.

## 2. Trigger conditions

Invoke this skill when:

- A direct caller names `spec-planner`, or the requested outcome matches its purpose, and the authoritative inputs affected by the current lifecycle slice are accepted and current.
- The orchestrator routes the project to Phase 7 with the same prerequisites satisfied.
- A user asks to "draft the spec," "write the plan," "produce the builder-ready docs," or "make this Spec-Kit-compatible."
- A later-phase skill (`task-breakdown`, `qa-reviewer`) reports it cannot ground a decision because the spec or plan is missing or stale.
- A substantive Phase 13 iteration changes goals, non-goals, or acceptance criteria and the accepted spec/plan must be re-aligned.
- For Existing Project Change, the §8E compact impact outcome selects Stage 7 or an earlier entry whose affected work reaches Stage 7.

Direct invocation is valid only when the genuine accepted prerequisites for the applicable slice are current, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when a genuine prerequisite for the affected scope is missing, stale, or conflicting. Block or route to its owning skill; route through the orchestrator only when cross-stage coordination or continuity is needed.

## 3. Inputs

Genuine required inputs depend on the applicable lifecycle slice:

- For New Product Build, accepted `product-thesis.md`, `problem-statement.md`, `mvp-scope.md`, `non-goals.md`, `user-journeys.md`, and `architecture.md`; include `intelligence-layer.md` when AI is load-bearing.
- For Existing Project Change, the accepted current `spec.md` and `plan.md`, the §8E compact impact outcome (direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions), and only the accepted upstream artifacts affected by the change.
- For Lightweight/Internal Build, accepted scope plus only the journeys, architecture, and other inputs genuinely needed to make the smaller applicable spec and plan reconstructable. Do not require an optional stage or empty upstream artifact solely to prove inapplicability.

Optional context:

- `founder-intent.md` — for risks the founder named up front.
- `discovery.md` — for evidence behind required capabilities.
- `decisions.md` — for prior spec/plan decisions and supersedes.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference; ask only if ambiguity materially changes the work.

User context the skill expects:

- The version label (`v0.1`, `v0.2`, …) and output location when they are already established; ask only if an unresolved choice materially changes artifact identity or placement.
- Any external constraints (regulatory, contractual, partner) the spec must inherit.

## 4. Outputs

Files this skill produces or updates:

- `spec.md` (project-level) — filled per `project-system/templates/spec.md`: §1 Overview, §2 Target users, §3 User problems, §4 Goals (each verifiable), §5 Non-goals, §6 User journeys (by reference, not restated), §7 Required capabilities, §8 Architecture summary, §9 Intelligence-layer summary, §10 Acceptance criteria (grouped by area, each a single line), §11 Risks, §12 Open questions.
- `plan.md` (project-level) — filled per `project-system/templates/plan.md`: §1 Purpose, §2 Inputs, §3 Decisions resolved at planning level, §4 File and directory structure, §5 Build phases, §6 Artifact dependencies, §7 Skill / capability creation order, §8 Sequential vs parallel work, §9 Review checkpoints, §10 Validation strategy, §11 Merge criteria, §12 Risks and mitigations.

Spec Kit compatibility is shape-only:

- The artifacts are plain markdown with the headings used by Spec Kit-aware tooling. Compatibility is a *shape* convention, not a runtime dependency. Projects without Spec Kit can read and act on these files unchanged.

Shape rules:

- `spec.md` is implementation-neutral — it says *what must be true*; the *how* is in `plan.md`.
- Goals (`spec.md` §4) are testable; vague goals are rejected.
- Open questions (`spec.md` §12) are deferred to `plan.md` or to explicit human decisions; they do not block the spec from being accepted.
- For Existing Project Change, accepted artifacts make the direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions reconstructable. Current `spec.md` and `plan.md` may carry that compact outcome; do not require a full upstream N/A ledger or duplicate it in both files.
- Planning details live in `plan.md`; mirror only a meaningful accepted choice or tradeoff into `decisions.md`.
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Build `spec.md` and `plan.md` section by section, explaining how each section constrains downstream implementation and review; ask where the answer teaches or materially shapes the artifacts.
- **Founder Mode.** Pressure-test goals, non-goals, acceptance criteria, risks, and open questions for testability and honest scope.
- **Expert Mode.** Draft both files from accepted inputs; surface only choices that materially change goals, non-goals, acceptance criteria, risk, or implementation approach.
- **Build Mode.** Use only when implementation is blocked by a specific spec or plan question; confirm or refute that point without broad redrafting.

In every mode, the skill owns both files and updates each one when the current scope affects it.

## 6. Question policy

What the skill **must** ask:

- The version label or output location only when it cannot be inferred safely and the unresolved choice materially changes artifact identity or placement.
- What makes an untraceable goal verifiable when accepted inputs do not answer that question.
- Whether a missing dependency will land before its actual downstream gate when acceptance would otherwise be ambiguous.
- Confirmation before overwriting a signed-off `spec.md` or `plan.md`.

What the skill **may assume**:

- The minimalism rule (small spec, small plan).
- Non-goals in `non-goals.md` are binding for the spec.
- The Spec Kit compatibility shape applies by default; opt-out is logged in `decisions.md`.

Resolve and state profile and mode from the sources in §3. Ask about either only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output; do not persist ordinary session posture.

How the skill **confirms before destructive actions**:

- Removing or replacing a signed-off goal, non-goal, or acceptance criterion requires a logged decision in `decisions.md`.
- Renaming a stable section heading requires a logged decision and a paired update to every dependent skill's references. **Heading-dependent skills (downstream readers of `spec.md`, `plan.md`, `tasks.md`):** `task-breakdown` (reads `spec.md` §7 / §10 and `plan.md` §5 to break the backlog), `qa-reviewer` (reads `spec.md` §10 and `plan.md` §11 to evaluate acceptance), `security-reviewer` (reads `spec.md` commitments and `intelligence-layer.md` §4 / §7 boundaries through the spec). A rename without paired updates breaks the contract these skills read against.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- `spec.md` is filled with §§1–12, no placeholders, no leftover guidance, every goal verifiable.
- `plan.md` is filled with §§1–12, no placeholders, and no leftover guidance; meaningful accepted choices or tradeoffs are mirrored into `decisions.md`.
- When journeys are applicable, the `User journeys` section in `spec.md` references the accepted journey artifact by name rather than restating it. When they are inapplicable, the spec records the material exclusion only if omission would otherwise be surprising, ambiguous, or consequential; no dummy journey artifact is required.
- The `Intelligence-layer summary` is consistent with `intelligence-layer.md` when AI is load-bearing; otherwise it states briefly that AI is not load-bearing without requiring a standalone N/A-only artifact.
- Cross-references resolve.
- The caller receives the Phase 7 result and any actual downstream gate. Return to the orchestrator only when cross-stage routing or continuity is needed.

## 8. Failure modes

- **Inputs missing.** Block and name the missing genuine prerequisite. Route to its owning skill, using the orchestrator only when coordination or continuity is needed.
- **Unverifiable goal.** Reject the entry. Ask for the test that would confirm the goal is met.
- **Spec § renamed.** Refuse silent rename. The QA and security reviewer skills key off these headings; a rename without a paired decision is a contract break.
- **Conflict between `architecture.md` and `spec.md` §8 (Architecture summary).** Stop and reconcile. Either revise the summary or update the architecture (with logged decision).
- **`plan.md` adds capabilities not in `spec.md`.** Reject. The plan describes how the spec gets built, not what gets built.
- **Existing Project Change Stage 7 re-entry lacks a clear compact impact outcome.** Block until accepted artifacts make the direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions reconstructable. Do not require duplicate `decisions.md` plus `plan.md` records or unaffected-stage N/A rows; route to the orchestrator only if cross-stage diagnosis is needed.
- **Out-of-scope request.** If the user asks the skill to also write `tasks.md`, redirect to `task-breakdown`. If they ask for code, redirect downstream of `task-breakdown`.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** A reviewer subagent may be used to draft the §10 acceptance criteria from upstream artifacts in parallel. Fallback: do it inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.
- **Spec Kit.** Compatibility is a shape convention, not a runtime dependency. Spec Kit may be invoked separately on these files; the skill itself does not require Spec Kit to function.

No Conductor-only assumptions. The artifacts live in tracked project files, never in `.context/`.

## 10. Reference example

See the freelance-photographer reference project's Stage 7 fills:

- `project-system/examples/photographer-saas/spec.md` — overview, target user (the freelance photographer), problems, goals (each testable), non-goals, journeys by reference, required capabilities (gallery, delivery link, client selection, AI suggestion), architecture summary, intelligence-layer summary, acceptance criteria, risks, open questions.
- `project-system/examples/photographer-saas/plan.md` — how the photographer MVP gets built: phases, dependencies, build order, validation strategy, merge criteria.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
