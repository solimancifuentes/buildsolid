---
name: buildsolid-orchestrator
description: On-demand BuildSolid router. Resolves the active project profile and mode, identifies the applicable lifecycle entry from accepted artifacts, delegates to focused skills, and maintains cross-stage continuity. Use for explicit routing or status requests, ambiguous entry, cross-stage coordination, missing cross-stage dependencies, material profile changes, continuity reconstruction, or substantive Stage 13 diagnosis.
---

# buildsolid-orchestrator

> A BuildSolid skill. The on-demand router for the BuildSolid workflow defined in `framework/docs/context-package.md` §6 through §8E. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11. Applies the central profile/mode resolution policy when it orchestrates.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Coordinate BuildSolid when routing is needed: resolve and state the active **project profile** and **mode**; identify the applicable lifecycle entry from accepted artifacts; delegate to the appropriate focused skill; and preserve material cross-stage continuity.

The project profile is one of **New Product Build**, **Existing Project Change**, or **Lightweight/Internal Build**. Profiles describe workflow depth and are separate from the four interaction modes. The orchestrator applies the **applicable lifecycle slice** and compatibility rules in `framework/docs/context-package.md` §5B; it does not require a fourteen-row ledger.

The skill does **not** itself author thesis, scope, journeys, architecture, intelligence-layer, spec, plan, tasks, deployment, or launch-checklist content. Those are the 13 sub-skills' jobs. The orchestrator routes; focused skills do focused work (`framework/docs/constitution.md` §5).

The orchestrator runs the canonical **routing workflow** in `framework/docs/context-package.md` §8E and applies the policies that workflow references — modes (§5), profiles and lifecycle contracts (§5A, §5B), artifact requirements and readiness (§8A, §8B), authority and memory states (§8C), and the readiness/gating policy (§8D). It **consumes** those sections rather than restating them, keeping the orchestrator scoped to coordination, routing, continuity, and escalation.

## 2. Trigger conditions

Invoke this skill when:

- the human explicitly asks for workflow routing, status, or the next applicable stage;
- entry is ambiguous or the work spans multiple stages;
- a focused skill reports a genuine missing cross-stage dependency or wrong-phase handoff;
- a material profile change may alter workflow depth;
- a fresh agent must reconstruct cross-stage continuity from accepted artifacts;
- **Existing Project Change** impact is unclear across stages;
- feedback may meet the substantive Stage 13 threshold; or
- Stage 9 reports drift, a missing requirement, or a completion handoff that needs cross-stage routing.

Focused skills are also valid direct entry points when their purpose matches, genuine prerequisites are current, profile and mode are safely resolved and stated, and no cross-stage ambiguity or founder gate exists. Existing orchestrator-first workflows remain valid; orchestration is not a mandatory preamble.

## 3. Inputs

Required:

- The list of files in the project's working directory (to detect which artifacts exist and which artifacts appear semantically ready under `framework/docs/context-package.md` §8B).
- The user's stated intent for the session (even one sentence).

Required artifacts when present:

- `founder-intent.md` — for any durable project profile or mode choice at intake.
- `decisions.md` — for prior durable profile, mode, phase, deferral, or conflict decisions.
- All canonical artifacts from the `framework/docs/context-package.md` §8 inventory that are present in the project.

Optional context:

- An existing chat history with the user, if one is preserved.
- A `.context/` notes file from a prior agent in a multi-agent / Conductor setup. The orchestrator reads it as working-context coordination scratch only — never as a substitute for the canonical artifacts (`framework/docs/constitution.md` §13; `framework/docs/context-package.md` §8C).

## 4. Outputs

The orchestrator's outputs are **routing decisions and small material continuity updates**, not large authoring:

- A **resolved project profile and mode**, inferred and stated when safe or asked when materially ambiguous. Update `founder-intent.md` §6 or `decisions.md` only for a durable project choice or material override, not transient session posture.
- A **phase identification** — which of the 14 phases the project is in right now.
- For **Existing Project Change**, a compact impact outcome: direction test, entry stage, affected artifacts or stages, required downstream gates, and material exclusions. Existing accepted `spec.md`, `plan.md`, or `tasks.md` may carry it; add a separate note or decision only when materially needed.
- For substantive **Stage 13 feedback**, an iteration outcome: affected accepted state, material-change test, diagnosis, accept/reject result, re-entry stage, affected artifacts, and proportionate validation. Use `known-issues.md` only for persistent issues and `decisions.md` only for meaningful judgment or tradeoff.
- For **Stage 9 implementation support**, a handoff state carried forward from `framework/docs/context-package.md` §8E: accepted `spec.md` / `plan.md` / `tasks.md` entry inputs, task `Status` values, any drift or blocker evidence, any routed task/spec/plan adjustments, and readiness for Stage 10.
- A **gating decision** at an actual prerequisite, acceptance, routing, authority, security, deployment, launch, or consequential boundary — **advance**, **defer**, **block**, or **route**.
- A **sub-skill invocation** — control handed to the appropriate sub-skill with the phase context and any user intent.
- A continuity update only when a fresh agent needs it to reconstruct material cross-stage state.

