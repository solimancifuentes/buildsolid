---
name: deployment-manager
description: Plan environments, secrets handling, rollout, rollback, observability, and on-call basics for a downstream BuildSolid project. Produces or updates deployment.md as a planning artifact only — BuildSolid does not automate deployment. Use this skill when Stage 11 deployment planning applies and its genuine accepted inputs are current.
---

# deployment-manager

> A BuildSolid skill. Drives Phase 11 (Deployment) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.
>
> **Scope guardrail.** This skill produces **planning artifacts only**. It does not run deploys, manage cloud infrastructure, or generate deployment automation — those are explicit non-goals (`framework/docs/constitution.md` §15). The skill stops at `deployment.md`.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Produce or update `deployment.md` for a downstream BuildSolid project — environments, secrets handling, rollout / rollback, observability, on-call basics, backups, cost / capacity, compliance commitments. The skill is the BuildSolid-side designer of "how this project ships and runs," recording it in markdown so any agent or operator can read it later.

The skill **does not**: run deploys, generate Terraform / Pulumi / Ansible / Helm / GitHub-Actions files, write CI/CD pipelines, or take any action against a cloud provider. Those would violate `framework/docs/constitution.md` §15. If the project chooses to add deployment automation, the *project's* `decisions.md` records that decision and the project's own implementation tasks own it — the skill's role ends at the planning artifact.

## 2. Trigger conditions

Invoke this skill when:

- A user or direct caller needs Stage 11 deployment planning and the current accepted inputs for the affected deployment surface exist.
- The orchestrator routes an applicable project to Phase 11 with its genuine dependencies satisfied.
- A user asks to "plan the deploy," "draft deployment.md," "set the rollout strategy," "decide on environments," or "name the secrets store."
- A later-phase skill (`launch-prep`) reports it cannot ground a launch checklist because the deployment plan is missing.
- An accepted change affects how the project ships or runs (for example, adding a managed AI provider, switching regions, or adopting a queue).

Direct invocation is valid when deployment planning is the focused purpose, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. Do **not** invoke merely to mark Deployment inapplicable. When the current deployment decision genuinely depends on missing architecture, route to `technical-planner`; do not require `architecture.md` for a deployment question that does not depend on it.

## 3. Inputs

Genuine prerequisites for the current deployment scope:

- Accepted product or release commitments — normally `spec.md` — for the auth, data-handling, availability, or other promises the deployment must respect.
- `architecture.md` when components, dependencies, data boundaries, or non-functional constraints materially shape the deployment decision.
- `intelligence-layer.md` only when AI is load-bearing or its cost, data flow, provider, fallback, or safety commitments affect deployment.

Optional context:

- `non-goals.md` — for technical / business-model non-goals that constrain deployment choices.
- `decisions.md` — for prior deployment decisions and supersedes.
- `founder-intent.md` §5 — for constraints (time, money, energy) that shape rollout simplicity.
- An existing `deployment.md` — if iterating, not greenfielding.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller / orchestrator. State any inference and ask only when ambiguity would materially change the work.

User context the skill expects:

- The environments the project ships through (or "single environment, names and reasons").
- The secret store the project uses (a manager, env vars, a hosted vault) — never asks for the secrets themselves.
- Who is on-call and what severity definitions apply.

## 4. Outputs

Files this skill produces or updates:

- When Stage 11 applies, `deployment.md` — filled per `project-system/templates/deployment.md`: §1 Environments, §2 Secrets and credentials (names and storage locations only — **never the secrets themselves**), §3 Rollout strategy, §4 Rollback strategy (including data implications), §5 Observability, §6 On-call and incident response, §7 Backups and recovery, §8 Cost and capacity, §9 Compliance and data handling. Optional sections only when materially relevant.
- When Stage 11 is inapplicable, create no `deployment.md` solely to record N/A. Record a compact material exclusion in an existing owning artifact only when the omission would otherwise be surprising, ambiguous, or consequential.

Shape rules:

