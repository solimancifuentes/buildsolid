# Photographer SaaS — Implementation Plan

Project-level implementation plan for the photographer SaaS reference example: how the artifacts described in [`spec.md`](spec.md) would get built. The plan defines the order of work, dependencies, parallelization, and merge criteria. It is not the task list — [`tasks.md`](tasks.md) follows.

This is a BuildSolid reference example. Per [`README.md`](README.md) §1, this plan describes a *would-build*; the example produces no implementation. The plan still has to be coherent enough that a competent agent could pick it up and build.

> The scenario, research corpus, people, measurements, permissions, galleries, eval data, and outcomes are synthetic and illustrative. Every implementation, provider selection, real-data use, legal conclusion, deployment, and live result below remains future downstream work.

Workflow phase: **Phase 7 — Spec Creation** (paired with [`spec.md`](spec.md)). Driving skill: `spec-planner`.

Governing artifacts (highest applicable authority first):

1. [`decisions.md`](decisions.md) — append-only accepted project choices and clarifications.
2. [`spec.md`](spec.md) — the current product contract, kept reconciled to accepted decisions.
3. This plan — implementation order for that contract.

If these conflict, stop and reconcile the lower-authority artifact before implementation; do not silently choose one.

Related artifacts: [`mvp-scope.md`](mvp-scope.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`tasks.md`](tasks.md), [`deployment.md`](deployment.md), [`launch-checklist.md`](launch-checklist.md).

---

## 1. Purpose

This plan describes the *shape* of the work that would build the photographer SaaS MVP. It names the build phases, the dependencies between artifacts, and the merge criteria for shipping v1. It does not enumerate per-file work — those live in [`tasks.md`](tasks.md). It is a downstream project plan, not a plan for changing BuildSolid itself.

## 2. Inputs

- [`spec.md`](spec.md) — goals, non-goals, acceptance criteria.
- [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md) — scope envelope.
- [`architecture.md`](architecture.md) — system shape (four components, no public API, no native mobile).
- [`intelligence-layer.md`](intelligence-layer.md) — AI design (one capability, closed output vocabulary, 300-frame golden set).
- [`design.md`](design.md) — four screens, AI-presentation rules, accessibility commitments.
- [`user-journeys.md`](user-journeys.md) — primary journey only.
- [`decisions.md`](decisions.md) — DEC-1 through DEC-12 hold the accepted project choices and append-only clarifications.

## 3. Decisions resolved at the planning level

- **Q1 — AI provider for v1. Unresolved.** DEC-4 requires a later append-only accepted entry naming the provider and dating its written no-retention/no-training commitment; C1 remains `Blocked` until it exists.
- **Q2 — Eval pass threshold. Resolved by DEC-6.** Precision ≥ 0.80 and recall ≥ 0.70 on the keeper label; the per-reason confusion matrix has no hard threshold.
- **Q3 — CSV export shape. Resolved by DEC-7.** Filenames only; no AI labels.

## 4. File and directory structure

The MVP source layout (would-be — not produced by this example):

```
.
├── README.md                       ✗
├── AGENTS.md                       ✓ (filled by BuildSolid template)
├── CLAUDE.md                       ✓ (filled by BuildSolid template)
├── spec.md                         ✓
├── plan.md                         ✓
├── tasks.md                        ✓
├── decisions.md                    ✓
├── changelog.md                    ✓
├── known-issues.md                 ✓
├── deployment.md                   ✓
├── launch-checklist.md             ✓
├── founder-intent.md               ✓
├── discovery.md                    ✓
├── product-thesis.md               ✓
├── problem-statement.md            ✓
├── mvp-scope.md                    ✓
├── non-goals.md                    ✓
├── user-journeys.md                ✓
├── design.md                       ✓
├── architecture.md                 ✓
├── intelligence-layer.md           ✓
├── client/                         ✗  (web client; not produced in this example)
├── api/                            ✗  (API service; not produced)
└── ops/                            ✗  (deployment notes only — see deployment.md)
```

Files marked ✓ exist as fills inside this example directory. Files marked ✗ are what an actual implementation would produce; the reference example does not produce them.

## 5. Build phases

The V3 and V4 labels below are stable local compatibility-fixture identifiers; they do not depend on an external plan, decision log, or validation record.

### V3 brownfield change — stalled-gallery dashboard state

This note preserves a verbose Existing Project Change impact-analysis record for the stalled-gallery compatibility review before Stage 8 task updates.