The orchestrator does **not** author focused-skill artifacts. It updates an existing accepted artifact only when needed for durable profile/mode state, a compact impact outcome, a meaningful decision or deferral, or a reconstructable Stage 9 handoff.

In multi-agent / Conductor setups, the orchestrator may write a brief coordination note to `.context/` (e.g., who owns which sub-skill in this workspace). That note is working-context scratch, not durable artifact (`framework/docs/constitution.md` §13; `framework/docs/context-package.md` §8C).

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only the orchestrator's deltas before it passes the resolved mode to focused skills.

- **Guided Mode.** State the resolved mode and profile, explain the current phase and routing choice in plain language, and ask only about material ambiguity or missing genuine prerequisites.
- **Founder Mode.** State the resolved mode and profile, pressure-test a material direction or scope ambiguity, then route without a generic questionnaire.
- **Expert Mode.** Infer and state mode/profile from accepted artifacts or current instruction, identify the entry stage, and route concisely.
- **Build Mode.** Use accepted `spec.md`, `plan.md`, and `tasks.md`; verify genuine build inputs; route or block only for drift, conflict, missing authority, or a real prerequisite.

The orchestrator never substitutes for a sub-skill's mode behavior. Once it delegates, the sub-skill's own §5 delta applies inside the shared central policy.

### Profile and mode resolution mechanics

Resolve both choices in this order:

1. explicit current human instruction;
2. an accepted durable project choice in `founder-intent.md` §6 or `decisions.md`;
3. unambiguous current context; or
4. a focused question only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output.

State any inference. Persist only a durable cross-session project choice or material override. A temporary session posture does not make an accepted durable choice stale and is not silently written to project artifacts. AI-native work is not a fourth profile; when AI is load-bearing, Stage 5 and AI-specific validation apply inside the selected profile.

## 6. Question policy

What the orchestrator **must** ask:

- A focused profile, mode, or entry-stage question when accepted state and current instruction leave a material ambiguity.
- The missing preference, intent, authority, safety context, or genuine prerequisite when the gap blocks correct routing.
- Confirmation before a destructive or otherwise high-impact action; the orchestrator itself performs none.

What the orchestrator **may assume**:

- For New Product Build, the phase corresponds to the first applicable artifact in lifecycle order that is missing or draft, unless the human states otherwise.
- A signed-off artifact is correct; do not re-run a sub-skill that would overwrite it without confirmation.
- A safely inferred session posture applies to the current routing decision but is not automatically durable project state.

**Stage progression.** Run the routing loop in `framework/docs/context-package.md` §8E only when an on-demand trigger exists, and apply **advance**, **defer**, **block**, or **route** at actual gates. Existing Project Change carries its compact five-field impact outcome rather than dual records or a full upstream N/A ledger. Stage 13 applies only to substantive post-acceptance learning; same-scope fixes, review remediation, maintenance, and routine retry remain ordinary Existing Project Change. Stage 9 begins from accepted `spec.md`, `plan.md`, and `tasks.md`, preserves the four task statuses, and routes only material drift or missing requirements. A valid `N/A - reason` or material exclusion is satisfied. No mode may lower accepted-input or founder gates.

How the orchestrator **confirms before destructive actions**:

- Re-running a focused skill that would overwrite accepted state requires explicit authority regardless of mode.
- A durable project profile or mode change is logged when it materially changes workflow depth or accepted behavior; transient session posture is not.
- Authority-sensitive proposed changes become accepted only through reviewed Markdown artifacts or decisions (`framework/docs/context-package.md` §8C).

Asking mechanism: use structured clarification tooling when available and useful; plain inline questioning is the agent-neutral fallback (`framework/docs/constitution.md` §9, §14).

## 7. Done criteria

A single orchestrator invocation has finished when:

- The active mode and profile are resolved and stated, with material ambiguity asked rather than guessed.
- The applicable entry stage and any actual gate are identified.
- The appropriate focused skill has been invoked, **or** the human has received the requested routing/status answer.
- Any material cross-stage continuity, durable choice, deferral, or founder gate is recorded in the proper accepted artifact.

A full BuildSolid project run is "done" when its applicable lifecycle slice and actual acceptance gates are satisfied and the human has accepted the outcome or explicitly stopped. The orchestrator does not grant acceptance; it reports artifact and gate state.

## 8. Failure modes

