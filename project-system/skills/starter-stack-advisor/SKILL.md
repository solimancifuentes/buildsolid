---
name: starter-stack-advisor
description: Helper skill that proposes an opinionated minimal default stack for solo builders who want a default, not a debate. Invoke it directly or from technical-planner when accepted project constraints support a proposal. Not an independent workflow stage; it returns suggestions and rationale, never authors architecture.md on its own.
---

# starter-stack-advisor

> A BuildSolid helper skill. **Not an independent workflow stage.** Invoked directly or by `technical-planner` (Phase 6) when the user wants a default stack rather than an open architecture debate. It remains standalone, optional, and non-authoring under `framework/docs/context-package.md` §§7 and 8E. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Propose an **opinionated minimal default stack** for a solo-built MVP, with a one-line reason per choice and named fallbacks. The skill exists so a builder who says "just give me a sensible default" gets one, instead of being walked through every layer.

The skill **only proposes**. It returns the stack and its rationale to the caller (typically `technical-planner`); it never edits `architecture.md` or any other artifact directly. It is a helper, not an architect.

## 2. Trigger conditions

Invoke this skill when:

- A direct caller names `starter-stack-advisor`, or the requested outcome matches its proposal-only purpose, and accepted project constraints are available.
- `technical-planner` is in Phase 6 and the user has indicated they want a default stack rather than choosing components individually.
- A user explicitly asks for "a sensible default stack," "the gstack," "just pick something," or similar.
- A later-phase skill is blocked because no stack has been chosen and the user wants the helper's opinion as a starting point.

Direct invocation is valid only when accepted project constraints are sufficient for the proposal, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. An orchestrator preamble is not required.

Do **not** invoke when:

- The user has already named the stack (in `decisions.md`, `founder-intent.md` constraints, or directly in chat). Defer to the user's choice.
- The project has hard external constraints (regulatory, integration, parent-product) that the helper cannot reason about without those constraints surfaced; in that case, the caller should hand the constraints to `technical-planner` instead.

## 3. Inputs

Genuine required inputs from the caller, whether the user, `technical-planner`, or another coordinating skill:

- Accepted project scope and technical constraints — normally `mvp-scope.md` and `non-goals.md`, or equivalent accepted `spec.md`, `plan.md`, existing architecture context, or another owning artifact.
- The project's accepted `intelligence-layer.md` only when AI is load-bearing — to align the AI provider choice with the layer.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller/orchestrator. State any inference; ask only if ambiguity materially changes the proposal.

Optional context:

- `founder-intent.md` §5 (constraints) — to respect technologies the founder will or will not touch.
- `decisions.md` — to avoid proposing a stack that has already been considered and rejected.
- The founder's own preference between two equally-valid defaults (e.g., serverless vs single VM), if expressed.

The skill does **not** require a finished `architecture.md` to exist — it is invoked precisely to help draft one.

## 4. Outputs

The skill returns a **proposal**, not a file. The proposal contains:

- A short paragraph naming the proposed stack at the highest level (e.g., "single-page web app + small API + managed database + managed AI provider").
- A bullet list, layer by layer, with: layer, the proposed default, the one-line reason, and a named fallback. Layers typically include: client, API/server, data store, background work (if any), auth, hosting/runtime, AI provider, observability, secrets store.
- A short "why this default fits this project" paragraph that grounds each choice in the accepted scope and technical constraints and, when AI is load-bearing, `intelligence-layer.md`.
- A short "what would change if…" paragraph naming the most likely conditions that would push the stack off-default (e.g., "if the project must run in a customer's VPC, swap hosting to <X>").

When the caller is `technical-planner`, it may adapt the proposal into `architecture.md` per `project-system/templates/architecture.md` §3 / §5 / §6 and record meaningful architectural choices in `decisions.md` (`project-system/templates/architecture.md` §6 rule). A direct human caller receives the same proposal for consideration.

