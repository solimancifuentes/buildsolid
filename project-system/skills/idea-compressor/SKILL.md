---
name: idea-compressor
description: Reduce a sprawling project idea into a one-paragraph product thesis and a sharp problem statement. Use this skill in Stage 2 (Idea Compression) once accepted current intent and problem evidence can ground the result, or whenever an existing thesis or problem statement has drifted and needs to be re-tightened.
---

# idea-compressor

> A BuildSolid skill. Drives Phase 2 (Idea Compression) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. It is usable on any agent harness — Claude Code's `skill-creator` is the preferred authoring tool when available, and the conventions it teaches are followed here by hand when it is not.

---

## 1. Single purpose

Compress a project's raw intent into two artifacts: a one-paragraph **product thesis** (`product-thesis.md`) and a sharp **problem statement** (`problem-statement.md`). Nothing else. The skill does **not** define MVP scope, user journeys, architecture, or the intelligence layer — those are downstream skills.

A thesis is "compressed" when it fits in one paragraph, names the user, the problem, the wedge, and where the AI layer (if any) is decisive — and removing any sentence breaks the meaning.

## 2. Trigger conditions

Invoke this skill when:

- A direct caller or the orchestrator identifies applicable Phase 2 (Idea Compression) work and accepted current intent plus problem evidence supply the genuine inputs. For a New Product Build, `founder-intent.md` and `discovery.md` are the default owners. For Existing Project Change or Lightweight/Internal Build, an accepted `spec.md`, `plan.md`, current product record, research record, or another equivalent owning artifact may supply unchanged context; require discovery only when the requested outcome genuinely depends on unresolved discovery evidence.
- A user explicitly asks to "compress the idea," "draft the thesis," "write the problem statement," or "tighten the pitch."
- An existing `product-thesis.md` or `problem-statement.md` has drifted from its applicable accepted intent or evidence owner (caught during a review or a substantive Phase 13 iteration) and must be re-anchored.
- A later-phase skill (e.g., `mvp-scope`, `ux-minimalist`) reports it cannot ground a decision because the thesis is missing or fuzzy.

Direct invocation is valid when this skill is named or its purpose matches and current accepted intent and the evidence genuinely needed for compression exist, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when the applicable accepted intent is missing, still raw, or materially contradictory. For a New Product Build, route to `founder-discovery`. For Existing Project Change or Lightweight/Internal Build, route to the accepted owner's producer; use `founder-discovery` only when intent, audience, product direction, or genuinely required discovery evidence is unresolved. A missing file by itself is not a reason to rediscover accepted context.

## 3. Inputs

Genuine required inputs depend on the applicable lifecycle slice:

- For New Product Build, accepted `founder-intent.md` and `discovery.md` are the default inputs and supply the founder, audience, motivating insight, observations, findings, and current alternatives.
- For Existing Project Change or Lightweight/Internal Build, accepted `spec.md`, `plan.md`, existing thesis/problem artifacts, current product or research records, or another equivalent owning artifact may supply unchanged intent and adequate evidence. Require only the owners and evidence needed to produce a traceable thesis and problem statement; do not force rediscovery or create dummy upstream artifacts.

Optional context:

- `decisions.md` — for prior thesis attempts and the reasons they were superseded.
- The resolved project profile and interaction mode. Resolve them from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference and ask only when ambiguity would materially change workflow depth, behavior, risk, scope, acceptance, or output.

User context the skill uses when available:

- A correction when the primary user represented by the applicable accepted intent is no longer current.
- Any thesis sentences the founder has already drafted, even rough ones.

If no accepted owner establishes intent well enough to avoid inventing it, this skill stops and returns the blocker to the caller. Route to `founder-discovery` for genuinely unresolved intent or discovery; otherwise route to the missing accepted owner's producer. Use the orchestrator only when cross-stage routing or continuity is needed.

## 4. Outputs

Files this skill produces or updates:

- `product-thesis.md` — filled per the `project-system/templates/product-thesis.md` shape: §1 thesis paragraph, §2 wedge, §3 audience line, §4 why-now. Optional sections (tagline, what-the-thesis-is-not) only if they materially clarify intent.
- `problem-statement.md` — filled per the `project-system/templates/problem-statement.md` shape: §1 who has the problem, §2 the problem, §3 why it persists, §4 current alternatives, §5 severity and frequency.

Shape rules:

- Both files are plain markdown, edit-in-place per `framework/docs/constitution.md` §3 principle 9.
- The thesis is **one paragraph** of 4–8 sentences. Multi-paragraph theses fail the skill's done criteria.
- The problem statement avoids solutions and feature lists; it describes the problem and its alternatives.
- All blockquoted `>` guidance from the templates is removed before the artifact is considered filled.
- Every claim in either file is traceable to the applicable accepted intent or evidence owner. Untraceable claims must be flagged and either grounded in accepted evidence, resolved with the founder when material and not safely inferable, or removed. The skill never invents intent, audience, evidence, or a wedge to complete the shape.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Compress in visible steps: establish the audience, name the wedge, draft the thesis, then cut it to one paragraph while tying each cut to the applicable accepted source and resulting `product-thesis.md` or `problem-statement.md` section.
- **Founder Mode.** Treat the existing intent as a hypothesis and pressure-test thesis specificity, audience, wedge, and removable claims before writing accepted artifact language.
- **Expert Mode.** Draft the thesis and problem statement directly from the applicable accepted intent and evidence owners; surface only choices that materially change the artifacts.
- **Build Mode.** Use only when a downstream skill is blocked by a missing or contradictory thesis; resolve the specific thesis question without reopening full discovery.