- **Never store secrets in `deployment.md` or anywhere in the repository.** §2 names the secrets and points at where they actually live (`project-system/templates/deployment.md` §2 rule).
- The rollback strategy in §4 names the maximum acceptable rollback time and any data that would be lost. A rollback strategy that pretends data is reversible when it is not is rejected.
- The cost section §8 cross-references applicable architecture commitments and, when AI is load-bearing, `intelligence-layer.md` §6 for AI-layer cost.
- For compliance commitments in §9, every commitment names the check that enforces it (`project-system/templates/deployment.md` §9 rule).
- Solo-founder defaults are valid (e.g., "founder is the on-call; severity-1 wakes them up; otherwise once-daily dashboard check"). They must be stated, not implied.
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Build `deployment.md` section by section, explaining deployment decisions that are often skipped at MVP scale: environments, secrets, rollback, monitoring, and rollout ownership.
- **Founder Mode.** Pressure-test rollout failure, operational ownership, and launch-readiness assumptions before accepting the deployment plan.
- **Expert Mode.** Draft `deployment.md` from the relevant accepted inputs; surface only deployment choices that materially change cost, latency, observability, or rollback safety.
- **Build Mode.** Use when implementation is blocked by a specific deployment decision; answer or record that decision without redrafting the whole deployment plan.

In every mode, the skill writes or updates `deployment.md` only when Stage 11 applies.

## 6. Question policy

What the skill **must resolve**, asking only when the answer is not safely inferable and would materially change the plan:

- The environments the project ships through if not declared.
- The secret store, if not declared (the *store*, not the secrets).
- The on-call setup; "the founder gets paged for severity-1, otherwise watches dashboards once a day" is a valid answer for a solo founder MVP, but must be explicit.
- For each compliance commitment, "what check enforces this?"
- Human authority before changing a signed-off `deployment.md`.

What the skill **may assume**:

- Solo-founder defaults: managed services preferred over self-hosted, single-region preferred over multi-region, simpler-rollout preferred over canary.
- When AI is load-bearing, its accepted cost ceiling from `intelligence-layer.md` §6 is binding for the deployment cost ceiling.
- Non-goals in `non-goals.md` are binding (e.g., "no multi-region" → no multi-region rollout strategy).
- The resolved profile and mode when they can be inferred unambiguously from current instruction, accepted durable state, or caller context; state the inference rather than asking again.

How the skill **confirms before destructive actions**:

- The skill makes no live changes. Acceptance of risky rollback strategies (e.g., irreversible migrations) is logged in `decisions.md`.
- Adopting a previously rejected deployment pattern requires superseding the prior decision.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

## 7. Done criteria

- When Stage 11 applies, `deployment.md` is filled with §§1–9, no placeholders, no leftover guidance, no secrets.
- §3 names the typical lead time and who triggers the rollout.
- §4 names the maximum acceptable rollback time and any data implications.
- §5 lists the signals the project watches and where they are read.
- §6 names the on-call setup and the severity definitions.
- §8 reconciles with the applicable accepted architecture and, when AI is load-bearing, intelligence-layer cost commitments.
- §9 commitments each have a named check.
- Cross-references resolve.
- Return the Phase 11 result, unresolved gates, and readiness state to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed.

## 8. Failure modes

- **Required architecture missing.** If the current deployment decision materially depends on architecture, stop and route to `technical-planner`; otherwise continue from the accepted inputs that actually govern the decision.
- **Required AI-layer commitment missing.** When AI is load-bearing and deployment depends on its cost, data flow, provider, fallback, or safety treatment, stop and route to `intelligence-layer-architect`; do not require an intelligence-layer artifact for non-AI deployment work.
- **Deployment is inapplicable.** Create no empty deployment artifact. Record a material exclusion only when its omission needs durable explanation, then return the satisfied state to the caller.
- **User wants to commit secrets to the repo.** Refuse. Hard line. Walk the user through naming and storing the secret elsewhere.
- **Rollback strategy claims data reversibility that is not real.** Reject. Force an honest restatement (e.g., "rollback restores the application binary; data migrations are forward-only and tested in staging").
- **Compliance commitment without a check.** Reject. Aspirational compliance is not compliance.
- **Out-of-scope request.** If the user asks the skill to write Terraform / Helm / a CI pipeline / a deploy script, refuse and explain why (per the Scope guardrail above and `framework/docs/constitution.md` §15). Offer to record their decision to add automation in *the project's* `decisions.md`; the project's own implementation tasks then own the work.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** A reviewer subagent may be used to check that no secret string accidentally lands in §2 in parallel with drafting. Fallback: do the check inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.

The skill itself is cloud / platform / framework agnostic. The project records concrete platform choices in `decisions.md`; the skill simply asks for them.

No Conductor- or Spec-Kit-only assumptions. The artifact lives in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's Stage 11 fill, which is artifact-level only and creates no real infrastructure (`project-system/examples/photographer-saas/README.md` §1):

- `project-system/examples/photographer-saas/deployment.md` — planned `dev`, `staging`, and `production` shapes; prospective secret, rollout, rollback, observability, on-call, restore-safe retention, and cost/capacity treatment. No environment, deploy, recovery test, provider integration, or operating result exists in the example.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