The skill itself does not write to disk.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Return the default stack proposal with useful alternatives per layer and explain why each default is the starting point; ask only about constraints that materially change the proposal.
- **Founder Mode.** Return a terse default stack proposal; include only tradeoffs that affect MVP scope or founder constraints.
- **Expert Mode.** Return one default per layer with one-line reasons for the caller to accept, revise, or reject.
- **Build Mode.** Return only the missing or unclear layers named by the caller; do not re-propose layers already accepted in `architecture.md`.

In every mode, the skill marks the proposal as "default — verify against project constraints" so the caller does not adopt it without check.

## 6. Question policy

What the skill **must** resolve with the caller:

- Whether applicable technical non-goals have been accounted for when accepted inputs leave that materially ambiguous.
- Any conflict between a provider named in `intelligence-layer.md` and the helper's default; the accepted layer wins unless a meaningful change is separately accepted.

What the skill **may assume**:

- The caller has already gathered the inputs in §3.
- A solo builder defaults to managed services over self-hosted infrastructure, single-region over multi-region, and simple over distributed.

Resolve and state profile and mode from the sources in §3. Ask about either only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output; do not persist ordinary session posture.

How the skill **confirms before destructive actions**:

- The skill makes no destructive actions; it produces a proposal. The caller is responsible for any artifact edits and any required confirmation.

When the user invokes the skill directly, ask that user only about material ambiguity or a missing genuine prerequisite. When another skill invokes it, return any unanswered material question to that caller rather than bypassing the caller's authority boundary.

## 7. Done criteria

- The skill has returned a proposal with: stack-shape paragraph, layer-by-layer bullets (with default, reason, fallback for each), grounding paragraph, "what would change if" paragraph.
- Each layer in the proposal has a named fallback.
- The proposal aligns with `intelligence-layer.md` when AI is load-bearing and respects the applicable accepted technical and AI non-goals or constraints.
- The proposal carries the "default — verify against project constraints" marker.
- The proposal is returned to the direct caller. Return to the orchestrator only when cross-stage routing or continuity is needed.

The user's signal that the helper has finished is receipt of the complete proposal; if `technical-planner` invoked it, that skill owns any later `architecture.md` update.

## 8. Failure modes

- **Caller did not provide required inputs.** Return a refusal naming the missing accepted scope or technical constraints, and name `intelligence-layer.md` only when AI is load-bearing. Do not invent scope or AI capabilities.
- **Project constraints rule out every default at a layer.** Return that layer marked "no default — caller must choose"; do not invent a default that violates a non-goal.
- **Conflict with `decisions.md`.** If a previously rejected stack matches the helper's default, return the proposal with a flag pointing the caller at the prior decision. Do not silently re-propose what was rejected.
- **Asked to write `architecture.md`.** Refuse. The helper does not author architecture; route the request back to `technical-planner`.
- **Asked to choose between stacks the caller has narrowed to.** If another skill invoked this helper and the choice depends on user preference, return the proposal labeled "tie — caller must ask user." If the user invoked it directly, ask only when the preference is materially outcome-changing; otherwise state the default and its tradeoff.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Subagents.** A reviewer subagent may be used to sanity-check each layer's default against the project's non-goals in parallel. Fallback: do the check inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.

The proposed defaults themselves are stack-agnostic in spirit — the skill's role is to *encode the rule for choosing a minimal stack*, not to commit BuildSolid to any specific provider. Concrete defaults are the helper's opinion at the time; they are not part of BuildSolid's contract. No Conductor- or Spec-Kit-only assumptions appear in this skill.

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 6 fill:

- `project-system/examples/photographer-saas/architecture.md` — names a provider-neutral four-component shape plus stock data-store and email dependencies, while leaving the specific AI provider and concrete language/framework choices unresolved. Its header identifies `starter-stack-advisor` as an optional proposal baseline consumed by `technical-planner`; the artifact records planned architecture, not a deployed stack or separate proposal-to-final delta.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
