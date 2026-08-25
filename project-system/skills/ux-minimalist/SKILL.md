---
name: ux-minimalist
description: Drive UX direction toward fewer screens, fewer states, and clearer flows. Use this skill in Stage 4 (UX Direction) once scope is defined, updating the applicable design.md and/or user-journeys.md surface at the smallest depth the work genuinely requires.
---

# ux-minimalist

> A BuildSolid skill. Drives Phase 4 (UX Direction) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Produce or update the applicable UX direction in `user-journeys.md` (the flows the product must support) and/or `design.md` (UX principles, tone, screens, states, and patterns). New Product Build uses both paired artifacts by default. Existing Project Change and Lightweight/Internal Build touch only the affected artifact; a design-only change does not create a journey file, and a journey-only change does not create design content. The skill enforces minimalism harder than anywhere else (`framework/docs/constitution.md` §3 principle 3, §7) — cut screens, cut states, combine views.

The skill does **not** produce visual design files, component libraries, or interactive prototypes. It produces durable, agent-readable UX direction that a designer or builder can implement against.

## 2. Trigger conditions

Invoke this skill when:

- A direct caller or the orchestrator identifies applicable Phase 4 work and accepted current scope plus applicable constraints supply the genuine inputs.
- A user asks to "draft the journeys," "list the screens," "name the principles," or "tighten the UX."
- A later-phase skill (`technical-planner`, `spec-planner`) reports it cannot ground a decision because the journeys or screens are unclear.
- A substantive Phase 13 iteration adds or removes a journey and `user-journeys.md` / `design.md` need updating.

Direct invocation is valid when this skill is named or its purpose matches, accepted scope is current, an applicable journey or UX decision exists, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when scope is unclear — return control to `mvp-scope` first.

## 3. Inputs

Genuine required inputs depend on the applicable lifecycle slice:

- Accepted scope and applicable non-goals or constraints — normally `mvp-scope.md` and `non-goals.md` for New Product Build; accepted `spec.md`, `plan.md`, existing UX artifacts, or another owning artifact may supply equivalent current state for Existing Project Change or Lightweight/Internal Build.
- `product-thesis.md` only when audience, wedge, or product direction materially shapes the affected UX and that information is not already clear from accepted current state.

Optional context:

- `problem-statement.md` — for the user's day-to-day context.
- `intelligence-layer.md` — if the AI layer surfaces in the UX (read for AI-presentation guidance even though `intelligence-layer-architect` is the canonical owner).
- `decisions.md` — for prior UX decisions and superseded patterns.
- The resolved project profile and interaction mode. Resolve them from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference and ask only when ambiguity would materially change workflow depth, behavior, risk, scope, acceptance, or output.

User context the skill expects:

- The single most important user action — the one journey that, if it works, the thesis is alive.
- Any tone or voice preferences the founder has already named.

## 4. Outputs

New Product Build produces or updates both files by default. For Existing Project Change or Lightweight/Internal Build, identify whether journeys, design direction, or both are genuinely affected and touch only those artifacts.

- `user-journeys.md`, when user flows or acceptance paths are affected — filled per `project-system/templates/user-journeys.md`: §1 primary journey, §2 secondary journey only if needed, §3 third journey only with strong reason grounded in accepted scope, and §4 cross-journey patterns. Each actual journey names user, trigger, goal, success, steps, failure modes, and where AI shows up.
- `design.md`, when UX direction, screen/state behavior, tone, accessibility, or patterns are affected — filled per `project-system/templates/design.md`: §1 design principles, §2 tone and voice, §3 key screens, §4 cross-screen patterns, and §5 out-of-scope for design at the applicable depth.

Shape rules:

- When journeys apply, use the smallest set; 1–3 is the New Product default, and a third requires explicit justification in the applicable accepted scope owner.
- When design applies, principles are concrete enough that they would lead a designer to a *different* answer than the default ("clean", "intuitive" do not qualify).
- When journeys and screens both apply, key screens follow journey order, not alphabetical or hierarchical order.
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Start from user journeys before screens, then write screen/state decisions with explicit tradeoffs.
- **Founder Mode.** Pressure-test every screen against the user action it supports, whether it can be folded into another screen, and whether the tone is specific enough to guide product decisions.
- **Expert Mode.** Draft journeys and screens from the applicable accepted scope and product-direction sources; surface only UX choices that would alter architecture or acceptance criteria.
- **Build Mode.** Use only when implementation is blocked by an unclear journey, screen, state, or tone decision; confirm that point without redesigning.

