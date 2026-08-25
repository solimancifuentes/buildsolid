---
name: intelligence-layer-architect
description: Design load-bearing or materially changed AI capabilities as a layer — capabilities, prompts, models, evals, fallbacks, costs, and safety — not as a sprinkle of features. Use this skill in Stage 5 when the relevant accepted scope and experience inputs exist, to produce or update intelligence-layer.md.
---

# intelligence-layer-architect

> A BuildSolid skill. Drives Phase 5 (Intelligence Layer) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Encodes BuildSolid's core principle that AI is an intelligence layer, not a feature (`framework/docs/constitution.md` §3 principle 4). Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Produce `intelligence-layer.md` — the single source of truth for what the project's AI does, how it knows when it is wrong, and what happens when it is. The skill treats the AI as a designed layer with capabilities, prompts / policies, model choice, evals, fallbacks, cost, safety, memory, context handling, and human override. Each capability must address all nine dimensions defined in §4.

The skill does **not** design product UX (that is `ux-minimalist`), pick the rest of the stack (that is `technical-planner`), or implement prompts in code. It defines the layer.

## 2. Trigger conditions

Invoke this skill when:

- A user or direct caller needs to design a load-bearing AI layer or materially change an accepted AI capability, and the genuine accepted inputs for that scope are current.
- The orchestrator routes an applicable project to Phase 5 with its genuine dependencies satisfied.
- A user asks to "design the AI layer," "list the AI capabilities," "write the prompts," "set evals," or "name the safety boundaries."
- A later-phase skill (`technical-planner`, `qa-reviewer`, `security-reviewer`, `deployment-manager`) reports it cannot ground a decision because the AI layer is unclear.
- An accepted change adds, removes, or materially changes a load-bearing AI capability.

Direct invocation is valid when this focused purpose matches, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. Do **not** invoke merely to record that a project has no AI layer, or when AI is neither load-bearing nor changed. When capability scope is materially unclear, or a user-facing AI surface lacks an accepted journey, block and route to `mvp-scope` or `ux-minimalist` as appropriate.

## 3. Inputs

Genuine prerequisites for the current AI scope:

- Accepted scope — normally `mvp-scope.md` — naming the load-bearing AI capabilities and AI-related cuts.
- `user-journeys.md` or another accepted experience contract for each user-facing AI surface.
- `product-thesis.md` when AI is part of the wedge or the change could affect product direction.

Optional context:

- `non-goals.md` §5 — AI non-goals; treat as binding cuts.
- `design.md` — for AI-presentation guidance (Optional E in the design template).
- `decisions.md` — for prior model/prompt/eval decisions and supersedes.
- `architecture.md` if it exists yet — for the boundary the AI layer must respect.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller / orchestrator. State any inference and ask only when ambiguity would materially change the work.

User context the skill expects:

- The cost ceiling the founder will tolerate per active user, even rough.
- Any safety boundaries the founder wants stated as hard "no"s.

## 4. Outputs

Files this skill produces or updates:

- When Stage 5 applies, `intelligence-layer.md` — filled per `project-system/templates/intelligence-layer.md`: §1 role of the layer, §2 capabilities (each with what/why/inputs/outputs/UX/prompt/model/evals/fallbacks/cost/safety), §3 cross-capability concerns, §4 data flow into and out of models, §5 eval strategy, §6 cost model, §7 safety boundaries, §8 iteration loop. Optional sections only when they materially clarify.
- When AI is not load-bearing and no accepted AI capability is being changed, create no `intelligence-layer.md` solely to record N/A. Record a compact material exclusion in an existing owning artifact only when the omission would otherwise be surprising, ambiguous, or consequential.

Shape rules:

