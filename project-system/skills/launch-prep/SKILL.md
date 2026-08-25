---
name: launch-prep
description: Drive positioning, landing-page guidance, first-user planning, metrics, and readiness for an actual launch. Produces or updates launch-checklist.md — the binary list of applicable conditions that must be true before the project ships to its first users. Use this skill in Stage 12 when the relevant accepted launch inputs exist.
---

# launch-prep

> A BuildSolid skill. Drives Phase 12 (Launch Prep) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Drive the applicable work that makes an actual launch or readiness event answerable: product readiness, communications or positioning when relevant, first-user outreach when relevant, and the metrics or commitments the event will be judged by. Produces `launch-checklist.md` — the binary list of conditions that must be true for that event without inventing inapplicable launch content.

The skill does **not** build the landing page, run marketing campaigns, or deploy (that is `deployment-manager`'s planning artifact + the project's own implementation). It produces the artifact that makes "are we ready?" answerable.

## 2. Trigger conditions

Invoke this skill when:

- A user or direct caller is preparing an actual launch or needs a launch-readiness decision, and the genuine accepted inputs for that launch are current.
- The orchestrator routes an applicable project to Phase 12 with its genuine dependencies satisfied.
- A user asks to "draft the launch checklist," "plan the launch," "list first users," "write the positioning," or "set the activation metric."
- A pre-launch dry run reveals gaps and the checklist must be re-tightened.
- An accepted material change affects the goal, audience, launch treatment, or readiness criteria.

Direct invocation is valid when actual launch or readiness work is the focused purpose, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. Do **not** invoke merely to mark Launch Prep inapplicable. If an applicable launch depends on unresolved deployment or major product commitments, block and route to the owning stage first.

## 3. Inputs

Genuine prerequisites for the current launch scope:

- Accepted product or release commitments — normally `spec.md` — for the launch scope and acceptance criteria.
- The applicable accepted metric owner only when §7 metrics are part of the current launch or readiness scope — normally `mvp-scope.md` §§4–5, but an accepted `spec.md` or another owning artifact may define equivalent success / failure criteria for a compact slice.
- `intelligence-layer.md` only when AI is load-bearing or an AI commitment affects launch readiness.
- `deployment.md` only when the launch depends on deployment, rollout, rollback, observability, or operations commitments.

Optional context:

- `user-journeys.md` and `design.md` — for the journeys and screens the launch must serve.
- `architecture.md` §7 — for non-functional constraints the launch must validate.
- `decisions.md` — for prior launch-related decisions.
- `known-issues.md` — for items that must be either fixed or accepted before launch.
- The current security-review result and its task, review, pull-request, or accepted-decision provenance when security is relevant.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller / orchestrator. State any inference and ask only when ambiguity would materially change the work.

User context the skill expects:

- The first-user list or outreach channel only when first-user acquisition or communication is in scope.
- Any launch window the founder is targeting when timing materially affects readiness.
- The activation and failure metrics only when §7 metrics are part of the current event.

## 4. Outputs

Files this skill produces or updates:

- When Stage 12 applies, `launch-checklist.md` — filled per `project-system/templates/launch-checklist.md`: §1 Product, §2 Intelligence layer, §3 Infrastructure and deployment, §4 Security, §5 Privacy and compliance, §6 Communications, §7 Metrics, §8 Operations and on-call, §9 Decisions and open questions. Include only applicable checks; optional sections (Marketing assets, Legal and contracts, Post-launch monitoring rota, Rollback decision tree) appear only when materially relevant.
- When no actual launch or readiness outcome is in scope, create no `launch-checklist.md` solely to record N/A. Record a compact material exclusion in an existing owning artifact only when the omission would otherwise be surprising, ambiguous, or consequential.

Conditional side outputs, captured in existing artifacts only when the current launch scope needs them:

- A **positioning statement**, when communications or positioning are affected — capture the smallest useful statement in `launch-checklist.md` §6 (Communications). A one-paragraph "X for Y that Z" plus 3–5 supporting bullets is a typical New Product default, not a minimum for Existing Project Change or Lightweight/Internal Build. Append a `decisions.md` entry only when accepting the positioning resolves a meaningful judgment or tradeoff that needs durable rationale, then cross-reference it from §6.
- A **first-user list / channel plan**, when first-user acquisition or outreach is affected — capture the smallest useful list or channel plus the applicable message in `launch-checklist.md` §6. A list of 5–25 users is a typical New Product default, not a minimum for an existing-change or internal readiness event. Append a `decisions.md` entry only when the plan resolves a meaningful accepted judgment or tradeoff that needs durable rationale.

The skill does **not** introduce a new canonical artifact (`framework/docs/constitution.md` §10) — no `positioning.md`, no `first-users.md`. Any applicable side output lives in `launch-checklist.md` §6, with `decisions.md` used only for a meaningful accepted judgment or tradeoff. A readiness-only or metrics-only event does not create positioning or first-user content merely to fill §6.

Shape rules:

- Every checklist item is **binary** — "yes, this is true" or it is not done (`project-system/templates/launch-checklist.md` rule).
- When §7 metrics apply, activation and failure metrics trace to the applicable accepted metric owner, normally `mvp-scope.md` §§4–5. The skill does not invent metrics or require them for a communication-only or other event where §7 is materially inapplicable.
- When AI is load-bearing, the intelligence-layer items in §2 reference `intelligence-layer.md` §5, §6, and §7 by section.
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Fill the applicable `launch-checklist.md` areas one by one, tying checklist items back to their owning artifacts and surfacing commonly skipped launch checks.
- **Founder Mode.** Pressure-test the applicable support, outreach, rollback, metrics, and timing assumptions before treating launch prep as ready.
- **Expert Mode.** Draft the checklist from the relevant accepted inputs; surface only applicable founder-commitment items such as outreach, support, metrics, or timing.
- **Build Mode.** Use when implementation is blocked by a specific launch-readiness decision; answer or record that decision without replanning launch.

