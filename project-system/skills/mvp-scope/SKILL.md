---
name: mvp-scope
description: Define the smallest valuable build that proves the project's product direction, and lock the cuts as explicit non-goals. Use this skill in Stage 3 (MVP Scope) once the relevant product and problem basis is accepted, or whenever a material scope question needs to be resolved or re-narrowed.
---

# mvp-scope

> A BuildSolid skill. Drives Phase 3 (MVP Scope) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Produce two paired artifacts: an `mvp-scope.md` defining the smallest valuable build that proves the thesis, and a `non-goals.md` that locks the cuts so they do not silently re-enter scope.

The skill enforces minimalism (`framework/docs/constitution.md` §3 principle 3, §7). It does **not** design UX, architecture, or the AI layer — it only decides what is in and what is explicitly out.

## 2. Trigger conditions

Invoke this skill when:

- A direct caller or the orchestrator identifies applicable Phase 3 work and accepted current state supplies the product direction, problem basis, and constraints genuinely needed for the scope decision.
- A user asks to "define the MVP," "draw the scope line," "list non-goals," or "cut the scope."
- A later-phase skill (e.g., `ux-minimalist`, `technical-planner`) reports it cannot ground a decision because scope is unclear.
- A material scope question arises from accepted project state, including scope that changed during a substantive Phase 13 iteration.

Direct invocation is valid when this skill is named or its purpose matches and the caller supplies a current thesis/problem or a material scope question grounded in current accepted inputs, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when the product direction or problem basis needed for the scope decision is missing or fuzzy. Route to `idea-compressor` or `founder-discovery` as appropriate; use the orchestrator only when cross-stage coordination or continuity is needed.

## 3. Inputs

Genuine required inputs depend on the applicable lifecycle slice:

- For New Product Build, accepted `product-thesis.md`, `problem-statement.md`, and `founder-intent.md` supply the thesis, problem, success definition, and constraints.
- For Existing Project Change or Lightweight/Internal Build, accepted current `spec.md`, `plan.md`, existing scope artifacts, or another owning artifact may supply the unchanged product/problem basis and affected constraints. Require only the inputs needed for the material scope question; do not force upstream rediscovery or dummy artifacts.

Optional context:

- `discovery.md` — for evidence behind which capabilities are actually needed.
- `decisions.md` — for prior scope decisions and superseded cuts.
- The resolved project profile and interaction mode. Resolve them from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference and ask only when ambiguity would materially change workflow depth, behavior, risk, scope, acceptance, or output.

User context the skill expects:

- Confirmation of the founder's effort budget (weeks of solo work, or equivalent).
- Any capabilities the founder considers non-negotiable, and any they are willing to defer.

## 4. Outputs

Files this skill produces or updates:

- `mvp-scope.md` — filled per `project-system/templates/mvp-scope.md`: §1 thesis the MVP must prove, §2 in-scope (must-haves) with reasons, §3 explicit cuts, §4 success criteria, §5 failure criteria, §6 time/effort budget. Optional sections (phased path, external dependencies, deferred AI capabilities) only when materially useful.
- `non-goals.md` — filled per `project-system/templates/non-goals.md`: §1 product non-goals, §2 user-segment non-goals, §3 business-model non-goals, §4 technical non-goals, §5 AI non-goals, §6 process for revisiting non-goals.

Shape rules:

- For a New Product Build and a typical solo MVP, §2 of `mvp-scope.md` should land at **3–7 must-haves**. More than 7 → push back, cut. Existing Project Change and Lightweight/Internal Build use the smallest set that is semantically ready for the affected scope question; do not invent capabilities to reach the New Product range.
- Every cut in §3 of `mvp-scope.md` becomes a corresponding entry in `non-goals.md`.
- Every non-goal includes its reason — a non-goal without a "because" is incomplete (`project-system/templates/non-goals.md` §1 rule).
- Both files are edited in place; no parallel versions (`framework/docs/constitution.md` §3 principle 9).
- Cross-references to other artifacts resolve at the point the skill exits.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Translate thesis to MVP scope visibly, separating thesis-proving capabilities from comfort features and writing paired non-goals.
- **Founder Mode.** Pressure-test each must-have against thesis proof and reject capabilities that prove a different thesis or smuggle in platform scope.
- **Expert Mode.** Draft the smallest defensible must-have set from the applicable accepted product and problem basis; for a typical New Product MVP, 3–7 items is the default. Surface only scope choices where reasonable builders would disagree.
- **Build Mode.** Use only when a downstream skill is blocked by unclear scope; confirm or refute the specific capability's in-scope/out-of-scope status.

