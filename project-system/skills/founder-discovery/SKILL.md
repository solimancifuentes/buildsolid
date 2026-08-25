---
name: founder-discovery
description: Pressure-test a project's idea, audience, problem, and differentiation the way a sharp startup office-hours session would. Use this skill when discovery is explicitly requested or accepted intent, audience, problem, or differentiation is unclear and Stage 1 work is applicable.
---

# founder-discovery

> A BuildSolid skill. Powers Founder Mode for Phase 1 (Founder Discovery) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6, §5. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Run a structured pressure-test of the project's intent — who it is for, what problem it addresses, why now, what the wedge is — and capture the result in the applicable intent or discovery artifact. New Product Build uses `founder-intent.md` plus `discovery.md` by default; Existing Project Change and Lightweight/Internal Build update only the artifacts genuinely affected. The skill challenges the founder's assumptions before the project commits to a thesis.

The skill does **not** write the thesis (`idea-compressor` does), define scope (`mvp-scope` does), or draw architecture. Its only job is to make the inputs to those skills honest.

## 2. Trigger conditions

Invoke this skill when:

- A direct caller or the orchestrator identifies applicable Phase 1 (Founder Discovery) work because `founder-intent.md` and/or `discovery.md` are empty, sparse, marked draft, or materially unclear.
- The user explicitly requests discovery or asks to pressure-test the project's intent, audience, problem, or differentiation.
- The user enters **Founder Mode** for an existing project and asks to pressure-test accepted assumptions.
- A later-phase skill (`idea-compressor`, `mvp-scope`, `intelligence-layer-architect`) reports the inputs are too thin or self-contradictory and the project must return to discovery.
- A substantive Phase 13 iteration surfaces a fundamental change in audience or problem framing.

Direct invocation is valid when this skill is named or its purpose matches, the current raw idea or accepted project state supplies its genuine inputs, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

This is the **primary skill for Founder Mode**, not a Founder-Mode-only skill. Guided, Expert, and Build modes may invoke it when discovery is genuinely incomplete or materially affected.

## 3. Inputs

Genuine required inputs, supplied by accepted current state and/or the user:

- A raw or accepted description of the idea at the depth needed for the applicable discovery question.
- A current audience hypothesis, however rough.
- A current belief or open question about why this project could win.

Use accepted current state rather than asking the user to restate it. Ask only when a missing or conflicting input is not safely inferable and materially changes the discovery outcome. Never invent an audience, motivating insight, observation, or wedge to fill a template.

Optional artifacts on disk:

- `founder-intent.md` — if a draft exists, the skill sharpens it; if empty, the skill fills it.
- `discovery.md` — same.
- `decisions.md` — for prior framing decisions and superseded answers.
- The resolved project profile and interaction mode. Resolve them from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference and ask only when ambiguity would materially change workflow depth, behavior, risk, scope, acceptance, or output.

The skill does **not** require any other artifacts to exist. It is the earliest skill in the workflow.

## 4. Outputs

New Product Build produces or updates both files by default. Existing Project Change and Lightweight/Internal Build update `founder-intent.md` only when durable intent, audience, constraints, or choices are affected, and update `discovery.md` only when audience, problem, alternative, or other discovery evidence is collected or materially revised. Do not create either artifact solely because the paired skill ran.

- `founder-intent.md`, when applicable — filled per `project-system/templates/founder-intent.md`: §1 who the founder is, §2 who this is for, §3 why this exists, §4 what success looks like (3–5 bullets), §5 constraints named up front, and §6 any profile or mode choice intentionally adopted as durable project state. Do not record transient session posture in §6. Optional sections only when materially clarifying.
- `discovery.md`, when applicable — filled per `project-system/templates/discovery.md`: §1 who was talked to or observed, §2 raw observations, §3 structured findings, §4 current alternatives, §5 hypotheses to test next. The template's fuller counts are the New Product default; other profiles use the smallest evidence set that is semantically ready for the affected discovery question.

Shape rules:

- When `founder-intent.md` is affected, it is concise — short paragraphs and tight bullets. The agent that reads this next should grasp the relevant intent in under two minutes.
- When `discovery.md` is affected, it separates raw observations (§2) from structured findings (§3); the skill resists summarizing in §2.
- In an applicable `discovery.md`, a theme in §3 is only worth keeping if it is grounded across the evidence available at the selected profile's proportionate depth (`project-system/templates/discovery.md` §3 rule).
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Founder Mode (primary).** Pressure-test applicable audience, problem, wedge, willingness-to-pay, and alternative claims before the affected intent or discovery artifact is treated as ready. Ask in small, focused batches.
- **Guided Mode.** Cover the same discovery claims with more scaffolding and short explanations tied to the artifact sections being filled.
- **Expert Mode.** Read applicable accepted intent and discovery state first; question only weak or contradictory assumptions instead of replaying full discovery.
- **Build Mode.** Use only when discovery is missing for a downstream phase; ask or record only the discovery decision that unblocks the build.