- Typically **1–3 capabilities for an MVP**. More than 3 → push back on `mvp-scope.md` (`project-system/templates/intelligence-layer.md` §2 rule).
- Every capability must address the six template dimensions — prompts/policies, model choice, evals, fallbacks, cost, safety — **and** three further dimensions the skill enforces even when the template does not enumerate them: **memory** (what state the capability carries across calls or sessions, and where that state lives), **context handling** (how inputs are assembled — context-window budget, retrieval / RAG strategy if any, truncation rules), and **human override** (how a user or operator inspects, corrects, rejects, disables, or otherwise controls the capability's output). For a user-facing capability, name the screen in `design.md` or step in `user-journeys.md` that carries the override. For a background or internal capability, name the applicable operator or control boundary without requiring a dummy UX artifact. Memory and context handling fit under "Inputs" / "Prompt / policy" / "Data flow" (`project-system/templates/intelligence-layer.md` §2 / §4); human override fits under "Where it surfaces in the UX" / "Safety considerations" (§2 / §7) or the equivalent operator-control description. The skill does not introduce a new artifact for these dimensions; it ensures they are addressed in `intelligence-layer.md` as written.
- A capability missing any of the nine dimensions above is a draft, not a capability.
- Prompts longer than a paragraph live in a separate file under the project (e.g., `prompts/<capability>.md`), referenced from this artifact.
- The `Eval strategy` section names a golden set, a cadence, and an owner. "We'll add evals later" is not an eval strategy.
- Safety boundaries are stated as rules and the check that enforces them (`project-system/templates/intelligence-layer.md` §7 rule).
- Edited in place; no parallel versions.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Build each AI capability through the required dimensions, with extra attention to evals and fallbacks before `intelligence-layer.md` is accepted.
- **Founder Mode.** Pressure-test capability necessity, wrong-answer impact, measurement, cost growth, safety boundaries, and human override; reject generic safety claims.
- **Expert Mode.** Draft the layer from the relevant accepted scope, experience, and decision inputs; surface only choices that materially change cost, safety, model selection, or fallback design.
- **Build Mode.** Use when implementation is blocked by a missing capability, prompt boundary, eval, or fallback; resolve the blocked decision without redesigning the layer.

In every mode, the skill writes or updates `intelligence-layer.md` only when Stage 5 applies and ensures every capability is fully specified.

## 6. Question policy

What the skill **must resolve**, asking only when the answer is not safely inferable and would materially change the layer:

- The founder's per-active-user cost ceiling for the AI layer.
- For each capability, "how do you know it's working?" — the answer becomes the eval strategy.
- For each capability, "what happens when the model is unavailable, slow, or returns garbage?" — the answer becomes the fallback.
- The hard "no"s the AI must respect (e.g., "no medical advice", "never expose one client's selections to another").
- Human authority before changing an existing, signed-off `intelligence-layer.md`.

What the skill **may assume**:

- The minimalism rule (1–3 capabilities for an MVP).
- The non-goals in `non-goals.md` §5 are binding.
- The resolved profile and mode when they can be inferred unambiguously from current instruction, accepted durable state, or caller context; state the inference rather than asking again.
- Any `design.md` Optional E AI-presentation guidance is authoritative for how the layer surfaces in the UX.

How the skill **confirms before destructive actions**:

- Removing or replacing a previously accepted capability requires a logged decision in `decisions.md`.
- Changing a model, prompt, or eval threshold materially is logged per `project-system/templates/intelligence-layer.md` §8 (iteration loop).

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- When Stage 5 applies, `intelligence-layer.md` is filled with §§1–8, no placeholders, no leftover guidance.
- §2 contains 1–3 capabilities, each with all nine dimensions specified.
- §5 names a golden set, a cadence, and an owner.
- §6 names the cost ceiling and what happens above it.
- §7 lists at least 2 safety boundaries, each with the check that enforces it.
- Cross-references to applicable or present journey, architecture, design, and decision artifacts resolve; do not require an optional or later artifact solely to satisfy this check.
- For each user-facing capability, its UX surface in §2 matches the applicable accepted experience contract, normally a screen or step in `user-journeys.md` / `design.md`. Background or internal capabilities do not require a dummy UX artifact.
- Return the Phase 5 result, unresolved gates, and readiness state to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed.

## 8. Failure modes

- **More than 3 capabilities.** Refuse to finalize. Hand back to `mvp-scope` to defer capabilities to a later version, or have the founder accept the deviation in `decisions.md`.
- **Capability missing an eval.** Refuse to mark the capability complete. Eval-less capabilities are how AI silently degrades.
- **Capability missing a fallback.** Same. The skill explicitly asks "what does the user see when this fails?"
- **Cost ceiling unset.** Refuse to finalize §6. The skill asks for a number, even rough; "we'll see" is not a ceiling.
- **Safety boundary without a check.** Reject the entry. A rule with no enforcement is decorative.
- **AI surfacing in `user-journeys.md` but not specified here.** Hand back to `ux-minimalist` to remove the AI surface, or specify the capability that drives it.
- **Conflict with `non-goals.md` §5.** A proposed capability that violates an AI non-goal is rejected. Either revise the non-goal (with logged decision) or drop the capability.
- **AI is not load-bearing and no capability changed.** Do not create an empty N/A-only intelligence-layer artifact. Record a material exclusion only when its omission needs durable explanation, then return the satisfied state to the caller.
- **Out-of-scope request.** If the user asks the skill to write the actual prompt-tuning code, redirect — the skill describes the capability and policy; implementation lives in code (downstream of `task-breakdown`) once specs are in place.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** A reviewer subagent may be used to draft "five plausible failure modes per capability" while the main agent fills the layer. Fallback: do it inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.
- **Model choice.** The skill does not assume any specific model family or provider. The project records its choice in `intelligence-layer.md` §2 / §3 with a reason; the skill is portable across providers.

No Conductor- or Spec-Kit-only assumptions. The artifact lives in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 5 fill:

- `project-system/examples/photographer-saas/intelligence-layer.md` — one image-suggestion capability with a structured policy, an unresolved provider gate, a future rights-cleared 300-frame eval set, prospective cost ceilings, manual fallback, minimized provider inputs, and image-mediated prompt injection treated as possible but mitigated.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