In every mode, the skill writes both files to disk and ensures the cuts in `mvp-scope.md` §3 are mirrored as non-goals.

## 6. Question policy

What the skill **must** ask:

- The founder's effort budget when no accepted constraint names one and the budget materially changes the scope decision.
- For any capability labeled "must-have" that is not grounded in the applicable accepted product or problem source, an explicit "why is this required to prove the product direction?" question.
- For any non-goal the founder is unsure about, the reason — not the answer; the reason a non-goal exists is what prevents it from being relitigated.
- Confirmation before overwriting an existing, signed-off `mvp-scope.md` or `non-goals.md` (high-impact action per `framework/docs/constitution.md` §9).

What the skill **may assume**:

- Accepted current content in the applicable product and problem owners is authoritative for this task unless contradicted by higher-precedence accepted state or the current instruction.
- The minimalism rule applies (`framework/docs/constitution.md` §7) — when two options work, pick the smaller.
- A profile or mode that is unambiguous from the current instruction or accepted state, provided the inference is stated. Ask only if competing choices would materially change this work.

How the skill **confirms before destructive actions**:

- Removing a previously accepted in-scope capability requires a logged decision in `decisions.md` and explicit confirmation.
- Promoting a non-goal back into scope requires the same.

Asking mechanism: prefer `AskUserQuestion` when available; fall back to plain inline questioning.

## 7. Done criteria

- `mvp-scope.md` is filled, with §§1–6 complete, no placeholders, and no leftover guidance. For a New Product Build and a typical solo MVP, §2 contains 3–7 must-haves, each with a one-line reason. Existing Project Change and Lightweight/Internal Build contain the smallest semantically ready must-have set for the affected scope question, with a reason for each actual item and no invented filler.
- `non-goals.md` is filled, with §§1–6 complete, every non-goal naming its reason.
- Every cut in `mvp-scope.md` §3 has a matching entry in `non-goals.md`.
- The success and failure criteria in `mvp-scope.md` §§4–5 are concrete enough to recognize when met.
- The effort budget in `mvp-scope.md` §6 is consistent with the applicable accepted constraint owner, normally `founder-intent.md` §5 for New Product Build.
- Cross-references resolve.
- The completed artifacts and readiness result are returned to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed; otherwise identify `ux-minimalist` as the next applicable skill without a mandatory notification.

## 8. Failure modes

- **Applicable product direction or problem basis missing or fuzzy.** Stop. Return the blocker to the caller and route to `idea-compressor` when the thesis/problem owners are genuinely affected; otherwise route to the applicable accepted owner's producer. Use the orchestrator only when cross-stage coordination or continuity is needed.
- **More than 7 must-haves in a typical New Product MVP.** Refuse to finalize until the list is cut. Help the founder identify which items prove a different (larger) thesis. If the founder insists, log the deviation in `decisions.md` and proceed under protest. For Existing Project Change or Lightweight/Internal Build, judge readiness by the affected scope question rather than inventing or cutting toward a fixed count.
- **Effort budget exceeds one quarter of solo work.** Push back: the MVP is probably not minimal. Suggest cutting either §2 must-haves or §4 success criteria.
- **Non-goal without a reason.** Reject the entry; ask the founder for the reason. A non-goal with no reason will be relitigated.
- **Conflict with the applicable accepted product or problem basis.** If a must-have is not traceable to an applicable accepted owner, surface the conflict. Either update the affected owner through its proper skill and authority path, or remove the must-have.
- **Conflict with `decisions.md`.** If a logged decision contradicts a proposed cut, supersede the prior decision (with rationale) or revise the scope.
- **Out-of-scope request.** If the user asks the skill to also draft `user-journeys.md` or `architecture.md`, redirect to the appropriate downstream skill.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; fall back to plain inline questioning.
- **Subagents.** A reviewer subagent may be used in Founder Mode to challenge each must-have in parallel. Fallback: pressure-test inline.
- **Skill authoring.** Prefer `skill-creator` for edits to this file; otherwise edit by hand.

No Conductor- or Spec-Kit-only assumptions. The artifacts produced live in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 3 fills:

- `project-system/examples/photographer-saas/mvp-scope.md` — seven must-haves spanning upload, neutral AI suggestions, photographer review, delivery, client selections, finalize notification, and gallery-status dashboard, plus the file's explicit deferred cuts and prospective success/failure criteria.
- `project-system/examples/photographer-saas/non-goals.md` — product, audience, business-model, platform, and AI boundaries that lock those cuts, while preserving the one narrow retention purge required by the deletion commitment.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
