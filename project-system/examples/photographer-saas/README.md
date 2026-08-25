# Photographer SaaS — BuildSolid reference example

> The single worked reference example shipped with BuildSolid. It walks the freelance-photographer SaaS scenario from `framework/docs/context-package.md` §9 through every BuildSolid phase using only the shipped Markdown skills and templates — no real code, no live deployment.

> **Synthetic-scenario notice.** The scenario and its entire research corpus are illustrative fiction. Maya, other photographers, interviews, quotations, measurements, dates, forum/survey references, permissions, source galleries, and observed results are not real people, conducted research, or completed work.

This example exists to test that the BuildSolid workflow is walkable end-to-end on a realistic scenario using only the shipped artifacts and skills. Framework governs; this example is a compatibility fixture that must conform to it, not authority that redefines it.

The product the example describes is a **minimalist SaaS for freelance photographers** that helps a solo photographer:

1. Create a private gallery for a shoot.
2. Send a delivery link to the client.
3. Collect the client's favorites / final picks.
4. Use AI to suggest the best images for delivery — sharpness, expression, composition, and duplicate culling.

It is intentionally not a full studio-management platform. The MVP cuts everything that is not load-bearing for that loop.

---

## 1. Where the example stops being concrete

The BuildSolid constitution (`framework/docs/constitution.md` §15) keeps the Framework and Project System free of a product CLI, web app, package, runtime service, database, deployment automation, or project-generation logic. This example honors that rule:

- **Stages 0–8 (Intake → Task Breakdown) are fully fleshed out.** The example produces real, populated artifacts a solo photographer-builder could actually take to a builder agent.
- **Stages 9–12 (Implementation, QA, Deployment, Launch Prep) are artifact-level only.** The example fills `deployment.md` and `launch-checklist.md` as documents — it does **not** include source code, infrastructure-as-code, a live deployment, an analytics setup, or a launched product. It calls this stop-point out where the artifacts begin (see `deployment.md` §1 and `launch-checklist.md` §1).
- **Stage 13 (Iteration) has one substantive revisit touch only** — DEC-8 and the matching `changelog.md` entry show the constitution's "update artifacts in place" rule (constitution §3 principle 9). DEC-10 preserves an older classification for the later task-status compatibility correction, but the current compact treatment classifies that same-scope work as ordinary Existing Project Change; it is not a second product trigger or iteration. The example is not iterated to v2.

The validation notes in [`plan.md`](plan.md) also serve as compatibility fixtures. One preserves a verbose fourteen-stage applicability record, including explicit `N/A - reason` rows. Another shows the preferred compact Existing Project Change envelope. The same-scope task-status portability correction remains ordinary Existing Project Change because it does not cross the substantive Stage 13 iteration threshold.

If you are reading the example and expecting to find runnable code or a deployed photographer SaaS, stop here — that is outside this reference example's scope and would violate the constitution.

## 2. What artifacts the example contains

In BuildSolid phase order (see `framework/docs/context-package.md` §6):

| Stage | Artifact(s) | Status |
|---|---|---|
| 0. Intake | inline note in `founder-intent.md` §6 ("Active project profile and mode at intake") and §7 ("Raw idea at intake") | Fleshed |
| 1. Founder Discovery | `founder-intent.md`, `discovery.md` | Fleshed |
| 2. Idea Compression | `product-thesis.md`, `problem-statement.md` | Fleshed |
| 3. MVP Scope | `mvp-scope.md`, `non-goals.md` | Fleshed |
| 4. UX Direction | `design.md`, `user-journeys.md` | Fleshed |
| 5. Intelligence Layer | `intelligence-layer.md` | Fleshed |
| 6. Technical Architecture | `architecture.md` | Fleshed |
| 7. Spec Creation | `spec.md`, `plan.md` | Fleshed |
| 8. Task Breakdown | `tasks.md` | Fleshed |
| 9. Implementation | — | **Stops here.** Not produced; see §1. |
| 10. QA and Review | — | **Artifact-level only via** `known-issues.md`. No real code review. |
| 11. Deployment | `deployment.md` | **Artifact-level only.** No live deployment. |
| 12. Launch Prep | `launch-checklist.md` | **Artifact-level only.** Not launched. |
| 13. Iteration | DEC-8 plus the matching `changelog.md` revisit entry | **One substantive touch only.** DEC-10 is preserved historical classification, not a second product trigger. |

Cross-cutting artifacts: `AGENTS.md`, `CLAUDE.md`, `decisions.md`, `changelog.md`, `known-issues.md`.