In every mode, the skill writes meaningful durable information only to the affected applicable artifact. It never creates the optional paired artifact merely to complete the skill and never relies on chat as the durable record.

## 6. Question policy

What the skill **must resolve**, asking only when the answer is not safely inferable from accepted state and the ambiguity materially changes the output:

- What happens to the user if no one builds this.
- The concrete delta between each material claimed differentiator and its closest current alternative.
- Whether each material named audience is a real, specific population rather than a convenient abstraction; the ability to identify representative members is a useful test, not a mandatory question ritual.
- Why now: what changed recently enough to make the project possible or attractive, or the honest conclusion that nothing changed and the need has long been under-served.
- Explicit human authority before overwriting an affected existing, signed-off `founder-intent.md` or `discovery.md`. This confirmation is never inferred.

What the skill **may assume**:

- A profile or mode that is unambiguous from the current instruction or accepted state, provided the inference is stated. Ask only if competing choices would materially change this work.
- That a non-empty `founder-intent.md` reflects the founder's current beliefs unless contradicted.
- The reference-example pointer target (`project-system/examples/photographer-saas/founder-intent.md`, `project-system/examples/photographer-saas/discovery.md`) without re-confirming.

How the skill **confirms before destructive actions**:

- Overwriting a signed-off `founder-intent.md` or `discovery.md` requires explicit confirmation.
- Retracting a previously named audience or wedge is logged in `decisions.md`.

Asking mechanism: prefer `AskUserQuestion` when the harness provides it; plain inline questioning otherwise.

## 7. Done criteria

- For New Product Build, `founder-intent.md` retains §§1–6 with §§1–5 filled, and `discovery.md` is filled with §§1–5 using the default minimum evidence depth: at least 3 sources, 3 raw observations, 2 themes, 3 alternatives (including silent ones), and 1 hypothesis. The audience is specific enough to identify representative members, and the material wedge has a concrete delta against an alternative.
- For Existing Project Change or Lightweight/Internal Build, only the affected applicable artifact is created or updated. `founder-intent.md` remains a required read and is updated only when its durable content changes; `discovery.md` remains conditional or optional and is required only when discovery evidence is collected or materially revised.
- At those proportionate profiles, the affected artifact contains the smallest evidence and specificity needed for the actual discovery question. A one-operator internal tool may name that operator without inventing a five-person audience, and an inapplicable `discovery.md` or alternative comparison is not a completion gate. Do not invent sources, observations, themes, alternatives, hypotheses, or audience members.
- Cross-references resolve.
- The completed artifacts and readiness result are returned to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed; otherwise identify `idea-compressor` as the next applicable skill without a mandatory notification.

The user's signal that the skill is done is being able to answer "who is this for?" and "what does it do better than X?" without hesitation.

## 8. Failure modes

- **Founder describes a "platform" or "ecosystem".** Stop. Ask for the single first user. Refuse to fill the artifacts at platform-level abstraction.
- **Audience is unboundable.** When audience specificity is material to the affected work and the founder cannot describe it, stop — do not invent one. A known single internal operator is sufficiently bounded for proportionate internal work.
- **No real wedge.** When differentiation is material and the wedge reduces to "easier UX" or "AI-powered" with no concrete delta, record the unresolved hypothesis in the applicable discovery owner and stop. Do not create `discovery.md` solely for an inapplicable comparison or paper over the absence.
- **Conflicting prior decisions.** If `decisions.md` contains a prior framing the founder now contradicts, supersede the prior decision with a new entry; do not silently rewrite history.
- **Discovery on a hot impulse.** If the founder is mid-frustration and discovery would be premature, name this and offer to schedule a follow-up. Do not paper over emotional state with structured intake.
- **Out-of-scope request.** If the user asks the skill to also write the thesis or scope, redirect to `idea-compressor` / `mvp-scope`.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; fall back to plain inline questioning. Profile and mode may be resolved from current instruction, accepted durable state, unambiguous context, or the caller; no orchestrator-only declaration is required.
- **Subagents.** A reviewer subagent may be used to draft a "five plausible audience-objection questions" list while the main agent runs the conversation. Fallback: do this inline.
- **Skill authoring.** Prefer `skill-creator` for edits; otherwise edit by hand.

No Conductor- or Spec-Kit-only assumptions. The artifacts produced live in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 1 fills:

- `project-system/examples/photographer-saas/founder-intent.md` — a synthetic Maya persona, illustrative founder constraints, and prospective success targets used to show the artifact shape; none is represented as a real person or observed result.
- `project-system/examples/photographer-saas/discovery.md` — synthetic self-observation, interviews, quotations, counts, dates, and public-post scan used as worked-example inputs; none is represented as conducted or independently verified research.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