In every mode, the skill writes or updates `launch-checklist.md` only when Stage 12 applies.

## 6. Question policy

What the skill **must resolve**, asking only when the answer is not safely inferable and would materially change launch readiness:

- The first-user list or channel only when first-user acquisition or outreach is in scope.
- The launch window only when timing materially affects the current event (or "no fixed window — when checklist is green" when a launch window applies but is open-ended).
- The activation and failure metrics only when §7 is applicable, traced to the applicable accepted metric owner.
- For any unmet §2 / §3 / §5 hard gate, fix now or remain blocked. Ask about recorded mitigation only for a residual item the accepted project contract explicitly classifies as non-gating.
- Human authority before changing a signed-off `launch-checklist.md`.

What the skill **may assume**:

- Every applicable hard gate in the checklist must be defensibly true at launch. An explicit accepted decision may address only a residual item the governing project contract permits to remain non-gating; it cannot make an untrue hard gate pass.
- Applicable accepted non-goals are binding for launch even when they live outside `non-goals.md` (e.g., "no payments at launch" means no payments item in §1).
- When AI is load-bearing, its complete eval must pass `intelligence-layer.md` §5's threshold. Below-threshold AI remains blocked unless the accepted project contract expressly defines that capability and eval as non-gating; the photographer reference example does not.
- The resolved profile and mode when they can be inferred unambiguously from current instruction, accepted durable state, or caller context; state the inference rather than asking again.

How the skill **confirms before destructive actions**:

- The skill makes no live changes. Never mark an untrue checklist item passed. A logged exception records treatment of a contract-permitted non-gating residual; it does not change the item's truth or waive a hard gate.
- Declaring "ready to launch" is the user's call; the skill confirms the checklist state and refuses to proxy the decision.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- When Stage 12 applies, `launch-checklist.md` is filled with the applicable checks in §§1–9, every included item binary, no placeholders.
- When §7 applies, activation and failure metrics trace to the applicable accepted metric owner, normally `mvp-scope.md` §§4–5. When metrics are inapplicable to the current communication or readiness event, they are not a completion gate.
- When AI is load-bearing, intelligence-layer items in §2 reference `intelligence-layer.md` by section.
- When deployment applies, deployment items in §3 reference `deployment.md` by section.
- When §4 security checks apply, they are aligned with the latest `security-reviewer` result and its task, review, pull-request, or accepted-decision provenance.
- When §5 privacy checks apply, they are concrete; "we'll write a privacy policy later" is not acceptable as a passing condition for an applicable privacy commitment.
- Each applicable positioning or first-user side output is recorded in `launch-checklist.md` §6. If one or both are inapplicable, do not invent content to fill the section; retain a specific `N/A - reason` only when that in-file omission needs durable explanation. Add and cross-reference `decisions.md` only for a meaningful accepted judgment or tradeoff; do not require duplicate records.
- Cross-references resolve.
- Return the Phase 12 result, unresolved gates, and readiness state to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed. The project may launch only on the human's authority when every applicable hard gate is green. An accepted project contract may define which non-gating residual items permit explicit human risk acceptance; a project-specific hard gate cannot be waived by recording a mitigation.

## 8. Failure modes

- **Genuine input missing.** Stop and name the missing prerequisite. Route to its owning stage or to the orchestrator only when cross-stage coordination is needed.
- **Applicable activation or failure metric has no accepted owner.** When §7 applies, refuse to fill it until an applicable accepted artifact defines concrete success and failure criteria. Route to `mvp-scope` when Stage 3 owns the missing definition; otherwise route to the current spec or release-commitment owner. If §7 is inapplicable, this is not a blocker.
- **AI-layer evals not run / below threshold.** Mark §2 items unmet. Do not let the launch ship on "we'll improve the prompt later"; route back to Build Mode against `intelligence-layer.md`.
- **Open Critical / High security findings.** Mark §4 items unmet and remediate through Build Mode. Explicit risk acceptance is available only if the accepted project contract classifies the item as non-gating; a project-specific no-Critical/High launch gate cannot be passed by a logged mitigation. The skill does not silently downgrade severity.
- **No support channel named when support is applicable.** If the current event includes user-facing support or §6 requires a support channel, refuse until the channel is named. A communication-only, metrics-only, or internal readiness event with no applicable support commitment is not blocked by this check.
- **Compliance commitments not enforced.** Per `project-system/templates/launch-checklist.md` §5: a compliance promise without a check is not met.
- **Launch Prep is inapplicable.** Create no empty launch checklist. Record a material exclusion only when its omission needs durable explanation, then return the satisfied state to the caller.
- **Out-of-scope request.** If the user asks the skill to actually build the landing page, run the launch tweet, or send first-user emails, redirect — those are project-side execution. The skill's job ends at the checklist and any applicable planning side outputs.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** A reviewer subagent may be used to walk the §2 (intelligence-layer) checklist while the main agent walks §3 (infrastructure) in parallel. Fallback: walk them sequentially.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.

No Conductor- or Spec-Kit-only assumptions. The artifact lives in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's artifact-level Stage 12 fill (`project-system/examples/photographer-saas/README.md` §1):

- `project-system/examples/photographer-saas/launch-checklist.md` — an unchecked would-launch checklist whose hard gates cover the unresolved provider, complete future rights-cleared eval, retention/restore enforcement, security, qualified legal review, and real-data admission. A future properly consented five-photographer cohort and all stated timing/adoption thresholds are prospective; the example records no participants or result.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