- Selected change: make the already-described `stalled` gallery dashboard state buildable and reviewable. A gallery becomes `stalled` after 14 days without client finalization, and the photographer can manually re-share the delivery link from the dashboard. No automated client reminder or nudge is added.
- Profile and mode: Existing Project Change; Expert Mode.
- Existing-state read: [`founder-intent.md`](founder-intent.md), [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md), [`user-journeys.md`](user-journeys.md), [`design.md`](design.md), [`architecture.md`](architecture.md), [`spec.md`](spec.md), this plan, [`tasks.md`](tasks.md), and [`decisions.md`](decisions.md) through DEC-8.
- Direction test: no change to product intent, target audience, product direction, AI capability, architecture shape, external dependencies, or non-goals.
- Earliest affected stage: Stage 3 MVP Scope, because the dashboard must-have needs to explicitly include the stalled state and manual re-share behavior before downstream spec and tasks can be updated.
- Stage 0 Intake: N/A - reason: unchanged by this change.
- Stage 1 Founder Discovery: N/A - reason: unchanged by this change.
- Stage 2 Idea Compression: N/A - reason: unchanged by this change.
- Stage 3 MVP Scope: affected; update [`mvp-scope.md`](mvp-scope.md) in place.
- Stage 4 UX Direction: already satisfied by [`user-journeys.md`](user-journeys.md) §1, [`design.md`](design.md) §3, and [`architecture.md`](architecture.md) §4; no new journey, screen, or status vocabulary is introduced.
- Stage 5 Intelligence Layer: N/A - reason: no AI capability, model boundary, eval, prompt, memory, or fallback change.
- Stage 6 Technical Architecture: N/A - reason: architecture already includes `stalled` in the Gallery status vocabulary and no component, data-store, provider, service, or integration shape changes.
- Stage 7 Spec Creation: affected; update [`spec.md`](spec.md) and this plan in place.
- Stage 8 Task Breakdown: blocked until this plan note and DEC-9 exist; then update [`tasks.md`](tasks.md) B7 in place.
- Stage 9 Implementation: not executed in this reference example; the example remains artifact-level only.
- Stage 10 QA and Review: record the artifact-level review verdict in ordinary task or review provenance.
- Stage 11 Deployment: N/A - reason: no deployment, environment, secret, rollout, or operational change.
- Stage 12 Launch Prep: N/A - reason: no launch-positioning, first-user, metrics, or readiness change.
- Stage 13 Iteration: N/A - reason: this is a planned brownfield validation change, not post-acceptance product feedback that re-enters through the iteration loop.

### V4 compact compatibility fixture — task status portability

This note preserves the historical Stage 13 classification recorded in local DEC-10 while showing the compact treatment of the accepted review risk persisted as [`known-issues.md`](known-issues.md) KI-9: the backlog omitted task `Status` fields. Under the compact lifecycle, this same-scope correction is ordinary Existing Project Change rather than a new Stage 13 event because it does not change accepted product direction, scope, architecture, acceptance, launch treatment, or cross-stage direction.

- **Direction test:** no change to product intent, target audience, product direction, scope, UX, AI behavior, architecture, deployment, launch plan, task ordering, or acceptance criteria.
- **Entry stage:** Stage 8 Task Breakdown, because the accepted backlog shape needs the implementation-state field.
- **Affected artifacts or stages:** this compact note in [`plan.md`](plan.md) and the existing [`tasks.md`](tasks.md) backlog; update every existing task in place with one allowed `Status` value while preserving task count and order.
- **Required downstream gates:** artifact-level Stage 10 validation confirms every task uses exactly `Not started`, `In progress`, `Blocked`, or `Done`, with task count and order unchanged; Stage 9 implementation remains outside the reference example.
- **Material exclusions:** Stages 0–7 and 11–13 have no product, discovery, scope, UX, AI, architecture, spec, deployment, launch, or substantive iteration change. The accepted local DEC-10 record remains valid history; the compact classification does not rewrite it.

The MVP would be built in five phases. Acceptance remains A → B → C → D → E, with one safety exception: D1 may and should run as soon as A4/A5 exist, and must be `Done` before any real client photo is admitted. Until then, build and rehearsal work uses synthetic fixtures only.

**Phase A — Plumbing.** Photographer signup/login, an empty dashboard, an API service that talks to object storage via signed URLs, the relational data store, basic deploy pipeline. Ends when a photographer can log in and see an empty dashboard.

**Phase B — Manual loop end-to-end.** Gallery upload, photographer review-and-mark UI (with no AI yet — pre-marks are blank), delivery link minting, client view (default-keepers + show-all), client selection capture, photographer notification on finalize, stalled-gallery dashboard state with manual re-share, CSV export. Uses synthetic fixtures and ends when the representative loop completes without AI.

**Phase C — Intelligence layer plugged in.** C1 is `Blocked` until the later provider-selection entry exists. After it is unblocked, build the minimized model-call boundary, scoring, fallback, cost controls, and eval harness against a real rights-cleared golden set. Ends only when the complete eval gate passes; the synthetic scenario supplies no such result.

