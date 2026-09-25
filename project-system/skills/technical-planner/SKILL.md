---
name: technical-planner
description: Pick the project's stack and produce architecture.md — components, data, boundaries, key decisions, and any AI-layer boundary. Use this skill in Stage 6 (Technical Architecture) once the affected scope and any experience inputs the architecture depends on are accepted, plus intelligence-layer inputs when AI is load-bearing. Optionally invokes starter-stack-advisor for a default-stack starting point.
---

# technical-planner

> A BuildSolid skill. Drives Phase 6 (Technical Architecture) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Produce `architecture.md`, describing the project's components, data model, dependencies, key architectural decisions, non-functional constraints, and the boundary between the rest of the system and the intelligence layer. Optionally call the helper skill `starter-stack-advisor` to obtain a default-stack proposal as a starting point.

The skill does **not** design the AI layer (that is `intelligence-layer-architect`), write the spec (`spec-planner`), or break work into tasks (`task-breakdown`).

## 2. Trigger conditions

Invoke this skill when:

- A direct caller names `technical-planner`, or the requested outcome matches its purpose, and the accepted scope plus any experience contract the affected architecture depends on are current; an accepted `intelligence-layer.md` is also required when AI is load-bearing.
- The orchestrator routes the project to Phase 6 with those same prerequisites satisfied.
- A user asks to "pick the stack," "draw the architecture," "write the architecture doc," or "decide the components."
- A later-phase skill (`spec-planner`, `task-breakdown`, `deployment-manager`) reports it cannot ground a decision because the architecture is unclear.
- A substantive Phase 13 iteration changes a fundamental accepted architecture decision (e.g., monolith → split service, single region → multi-region).
- For Existing Project Change, the §8E compact impact outcome selects Stage 6 or an earlier entry whose affected work reaches Stage 6.

Direct invocation is valid only when the genuine accepted prerequisites for the affected architecture are current, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when a genuine prerequisite for the affected architecture is missing, stale, or conflicting. Block or route to its owning skill; route through the orchestrator only when cross-stage coordination or continuity is needed. Do not require an intelligence-layer artifact when AI is not load-bearing.

## 3. Inputs

Genuine required inputs:

- Accepted scope sufficient to bound the architecture: normally `mvp-scope.md`, or equivalent accepted current `spec.md`, `plan.md`, or another owning artifact for Existing Project Change or Lightweight/Internal Build.
- An accepted affected journey or other experience contract only when the architecture decision depends on a user flow; do not require `user-journeys.md` for a change with no journey impact.
- Accepted non-goals or constraints relevant to the affected architecture: normally `non-goals.md`, or equivalent accepted current state.
- Accepted `intelligence-layer.md` only when AI is load-bearing or the change affects the AI boundary.
- For Existing Project Change, the compact §8E impact outcome as carried by accepted `spec.md`, `plan.md`, `tasks.md`, or another owning artifact: direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions.

Optional context:

- `founder-intent.md` §5 (constraints): technologies the founder will or will not touch.
- `design.md`: for tone/UX implications that affect rendering or rendering boundaries.
- `decisions.md`: for prior architectural decisions and supersedes.
- A `starter-stack-advisor` proposal, if the user wanted a default-stack starting point.
- Existing or intended consuming examples for the affected surface: who calls it, with what input, and what outcome or failure they need. Use actual code or accepted journeys when available; a small illustrative call can clarify a new interface without becoming a new requirement.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference; ask only if ambiguity materially changes the work.

User context the skill expects:

- Any accepted non-default stack choice the founder has already made.
- Tolerance for self-hosted vs managed infrastructure when that choice materially changes the architecture and cannot be inferred safely.

## 4. Outputs

Files or accepted sections this skill produces or updates:

- `architecture.md`: when the full architecture artifact is applicable, filled per `project-system/templates/architecture.md`: §1 architecture overview, §2 system diagram (text-based, e.g., Mermaid), §3 components, §4 data model (key entities, relationships, ownership), §5 external dependencies (each with role and fallback), §6 key architectural decisions, §7 non-functional constraints (latency, throughput, availability, cost ceiling, compliance), §8 boundary with the intelligence layer. For a New Product Build and a typical v0.1 MVP, 3–6 components and up to 5 material architectural decisions are defaults. Existing Project Change and Lightweight/Internal Build use the smallest semantically ready affected depth without invented filler. An adequate compact contract may carry the affected architecture and rationale in its existing owning section (§8B); do not create `architecture.md` solely to satisfy a filename.

