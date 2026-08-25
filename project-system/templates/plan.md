# <Project> — Implementation Plan

> **Purpose.** Project-level **implementation plan**: how the artifacts described in [`spec.md`](spec.md) get built. The plan defines file/directory layout, the order of work, dependencies between artifacts, parallelization strategy, and merge criteria. It is **not** the task list — `tasks.md` follows.
>
> **Workflow phase.** Phase 7 — Spec Creation (paired with `spec.md`).
>
> **Driving skill.** `spec-planner`.
>
> **How to use this template.**
> - Replace `<Project>` and any `<…>` placeholder with project-specific content.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the plan filled.
> - Stable headings — [`tasks.md`](tasks.md) and the QA reviewer skill rely on them.
> - **The plan describes the shape of the work, not the work itself.** Per-file work items live in [`tasks.md`](tasks.md).
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Required after impact analysis** for Existing Project Change, and **Required** for Lightweight/Internal Build. New Product Build uses the full lifecycle by default. Existing Project Change records the compact impact outcome when material. Lightweight/Internal Build uses the smallest proportionate lifecycle slice.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it identifies authoritative inputs, resolved planning choices, structure, applicable build phases, dependencies, sequencing, review checkpoints, validation, merge criteria, risks, and any material lifecycle exclusions. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/plan.md`.

Project-level governing artifacts, subject to the BuildSolid Framework, use this precedence:

1. [`decisions.md`](decisions.md) — accepted project decisions, when present.
2. [`spec.md`](spec.md) — what must be true to ship within those decisions.
3. This plan — how the accepted spec is implemented.

If these sources conflict, stop and name the conflict. A later accepted decision controls only its stated question, but the stale owning artifact must be updated in place before this plan is used. Neither this plan nor the spec silently overrides an accepted decision.

Related artifacts: [`mvp-scope.md`](mvp-scope.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`tasks.md`](tasks.md), [`deployment.md`](deployment.md), [`launch-checklist.md`](launch-checklist.md).

---

## 1. Purpose

> One short paragraph. What this plan is for and what it is **not** for. Avoid restating the spec.

<…>

## 2. Inputs

> Bulleted list. The accepted artifacts and assumptions this plan takes as authoritative when building begins. Include only genuine prerequisites for the applicable work and remove any example bullet that does not apply to the affected slice. If a genuine prerequisite is missing, still draft, or materially conflicting, the plan is incomplete until it is resolved or explicitly deferred by the human. Record a material exclusion only after determining that an omitted stage or artifact is not a genuine prerequisite for the accepted work.

- [`spec.md`](spec.md) — goals, non-goals, acceptance criteria.
- [`founder-intent.md`](founder-intent.md) — accepted intent or durable project profile or mode choices, when this artifact is present and applicable.
- [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md) — accepted scope envelope, when present and applicable to the affected work.
- [`architecture.md`](architecture.md) — accepted system shape, when the affected work depends on or changes it.
- [`intelligence-layer.md`](intelligence-layer.md) — accepted AI design, when the affected work includes a load-bearing intelligence layer.
- <…>

For an **Existing Project Change**, use this compact impact block when the outcome is not already clear across the accepted `spec.md`, this plan, and [`tasks.md`](tasks.md). If another accepted section already owns an item, link it instead of duplicating it. These are the five compact fields; do not add a fourteen-stage applicability ledger solely to prove omission.

- **Direction test:** <Does the change alter product intent, target audience, or product direction? State yes or no and the accepted basis.>
- **Entry stage:** <Earliest affected lifecycle stage.>
- **Affected artifacts or stages:** <Only the accepted artifacts or stages the change touches.>
- **Required downstream gates:** <Actual prerequisite, review, security, deployment, launch, authority, or acceptance gates that must run.>
- **Material exclusions:** <Omissions whose absence would otherwise be surprising, ambiguous, or consequential; write "None" when there are no material exclusions.>

For a **New Product Build**, Stage 0 and the full ordered lifecycle remain the default; record only actual conditional-stage decisions or material deviations. Existing full matrices and `N/A - reason: <reason>` records remain valid and need no migration. For a **Lightweight/Internal Build**, plan only the smallest proportionate lifecycle slice and do not create empty artifacts or rows solely to record inapplicability.

## 3. Decisions resolved at the planning level

> Resolutions to material open questions in [`spec.md`](spec.md) §12 (and material questions surfaced during planning). Record the planning choice here. Mirror it into [`decisions.md`](decisions.md) only when it is a meaningful accepted choice, override, deferral, rejection, or tradeoff that needs durable rationale; ordinary planning detail does not require a second record.

- **Q1 — <name>.** Resolved. <planning choice>. *Rationale:* <…>. <Link to `decisions.md` only when the decision threshold is met.>
- **Q2 — <name>.** Resolved. <planning choice>. *Rationale:* <…>. <…>

## 4. File and directory structure

> The target file/directory layout for the project's source code, infrastructure, and documentation. Use a code block. Mark files that already exist (✓) and files that will be created (✗). Do not list every file individually for large directories — list the top-level shape and call out the files that matter.

```
.
├── README.md                  ✓ / ✗
├── <…>
└── <…>
```

> If the project's structure is documented elsewhere (e.g., a separate engineering README), point at it instead of duplicating it here.

## 5. Build phases

> The phases of work, in order. Phases are typically sequential at the *acceptance* level; work *inside* a phase can often run in parallel. Each phase: name, what it produces, what it ends with.
> Shape the level of detail to the project profile resolved and stated for the current work. Use a durable choice in [`founder-intent.md`](founder-intent.md) when one exists; ordinary session posture need not be persisted. Do not invent additional profiles or numeric risk tiers.
> Include only the applicable build phases. For Existing Project Change and Lightweight/Internal Build, the compact impact outcome and material exclusions explain material omissions; do not create an N/A-only phase or full lifecycle ledger. Existing `N/A - reason: <reason>` records remain valid, and the token may still explain a specific material omission when useful.
> Stage 9 implementation support uses this plan plus [`tasks.md`](tasks.md) per `framework/docs/context-package.md` §8E.

**Phase A — <name>.** <one or two sentences>.
**Phase B — <name>.** <…>.
**Phase C — <name>.** <…>.
**Phase D — <name>.** <…>.

> Add or remove phases to fit the project. Most v0.1 MVPs need 3–6 phases.

## 6. Artifact dependencies

> Dependencies that constrain the order of work, beyond the obvious "specs before implementation." Each: one line.

- <artifact / capability> depends on <…>.
- <artifact / capability> depends on <…>.

## 7. Skill / capability creation order

> If the project produces multiple capabilities or modules, list them in the order they should be built. Capture the dependency reason on each line. If the project is a single deliverable, this section can be a single bullet.

1. **<capability>** — <reason>.
2. **<capability>** — <reason>.
3. <…>

## 8. Sequential vs parallel work

> A short paragraph plus two bullet groups: what must be done sequentially (and why) and what can run in parallel.

**Sequential:**

- <…>
- <…>

**Parallel:**

- <…>
- <…>

## 9. Review checkpoints

> Reviews for the applicable phases and final integration. Each checkpoint: a name, the artifact it reviews, the criteria it checks. Record ordinary results in task, review, or pull-request provenance; add a [`decisions.md`](decisions.md) entry only when the review resolves a meaningful choice, override, deferral, rejection, or tradeoff.

- **Checkpoint A — <name>.** Reviews <…>. Criteria: <…>.
- **Checkpoint B — <name>.** Reviews <…>. Criteria: <…>.
- **Checkpoint <…> — <name>.** <…>.

## 10. Validation strategy

> Bulleted list. How the project knows the work is correct: structural checks, walkthroughs, manual or automated tests, evals for the AI layer, security reviews. Each bullet: one line.

- **Structural validation:** <…>.
- **Walkthrough validation:** <…>.
- **AI-layer evals:** <…> (cross-references [`intelligence-layer.md`](intelligence-layer.md) §5).
- **Security review:** <…>.
- **<other>:** <…>.

## 11. Merge criteria

> The conditions that must all be true for the version to be considered shippable. Aligns with [`spec.md`](spec.md) §10 acceptance criteria but adds plan-level requirements (clean checkpoints, meaningful decisions logged, no scope drift). Each: one line.

1. <…>
2. <…>
3. <…>

## 12. Risks and mitigations

> Plan-level risks. Extends, does not replace, [`spec.md`](spec.md) §11. Each: a name, the risk, the mitigation.

- **P1. <name>.** <one-line risk>. *Mitigation:* <one-line approach>.
- **P2. <name>.** <…>. *Mitigation:* <…>.

---

## Optional sections

### A. Build environment and tools *(optional)*

> The development environment the plan assumes (toolchain, runtime versions, package managers). Skip if the project README covers this.

### B. CI/CD strategy *(optional)*

> If the project uses CI/CD, name the pipeline at the planning level. Detailed deployment design lives in [`deployment.md`](deployment.md).

### C. Multi-workspace coordination *(optional)*

> If the team uses parallel workspaces (Conductor or otherwise), describe how artifacts are owned and merged. Inter-workspace coordination scratch belongs in `.context/` (or equivalent), never in tracked artifacts.

### D. Versioning convention *(optional)*

> The project's versioning scheme (semver, calver, or otherwise) and which file holds the canonical version string.