**Phase D — Pre-launch hardening.** Activate the 90-day storage lifecycle and idempotent application-owned database purge; keep opaque tombstones outside snapshot lineage and prove purge-before-restore promotion; obtain qualified, jurisdiction-specific legal review; then complete observability, AI/image-boundary review, conventional application-security review, load rehearsal, and the checklist. D1's real-data gate applies even if the rest of Phase D follows Phase C.

**Phase E — Future real pilot.** Only after D1–D6 and the provider/legal gates pass, onboard a properly consented five-photographer cohort and measure the §4 thresholds. This example records no launch or result.

## 6. Artifact dependencies

- C1 depends on A4, A5, and the later accepted provider entry required by DEC-4/DEC-11; until then it is `Blocked`.
- C2–C5 remain `Not started` behind C1; a blocked prerequisite does not make completed work or evidence exist.
- The manual loop may be built with synthetic fixtures before provider selection.
- D1 depends on A4/A5 and gates every real-photo path: object-storage lifecycle deletion and the database purge must be active first.
- D1 also owns the opaque tombstone and restore-before-promotion controls from DEC-12.
- C5 requires a future real, rights-cleared 300-frame golden set; the scenario's synthetic research corpus is not that set.

## 7. Skill / capability creation order

The MVP produces a single AI capability and a small set of product capabilities. In order:

1. **Photographer auth + dashboard skeleton** — without this, every later capability has no surface to attach to.
2. **Gallery upload + review UI (manual mode)** — proves the loop without AI; foundation for Phase C.
3. **Delivery link + client view** — closes the loop on the client side.
4. **Client selection capture + photographer notification** — closes the loop overall.
5. **CSV export** — small but load-bearing for the photographer's downstream Lightroom step.
6. **AI image-suggestion capability** — the wedge; landed last so the rest of the loop is already proven.
7. **Retention enforcement first for real data; observability before launch** — run D1 as soon as storage and the data store exist; no real photo is admitted before it passes.

## 8. Sequential vs parallel work

The phases in §5 are sequential at the acceptance level. Within phases, work parallelizes well — the photographer surface and the client surface can be built by different agents in different sessions, with the API as the shared contract.

**Sequential:**

- Acceptance: Phase A → Phase B → Phase C → Phase D → Phase E.
- Safety exception: D1 may execute after A4/A5 and gates real data regardless of phase labels.
- Provider gate: C1 is `Blocked` until the later accepted provider entry; C2–C5 remain `Not started` behind it.
- Within Phase C after unblocking: boundary → scoring/fallback/cost controls → complete eval. C5 also depends on D1 because the full eval uses a future real rights-cleared set; A6 may source and label that set outside the product system before D1, but no real image enters the product or provider flow until D1 is `Done`.

**Parallel:**

- Within Phase A: API skeleton, web client skeleton, deploy pipeline can run in parallel.
- Within Phase B: photographer Screen 2 (upload + review) and client Screen 3 (delivery link) can run in parallel; both depend on the API contract from Phase A.
- Future rights-cleared golden-set sourcing and labeling may run in parallel with synthetic Phase A/B work.
- Qualified legal/privacy review and security review (Phase D) run in parallel with the rest of Phase D's work; the legal review determines which public surfaces and treatments are required.

## 9. Review checkpoints

- **Checkpoint A — End of Phase A.** Reviews: signup/login, dashboard skeleton, API skeleton, deploy pipeline. Criteria: a photographer can log in; an empty dashboard renders; the API authenticates a request; the deploy procedure has been exercised once.
- **Checkpoint B — End of Phase B.** Reviews: end-to-end manual loop. Criteria: one full gallery walks Deliver → Select → Finalize without AI; CSV export works; photographer notification fires; a gallery that remains unfinalized for 14 days appears as `stalled` with manual re-share and no automated client reminder.
- **Checkpoint C — End of Phase C.** Reviews: AI image-suggestion capability. Criteria: golden-set eval meets the threshold in §3 Q2; closed-vocabulary schema validation passes; fallback path verified; per-gallery cost ceiling enforced.
- **Checkpoint D — End of Phase D.** Reviews: pre-launch hardening. Criteria: every checkbox in [`spec.md`](spec.md) §10 and every prelaunch item in [`launch-checklist.md`](launch-checklist.md) is satisfied; provider, full eval, retention/restore, security, qualified legal, and real-data gates cannot be deferred or passed by mitigation.
- **Checkpoint E — End of Phase E (launch).** Reviews: success metrics from [`mvp-scope.md`](mvp-scope.md) §4. Criteria: at minimum, five photographers have delivered one gallery each; median time-to-delivered-gallery < 15 min; client decide-time tracking has at least three data points within < 5 days.

Reviews produce task, review, or pull-request provenance. Meaningful accepted choices, exceptions, or tradeoffs are recorded in [`decisions.md`](decisions.md); routine pass/fail results need no duplicate decision entry.