Side effects:

- Each entry in `architecture.md` §6 must have a corresponding entry in `decisions.md` (`project-system/templates/architecture.md` §6 rule). A material compact architectural choice likewise follows the ordinary decision-recording threshold; routine implementation detail does not become a decision merely because it is compact.
- If `starter-stack-advisor` was invoked, the skill records the proposal-vs-final delta in `decisions.md` so future contributors understand which choices were defaults adopted vs choices made deliberately.

Shape rules:

- The system diagram in §2 is text-based (Mermaid, ASCII, or similar), with no proprietary file formats (`framework/docs/constitution.md` §4).
- Start from one or more concrete consuming uses before choosing a stack or component split: actor/caller, input, expected result and material failure. Derive the smallest interface, data invariants and ownership boundary that make those uses work, then explain the architecture that supports them. Preserve accepted constraints and existing consumers; do not treat an invented example as accepted intent.
- When a consequential design choice has real alternatives, set comparison criteria and a bounded exploration cost before sketches. Seek independent approaches when useful; one agent may draft them sequentially without seeing the later sketch in advance. Compare each against the same consuming uses, invariants and constraints, synthesize the chosen shape and record the actual tradeoff. A single sound design needs no artificial second option. Follow the optional [design comparison procedure](references/design-comparison.md).
- For a New Product Build and a typical v0.1 MVP, component count in §3 stays small (3–6) and §6 contains up to 5 material architectural decisions. More than those defaults → push back: the architecture may be ahead of the MVP. Existing Project Change and Lightweight/Internal Build are governed by the smallest semantically ready affected architecture, not fixed minimum counts.
- Stack choices are stated as decisions with reasons in §6, not as template assumptions (`project-system/templates/architecture.md` agent-neutrality rule).
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Walk from a concrete consuming use to the required interface and invariant, then explain alternatives only where they materially shape the artifact. `starter-stack-advisor` may anchor a requested default.
- **Founder Mode.** Pressure-test each actual component for necessity and require every material `architecture.md` §6 decision to survive "why not the simpler thing?" Do not add components or decisions merely to satisfy a default count.
- **Expert Mode.** Derive interfaces and invariants from accepted use, then draft the architecture, optionally seeded by `starter-stack-advisor`; surface only choices that meaningfully change constraints, cost or the AI-layer boundary.
- **Build Mode.** Use only when implementation is blocked by a specific architecture question; confirm or refute that point without broad redesign.

In every mode, the skill updates the applicable full artifact or adequate compact owning section in place. Every material §6 decision in a full `architecture.md` has a `decisions.md` entry.

## 6. Question policy

What the skill **must** ask:

- The founder's tolerance for managed vs self-hosted infrastructure only when it cannot be inferred and materially changes the architecture.
- Whether to invoke `starter-stack-advisor` only when the request does not already signal a preference and the choice materially changes how the architecture should be drafted.
- What need an untraceable §3 component serves when accepted scope and journeys do not answer the question.
- What happens when a §5 dependency without a fallback is unavailable, if no safe fallback or accepted-risk treatment can be inferred.
- Confirmation for a material change to signed-off architecture outside the current accepted scope or effects, or at an applicable reserved gate. Existing authority covers same-scope corrections; a signed-off filename alone does not require renewed approval.

What the skill **may assume**:

- The minimalism rule (smallest architecture that supports the journeys).
- Non-goals in `non-goals.md` §4 / §5 are binding.
- When AI is load-bearing, its cost ceiling is in `intelligence-layer.md` §6 and binds the architecture's cost ceiling in §7.

Resolve and state profile and mode from the sources in §3. Ask about either only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output; do not persist ordinary session posture.

How the skill **confirms before destructive actions**:

- Removing or replacing a signed-off architectural decision requires a logged decision in `decisions.md` that supersedes the prior one.
- Switching the AI provider is logged because it crosses into `intelligence-layer.md`.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- When `architecture.md` is applicable, it is filled with §§1–8, no placeholders and no leftover guidance. For bounded work, an accepted compact architecture section is semantically ready without a separate file.
- The affected design can be traced from a concrete consuming use through its interface, data invariants and ownership boundary to the selected component shape. Any material alternative comparison used declared criteria, a bounded cost, an explicit synthesis and a relevant verification path; an untested claim is labeled as such.
- For a New Product Build and a typical v0.1 MVP, §3 contains 3–6 components, each with responsibility, boundary, and (where applicable) data ownership, while §6 contains up to 5 material decisions. Existing Project Change and Lightweight/Internal Build contain the smallest semantically ready affected component and decision set, with no invented filler.
- The applicable §5 or compact equivalent lists every material external dependency with its fallback or accepted risk treatment.
- Every actual material §6 architectural decision has a reason and is mirrored into `decisions.md`; an unaffected or safely inferable choice is not promoted into a decision merely to populate the section.
- The applicable §7 or compact equivalent names targets for material non-functional constraints, or explicitly says there is no specific target.
- The applicable §8 or compact equivalent names the AI-layer boundary consistently with `intelligence-layer.md` when AI is load-bearing; otherwise it briefly states that no load-bearing AI boundary applies without requiring a standalone N/A-only artifact.
- Cross-references to applicable `mvp-scope.md`, `user-journeys.md`, `intelligence-layer.md`, `deployment.md`, and `decisions.md` inputs resolve; an inapplicable optional artifact is not required solely to satisfy this check.
- The caller receives the Phase 6 result and any actual downstream gate. Return to the orchestrator only when cross-stage routing or continuity is needed.

## 8. Failure modes

- **Inputs missing.** Block and name the missing genuine prerequisite. Route to its owning skill, using the orchestrator only when coordination or continuity is needed.
- **Interface chosen before its use is understood.** Reconstruct an actual consumer and the invariant it needs. If accepted intent cannot answer a material behavior question, route that question to its owning contract; do not select a stack to fill the gap.
- **Alternative sketches cannot be compared fairly.** Fix the same criteria and cost bound first, preserve independent reasoning where feasible, and reject an option that violates a critical invariant regardless of its popularity or elegance. Do not require multiple sketches for a routine local choice.
- **Component count > 6 for a typical New Product v0.1 MVP.** Refuse to finalize until cuts are made or the user logs an explicit deviation in `decisions.md`. For Existing Project Change or Lightweight/Internal Build, assess excess against the smallest affected architecture rather than a fixed count.
- **Dependency without a fallback.** Refuse the entry. Force a "this is acceptable risk" log in `decisions.md` if the user insists.
- **Decision without a reason.** Reject the §6 entry; ask for the reason. Decisions without reasons get re-litigated.
- **AI-layer boundary contradicts `intelligence-layer.md` when AI is load-bearing.** Stop and reconcile. Either update `intelligence-layer.md` (with a logged meaningful decision) or revise §8.
- **`starter-stack-advisor` proposal violates a non-goal.** Discard the violating layer and either substitute a non-default that respects the non-goal, or hand the layer to the user as "no default — caller must choose."
- **Existing Project Change Stage 6 re-entry lacks a clear compact impact outcome.** Block until accepted artifacts make the direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions reconstructable. Do not require duplicate `decisions.md` plus `plan.md` records or unaffected-stage N/A rows; route to the orchestrator only if cross-stage diagnosis is needed.
- **Out-of-scope request.** If the user asks for actual code (e.g., a Terraform file, a service skeleton), redirect. The skill produces the architectural artifact, not implementation. Implementation lives downstream of `task-breakdown`.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** Independent alternatives or a challenge review may use separate agents when available. Fallback: make bounded sequential sketches against the same frozen criteria, then synthesize inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.
- **`starter-stack-advisor` invocation.** The helper skill is *optional*. The skill must remain useful even when `starter-stack-advisor` is unavailable. In that case, build the architecture directly from the inputs without a default-stack starting point.

The skill itself is stack-agnostic; it does not assume a specific cloud, framework, or language. Project choices are recorded as `decisions.md` entries with reasons.

No Conductor- or Spec-Kit-only assumptions. The artifact lives in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 6 fill:

- `project-system/examples/photographer-saas/architecture.md`: a four-component shape with a data-minimized AI boundary, one neutral scorer across selected event-and-portrait types, and a narrow scheduled retention purge that does not introduce a general worker farm.
- `project-system/examples/photographer-saas/decisions.md`: records the accepted client, provider-selection criteria, worker boundary, and retention treatment. A specific provider remains unresolved until a later accepted entry names it and records the dated written commitment.

The [illustrative design comparison](references/design-comparison.md) shows how consuming examples and criteria can shape an optional bounded tradeoff. It is a method example, not observed performance or implementation evidence.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