In every mode, the skill writes the thesis and problem statement to disk; it never leaves them in chat.

## 6. Question policy

What the skill **must resolve**, asking only when the answer is not safely inferable from accepted state and the ambiguity materially changes the output:

- The primary user when the applicable accepted intent names more than one candidate or uses a vague abstraction ("creators," "small businesses").
- A contradiction between accepted discovery evidence and accepted intent.
- In Founder Mode, whether every thesis sentence survives the removal test; this is a pressure-test, not a mandatory question ritual.
- Explicit human authority before overwriting an existing, signed-off thesis or problem statement (treated as a high-impact action per `framework/docs/constitution.md` §9). This confirmation is never inferred.

What the skill **may assume**:

- Accepted current content in the applicable intent and evidence owners is authoritative for this task unless contradicted by higher-precedence accepted state or the current instruction.
- A profile or mode that is unambiguous from the current instruction or accepted state, provided the inference is stated. Ask only if competing choices would materially change this work.
- The reference-example pointer target (`project-system/examples/photographer-saas/product-thesis.md`, `project-system/examples/photographer-saas/problem-statement.md`) without re-confirming.

How the skill **confirms before destructive actions**:

- Overwriting an existing signed-off thesis or problem statement requires explicit human confirmation regardless of mode.
- A supersede event (the new thesis differs materially from the prior one) is logged in `decisions.md` with the prior thesis quoted.

Asking mechanism: prefer `AskUserQuestion` when the harness provides it; fall back to plain inline questioning otherwise (`framework/docs/constitution.md` §9, §14).

## 7. Done criteria

The skill has finished when **all** are true:

- `product-thesis.md` exists at the project's standard location, with §§1–4 filled, no `<…>` placeholders, no blockquoted `>` guidance, and §1 is exactly one paragraph of 4–8 sentences.
- `problem-statement.md` exists, with §§1–5 filled, no placeholders, no leftover guidance.
- Every claim in both files is grounded in the applicable accepted intent or evidence owner, or has been explicitly supplied or confirmed by the founder.
- Cross-references in both files resolve for applicable artifacts; an inapplicable optional artifact is not required solely to satisfy this check.
- If a prior thesis or problem statement was superseded, the supersede is logged in `decisions.md`.
- The completed artifacts and readiness result are returned to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed; otherwise identify `mvp-scope` as the next applicable skill without a mandatory notification.

The user's signal that the skill is done is reading the thesis paragraph aloud and not wincing.

## 8. Failure modes

- **Accepted intent missing or empty.** Stop. Return the blocker to the caller and route to the applicable owner's producer; route to `founder-discovery` when intent, audience, or product direction is genuinely unresolved. Use the orchestrator only when cross-stage coordination or continuity is needed. Do not invent intent.
- **Genuinely required evidence thin or absent.** If accepted context safely supports a bounded partial-evidence treatment, state that inference and proceed at proportionate depth. Otherwise ask about the material evidence gap or route to `founder-discovery`. Do not require discovery merely because a `discovery.md` file is absent, and record a decision only when the treatment resolves a meaningful judgment or tradeoff.
- **Multiple plausible primary users.** Ask the material disambiguation question (per §6). If ambiguity remains, write the thesis around the user the founder picks and record the alternative as an Anti-persona in `problem-statement.md` Optional C.
- **No real wedge.** If, after pressure-testing, the project's wedge reduces to "easier UX" or "AI-powered <X>" with no concrete delta, surface this to the user and stop. Do not invent a wedge. Route to Phase 1 through `founder-discovery` when the gap is genuinely a discovery problem; otherwise route to the accepted owner's producer. Use the orchestrator only when coordination is needed.
- **Thesis cannot be compressed to one paragraph.** Treat as a signal that scope is too broad. Hand the project back to `founder-discovery` or `mvp-scope` to narrow before re-attempting compression.
- **Conflict with `decisions.md`.** If a logged decision contradicts the new thesis, either supersede the prior decision (with rationale) or revise the thesis. Do not silently disagree with the decisions log.
- **Out-of-scope request.** If the user asks the skill to also draft `mvp-scope.md`, `architecture.md`, etc., redirect: "that is `mvp-scope` / `technical-planner`'s job; I will hand off when the thesis is filled."

## 9. Portability note

The skill itself is plain markdown and contains no Claude-Code-only behavior. It runs on any competent AI coding agent.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion` if the harness provides it. Agent-neutral fallback: plain inline questioning (`framework/docs/constitution.md` §9 / §14).
- **Authoring this file.** When edits to this `SKILL.md` are needed, prefer Claude's `skill-creator` if available. Fallback: hand-edit the file following the §11 sections directly.
- **Subagents.** A reviewer subagent may be used in Founder Mode to pressure-test thesis sentences in parallel with drafting (Claude Code's `Task`/`Agent` tool). Fallback: do the pressure-test inline in the main session.

No Conductor- or Spec-Kit-only assumptions appear in this skill. If the project uses Conductor, the thesis and problem statement still belong in tracked project artifacts, never in `.context/` (`framework/docs/constitution.md` §13).

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 2 fills:

- `project-system/examples/photographer-saas/product-thesis.md` — a compressed synthetic hypothesis with a prospective under-fifteen-minute time target for a 600-image shoot, not an achieved result.
- `project-system/examples/photographer-saas/problem-statement.md` — synthetic problem and comparison hypotheses spanning hosted galleries, self-hosted delivery, Lightroom plus emailed JPEGs, desktop AI cullers, and doing nothing; no market research is claimed.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10). If the example evolves, the skill points at the new section without copying its content here.