## 10. Validation strategy

- **Structural validation:** every required capability in [`spec.md`](spec.md) §7 has a working code path and is exercised by the primary journey.
- **Walkthrough validation:** a real-photo walkthrough may occur only after D1, provider selection where applicable, rights/consent, and required legal treatment are satisfied; until then use representative synthetic fixtures.
- **AI-layer evals:** golden-set eval per [`intelligence-layer.md`](intelligence-layer.md) §5 on every model or policy change, monthly cadence regardless.
- **Security review:** review the AI/image/data boundary first, treating image-mediated prompt injection as possible and testing the closed-schema, tool-less, minimized, isolated, reject-on-nonconformance boundary as mitigations; then complete conventional application security. Both pass before readiness.
- **Privacy and legal review:** verify 90-day storage/database deletion, external tombstones, restore-before-promotion, provider commitments, and logging boundaries; qualified review determines applicable legal treatment.
- **Performance rehearsal:** staging load test with five concurrent active photographers each uploading a 600-frame gallery; latency and AI scoring time captured against [`architecture.md`](architecture.md) §7 targets.

## 11. Merge criteria

The conditions that must all be true for v1 to be considered shippable:

1. Every checkbox in [`spec.md`](spec.md) §10 is checked.
2. Phases A–D have passed their checkpoints; ordinary outcomes have task, review, pull-request, or change provenance, and any meaningful accepted choice, exception, or tradeoff is recorded in [`decisions.md`](decisions.md).
3. Eval pass on the 300-frame golden set meets the threshold in §3 Q2.
4. No `Critical` or `High` item anywhere in [`known-issues.md`](known-issues.md) is `Open`; an empty Bugs section cannot mask a blocker categorized as a Gap or Debt.
5. [`launch-checklist.md`](launch-checklist.md) §1–§9 all checked; provider, full eval, retention/restore, security, qualified legal, and real-data gates cannot be waived or passed by a logged mitigation.
6. The initial ≤10-active-photographer operating projection remains under $200/month; the separate technical-capacity envelope is not represented as a cost promise.
7. Qualified review is complete and every required public artifact and treatment is implemented.
8. D1's deletion/tombstone/restore controls and the provider gate pass before the properly consented pilot cohort is admitted.

## 12. Risks and mitigations

Plan-level risks. Extends, does not replace, [`spec.md`](spec.md) §11.

- **P1. Phase B reveals the manual loop is not the photographer's loop.** The synthetic assumptions may be wrong. *Mitigation:* exercise synthetic fixtures first, then a properly authorized real pilot only after its gates; revisit scope before Phase C if the loop fails.
- **P2. Golden-set sourcing or labeling drags on.** The future 300-frame set requires real rights and consent. *Mitigation:* start sourcing early, but do not treat a partial run as Phase C completion; the complete threshold gates Phase C.
- **P3. Security, privacy, or legal review surfaces a structural issue.** Qualified review may change required artifacts or treatment. *Mitigation:* review the AI/image boundary first, conventional appsec second, and complete qualified legal review before real use.
- **P4. Initial cost ceiling cannot be held.** Real volume or provider pricing may exceed the ≤10-photographer operating estimate; the ≤50/50,000 capacity envelope is not a cost promise. *Mitigation:* enforce cost ceilings after provider selection and requalify pricing before scaling.
- **P5. Founder time budget runs out before Phase D.** 120–180 hours absorbed by Phases A–C. *Mitigation:* stop for scope requalification and an accepted decision before removing any required capability. Provider, complete eval, retention/restore, security, qualified legal, and real-data gates remain intact and cannot be downscoped or passed by mitigation; no other required capability has a pre-authorized cut order.

---

## Optional sections

### A. Build environment and tools

The specific AI provider and concrete language/framework choices remain unresolved. `starter-stack-advisor` can propose a provider-neutral baseline, but no advisor output selects a provider or stack without the applicable accepted entry.

### B. CI/CD strategy

A standard "main branch deploys to staging; tagged release deploys to production" pipeline is sufficient for v1. No multi-environment promotion machinery; no canary infrastructure beyond the "one photographer at a time" launch sequencing in Phase E. Detailed deployment design lives in [`deployment.md`](deployment.md).

### C. Multi-workspace coordination

Not applicable. The MVP is built by a single founder in a single working tree. If a future iteration introduces a contributor, the self-rules in [`AGENTS.md`](AGENTS.md) §5 apply: agent-neutral artifacts in tracked files, scratch in `.context/`.

### D. Versioning convention

CalVer (`YYYY.MM.PATCH`) for the shipped product. The canonical version string lives in [`changelog.md`](changelog.md) headings. Versioning was chosen over semver because the product is a single hosted SaaS and the calendar version is more meaningful than an API-stability promise.