## 3. The four-mode walkthrough invariant

BuildSolid supports four modes (Guided, Founder, Expert, Build — see `framework/docs/constitution.md` §9). This example must walk cleanly in each mode:

- **Guided** — a beginner photographer-builder can follow the artifacts in order, expanding each stage with the relevant skill, and reach the same end state.
- **Founder** — `project-system/skills/founder-discovery/SKILL.md` can pressure-test stages 1–3 against the artifacts in this example without needing additional context.
- **Expert** — an experienced solo builder can skim §4 ("Read in this order") and resume at stage 7 without re-deriving stages 1–6.
- **Build** — this artifact-only example does not enter Build Mode merely because `tasks.md` exists. A downstream implementation may act on a copied, current backlog only after explicit project implementation authority and accepted build inputs; no mandatory orchestrator preamble is required when entry is otherwise clear.

The example does **not** re-tell itself per mode. The same artifacts serve all four modes; the agent resolves and states the current posture, asks only on material ambiguity or a missing genuine prerequisite, and changes interaction depth accordingly (`framework/docs/constitution.md` §9). This matches `project-system/templates/AGENTS.md` §6 / `project-system/templates/CLAUDE.md` §3.

## 4. Read in this order

1. `AGENTS.md` — agent-neutral self-rules for the example project (a fill of `project-system/templates/AGENTS.md`).
2. `CLAUDE.md` — Claude-Code-specific guidance for the example project (a fill of `project-system/templates/CLAUDE.md`).
3. `founder-intent.md` — why the photographer is building this; intake project profile, mode, and raw idea live here.
4. `discovery.md` — observations about photographers and their delivery workflow.
5. `product-thesis.md` and `problem-statement.md` — compressed thesis + problem articulation.
6. `mvp-scope.md` and `non-goals.md` — what's in, what's explicitly out.
7. `user-journeys.md` and `design.md` — the deliver → select → finalize flow and minimalist UX direction.
8. `intelligence-layer.md` — the image-suggestion AI capability (sharpness, expression, composition, duplicate culling).
9. `architecture.md` — system architecture and stack for the MVP.
10. `spec.md`, `plan.md`, `tasks.md` — the project-level spec/plan/tasks the example produces.
11. `deployment.md`, `launch-checklist.md` — artifact-level only; see §1.
12. `decisions.md`, `changelog.md`, `known-issues.md` — cross-cutting living state, including the Stage 13 iteration touch.

Within the example, authority flows from the Framework constitution and context contract to accepted project decisions, then the accepted spec, plan, and tasks. Navigation files and checklists cannot reverse that order.

## 5. How skills and templates point at this example

Per `framework/docs/constitution.md` §11 item 10 and §12 item 7, skills and templates must reference this example by **pointer**, not by embedding it. Every shipped template's "Reference example fill" line points at the corresponding file in this directory (e.g., `project-system/examples/photographer-saas/founder-intent.md`). Every shipped skill's reference-example section points at the relevant artifact here. If a future skill or template embeds or duplicates content from this example, that is a constitution violation, not an enhancement.

## 6. Founder context

The example uses a single, named **synthetic** founder so the artifacts read as one coherent project, not a composite. Throughout this directory:

- **The founder persona is Maya Chen** — an illustrative freelance wedding and portrait photographer of seven years, building this product for herself and photographers like her, not as an investor pitch.
- **The active project profile at intake is New Product Build, and the mode is Founder Mode** — the photographer-builder is starting from a one-paragraph idea with no existing product, and wants the workflow to pressure-test that idea before scoping anything.
- **The example assumes a solo-founder budget**: roughly one quarter of part-time solo work to ship the MVP, no team, no funding round, no enterprise-sales aspiration.

If a later skill or template needs more biography than this, that is a sign the skill is over-asking. Keep it tight.

## 7. What this example does **not** do

- It does not generate code. The example stops at `tasks.md`.
- It does not stand up infrastructure. `deployment.md` is artifact-level.
- It does not launch the product. `launch-checklist.md` is artifact-level.
- It does not iterate beyond DEC-8's single substantive Stage-13 revisit touch; preserved DEC-10 history does not create another trigger.
- It does not introduce a second persona, a second product, or a second example. The current Project System ships exactly this one reference example.

If the workflow appears to require any of the above, first seek the applicable accepted project authority and Framework review. Amend Framework only when the proposed change would alter Framework itself; do not expand this example by implication.