In every mode, the skill writes only the affected applicable artifact or artifacts. It does not create the optional paired file solely because the skill owns both surfaces.

## 6. Question policy

What the skill **must resolve**, asking only when the answer is not safely inferable and the ambiguity would materially change the affected UX:

- The **primary journey** when journeys are affected and the applicable accepted scope owner does not make it clear.
- For any proposed third journey, whether it is required to prove the thesis or is merely convenient.
- For any new screen or state, whether it can collapse into an existing screen with a state change.
- Human authority before overwriting an affected existing, signed-off `user-journeys.md` or `design.md`.

What the skill **may assume**:

- The minimalism rule (cut, then cut again).
- Applicable accepted non-goals constrain UX even when they live outside `non-goals.md`.
- A profile or mode that is unambiguous from the current instruction or accepted state, provided the inference is stated. Ask only if competing choices would materially change this work.

How the skill **confirms before destructive actions**:

- Removing a previously accepted journey requires the applicable human authority when it changes scope or acceptance; add `decisions.md` only for a meaningful accepted judgment or tradeoff.
- Combining two screens into one uses ordinary task, review, pull-request, or change provenance unless it resolves a meaningful accepted UX tradeoff.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- For New Product Build, `user-journeys.md` and `design.md` are both semantically ready at their full default depth: the smallest 1–3 journeys, 3–6 concrete principles, the relevant tone and screens, cross-screen patterns, and design exclusions.
- For Existing Project Change or Lightweight/Internal Build, only the affected applicable artifact is created or updated at the smallest semantically ready depth. A design-only tone, accessibility, principle, screen, or state change does not create or update `user-journeys.md`; a journey-only change does not create or fill `design.md`.
- When both artifacts are applicable and affected, the screens in `design.md` §3 and the steps in `user-journeys.md` map onto each other. When only one is affected, validate it against accepted current state without making the optional paired artifact a completion gate.
- Cross-references to applicable or present scope, non-goal, intelligence-layer, and architecture artifacts resolve; do not require an optional or later artifact solely to satisfy this check.
- The completed artifacts and readiness result are returned to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed; otherwise identify `intelligence-layer-architect` as the next applicable skill when AI is load-bearing, without a mandatory notification.

## 8. Failure modes

- **More than three journeys in a New Product default.** Refuse to finalize without the applicable accepted scope owner justifying the third. If a larger journey set is accepted, record the meaningful deviation in `decisions.md` and flag the resulting risk.
- **Generic principles.** When design principles are affected, reject "clean", "intuitive", or "delightful" as sufficient direction. Resolve principles that would change a designer's answer.
- **Tone is missing or generic.** When tone is affected, "friendly and professional" is not enough; resolve concrete phrases the product would and would not say.
- **Conflict with accepted scope.** If an applicable journey covers a non-goal capability, surface the conflict; route the affected scope owner for a meaningful scope decision or remove the journey.
- **AI surfacing without `intelligence-layer.md`.** If a screen surfaces AI output but `intelligence-layer.md` does not exist, route to `intelligence-layer-architect` for the capability design before finalizing the screen; use the orchestrator only when cross-stage coordination or continuity is needed.
- **Out-of-scope request.** If the user asks for visual design files, component code, or prototypes, redirect — those are downstream-of-`spec-planner` concerns and are not in v0.1's markdown-first scope.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; fall back to plain inline questioning.
- **Subagents.** A reviewer subagent may be used to draft a "screens-that-could-collapse" list while the main agent fills `user-journeys.md`. Fallback: do it inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.

No Conductor- or Spec-Kit-only assumptions. The artifacts live in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 4 fills:

- `project-system/examples/photographer-saas/user-journeys.md` — one primary Deliver → Select → Finalize journey with scoring fallback, keeper-subset confusion, non-finalization handling, and DEC-8's exact first-iteration trigger: override rate above 50% sustained across at least three photographers in one calendar week. Secondary and third journeys are explicitly not included.
- `project-system/examples/photographer-saas/design.md` — photographer-time and photographer-control principles, two product surfaces, progressive states, a concise procedural voice, and four screens: photographer dashboard, upload plus AI review, client delivery link, and finalized selections.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