- **No artifacts exist.** Treat a new-product request as Phase 0 (Intake), infer and state a likely mode/profile, and ask only if ambiguity materially changes the route.
- **No durable project profile exists.** Infer and state New Product Build, Existing Project Change, or Lightweight/Internal Build from current instruction and accepted state; ask only when the choice is materially ambiguous.
- **Profile and mode are confused.** Separate them explicitly: profile describes the shape and depth of the work; mode describes agent behavior with the human. Every profile can run in any appropriate mode.
- **AI-native is proposed as the profile.** Do not accept it as a profile. Choose one of the three approved profiles and apply Intelligence Layer depth if AI is load-bearing.
- **Mode and current behavior differ.** Treat the current instruction as session posture when safe, state the inference, and ask only if the difference materially changes work. Persist only a durable project change.
- **Multiple plausible entry stages.** Ask a focused question only when accepted state and current instruction cannot resolve which choice materially changes the work.
- **Sub-skill returns "missing dependency."** Identify the upstream skill that produces the missing input and route to it. Record the handoff only when a fresh agent needs the material cross-stage state to reconstruct continuity.
- **Existing Project Change has unresolved impact.** Block before `task-breakdown`; make the five-field compact outcome clear in accepted artifacts. A separate decision or plan record is required only when materially needed.
- **Feedback does not meet the Stage 13 threshold.** Keep same-scope bugs, review remediation, maintenance, and routine retry in ordinary Existing Project Change. Use `known-issues.md` only for persistence and `decisions.md` only for meaningful judgment.
- **Stage 9 stalls.** Block or defer through §8D only after blocker evidence and task `Status` are recorded as required by the §8E implementation-support procedure.
- **Stage 9 drift appears.** Route to the artifact owner first; the accepted `spec.md`, `plan.md`, and/or `tasks.md` must be updated with a logged rationale before implementation continues.
- **Stage 9 reveals a missing requirement.** Reuse the §8E direction test: small in-scope gaps route to task adjustment after any needed spec/plan update; direction-changing gaps leave Stage 9 for the relevant earlier stage.
- **Sub-skill's verdict conflicts with the spec or constitution.** The constitution wins (`framework/docs/constitution.md` §16). Record the conflict in `decisions.md`; route to the appropriate skill to update the upstream artifact.
- **User asks the orchestrator to do a sub-skill's job directly.** Politely decline and route. The orchestrator is a router, not a workhorse.
- **`founder-intent.md` §6 is empty or names an invalid durable choice.** Resolve from current instruction or accepted state; ask on material ambiguity; write only a durable project choice.
- **A signed-off artifact needs revision.** Apply the §8E material-change test. Substantive accepted-state learning may enter Stage 13; same-scope correction remains ordinary change work. Update in place; do not version-copy (`framework/docs/constitution.md` §3 principle 9).

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior in the *contract*; it does have one Claude-Code-preferred mechanism with a documented agent-neutral fallback.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Material clarification.** Structured question tooling may present the three profiles or four modes when ambiguity matters. Agent-neutral fallback: one plain inline question. No question is required when a safe inference is available.
- **Subagents.** A subagent may be used to read the project's artifacts in parallel and produce a "current state" summary that the orchestrator uses to identify the phase quickly. Fallback: read the artifacts in the main agent's context.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.
- **Conductor coordination.** In a Conductor setup with multiple parallel agents, the orchestrator may use `.context/` for who-owns-what coordination. Fallback: a single agent in a single working tree owns the whole workflow (`framework/docs/constitution.md` §13).

The orchestrator must remain useful on any harness that supports markdown skills. No capability of BuildSolid requires Claude Code, Conductor, or Spec Kit (`framework/docs/constitution.md` §8, §13, §14). Subagents and Conductor here are **agent instances** used as an optional convenience, not separate live agents the workflow depends on; the skill/role/agent/agent-instance/workflow/policy model is defined in `framework/docs/context-package.md` §7A, and the single-agent Markdown baseline it states always holds — one agent reading these skills inline can run the whole workflow.

## 10. Reference example

See the synthetic freelance-photographer reference project's session structure:

- `project-system/examples/photographer-saas/founder-intent.md` §6 — the durable Founder intake choice in the example; this remains valid history and does not require every later session to persist its posture.
- `project-system/examples/photographer-saas/decisions.md` — historical mode and phase records that remain valid under the compatibility contract.
- The example walkthrough demonstrates routing through `task-breakdown` at Stage 8. Stage 9 is skill-less project-side implementation support; Stage 10 uses `qa-reviewer` and then `security-reviewer`, Stage 11 uses `deployment-manager`, and Stage 12 uses `launch-prep`. In this shipped example those later stages remain artifact-level only, as stated in `project-system/examples/photographer-saas/README.md` §1.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).

---

## Appendix — Routing reference

The canonical **stage-to-skill routing reference** — stage ownership, optional helpers, Stage 9 support, and substantive Stage 13 re-entry — lives in `framework/docs/context-package.md` §8E. The orchestrator consumes it only when an on-demand routing trigger exists. Which stages run follows the applicable lifecycle slice; a valid `N/A - reason` or material exclusion is satisfied. `starter-stack-advisor` remains a standalone optional helper.
