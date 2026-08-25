# Decisions — Photographer SaaS

Running log of decisions made about **this project** (the photographer SaaS reference example): scope, architecture, intelligence-layer tradeoffs, deployment choices, accepted/rejected proposals. The decisions log is the durable memory for "why is this project shaped this way?"

This is the **project-level** decisions log for the example. Record only decisions about this photographer SaaS here. Changes to BuildSolid's Framework or Project System source belong to the applicable BuildSolid governance and review process, not this downstream project log.

Related artifacts: [`spec.md`](spec.md), [`plan.md`](plan.md), [`tasks.md`](tasks.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md).

---

## How to read this file

Each decision uses this shape:

```
### DEC-<N> — <Title>
**Date:** YYYY-MM-DD
**Status:** Proposed / Accepted
**Context:** what prompted the decision.
**Decision:** what was decided.
**Rationale:** why.
**Consequences:** what this implies for downstream work.
**References:** links to spec/plan/tasks/architecture sections, prior decisions.
```

Append new decisions at the bottom. Do not edit accepted decisions in place. A later accepted entry records and links any supersession or revert while the earlier bytes remain historical truth.

---

## Entries

### DEC-1 — Single shoot type for the MVP, multi-style deferred

**Date:** 2026-04-27
**Status:** Accepted
**Context:** The founder works across weddings, portraits, and brand shoots. Discovery surfaced that style-specific AI weighting matters ([`discovery.md`](discovery.md) §3 Theme 5). The MVP needs to choose between launching with a single neutral scoring model or shipping per-style weighting from day one.
**Decision:** The MVP launches with a **single neutral scoring model** that targets event-and-portrait shoot types in aggregate. Per-style weighting (wedding-specific, portrait-specific, brand-specific) is deferred to a stage-13 iteration after the wedge has been validated.
**Rationale:** Per-style weighting requires either three labeled golden sets or a clean way to fork weights, both of which expand the founder's time budget past the [`mvp-scope.md`](mvp-scope.md) §6 ceiling. The wedge in [`product-thesis.md`](product-thesis.md) §2 is "AI-pre-marked favorites built into the loop" — neutrality of the scorer is acceptable for v1 if the override path is robust.
**Consequences:** Photographers whose style is far from the neutral scorer will see higher override rates; that signal is watched in production ([`intelligence-layer.md`](intelligence-layer.md) §5) and triggers the first iteration if sustained.
**References:** [`mvp-scope.md`](mvp-scope.md) Optional C; [`intelligence-layer.md`](intelligence-layer.md) §2; [`discovery.md`](discovery.md) §3 Theme 5, Optional C.

### DEC-2 — Web-only client; no native mobile in v1

**Context:** [`founder-intent.md`](founder-intent.md) Optional B names "no mobile-first product" as a personal anti-goal; the audience uses desktop or tablet primarily. Building a native mobile app would expand the surface significantly.
**Date:** 2026-04-27
**Status:** Accepted
**Decision:** v1 ships **as a single-page web application** that is responsive enough to be usable on tablets and modern mobile browsers. No native iOS or Android app is built.
**Rationale:** Mobile-web absorbs the small fraction of mobile use without a native build; a native app would push the founder's time budget past the [`mvp-scope.md`](mvp-scope.md) §6 ceiling.
**Consequences:** The architecture has one client; deployment has no app-store dependency; the [`design.md`](design.md) accessibility commitment targets responsive web at WCAG 2.1 AA.
**References:** [`architecture.md`](architecture.md) §1 / §6; [`non-goals.md`](non-goals.md) §1; [`founder-intent.md`](founder-intent.md) Optional B.

### DEC-3 — Synchronous-from-photographer-perspective scoring; client surface unauthenticated

**Date:** 2026-04-27
**Status:** Accepted
**Context:** Two architectural shape choices were considered together: whether to introduce a general-purpose worker farm for background work, and whether to require clients to log in.
**Decision:**
- **No general-purpose background-worker farm.** The only background work is the upload-time AI scoring pass, dispatched directly by the API service.
- **The client surface is unauthenticated, scoped to a token-based delivery link.**
**Rationale:** A worker farm would introduce a new failure surface for no thesis-critical gain ([`product-thesis.md`](product-thesis.md) §2 wedge). Asking clients to authenticate would add friction on the slow side of the loop ([`problem-statement.md`](problem-statement.md) §2) and produce no value for the wedge. **Specifically considered as non-goals and kept *in scope*:** the photographer notification on client-finalize (necessary; without it the photographer is back to manual chasing) and the photographer dashboard (necessary; for 5–40 galleries/month a status view is the cheapest answer).
**Consequences:** [`architecture.md`](architecture.md) §3 has four components; [`tasks.md`](tasks.md) Phase B order proves the manual loop before the AI lands.
**References:** [`architecture.md`](architecture.md) §6; [`non-goals.md`](non-goals.md) Optional B (kept-in-scope items).

### DEC-4 — Single AI provider for v1; second provider designed-in but not enabled

**Date:** 2026-04-27
**Status:** Accepted
**Context:** The intelligence layer requires a managed vision-language provider that does not retain or train on submitted images ([`intelligence-layer.md`](intelligence-layer.md) §4). Provider-redundancy support is named as a stage-13 candidate ([`intelligence-layer.md`](intelligence-layer.md) Optional C).
**Decision:** v1 launches on a **single managed AI provider** whose written privacy commitment ("no retention, no training on submitted images") is on file before integration begins. The model-call boundary in the API service is designed to support a second provider via a switch policy, but the second provider is **not enabled** for v1. The chosen provider's name and the date of the commitment letter are recorded as a separate dated entry below this one when the integration begins.
**Rationale:** A single provider keeps the security review and cost-modeling small; the boundary's switchability future-proofs against provider terms changing.
**Consequences:** If the chosen provider's policy changes, the integration is suspended (per [`intelligence-layer.md`](intelligence-layer.md) §2 Model choice); the boundary supports a fast switch but the second provider's eval-score parity must be confirmed before activation.
**References:** [`intelligence-layer.md`](intelligence-layer.md) §2, §4, Optional C; [`architecture.md`](architecture.md) §5, §6.

### DEC-5 — 90-day retention for client photos; photographer-extendable

**Date:** 2026-04-27
**Status:** Accepted
**Context:** Privacy commitments to clients require a definite retention window. Indefinite retention conflicts with both founder anti-goals and GDPR posture; sub-90-day retention causes friction for slow-deciding clients (5–14 day baseline).
**Decision:** Client photos and derived data (suggestions, selections) are deleted **90 days after the gallery is finalized**. The photographer can explicitly extend retention on a per-gallery basis (no global setting). Deletion is enforced at both the storage layer (lifecycle policy) and the application data store (cascade-delete).
**Rationale:** 90 days comfortably covers the 5–14 day decide window plus the photographer's typical post-finalization reuse; per-gallery extension handles the edge case of a client returning months later for a print or revision; dual-layer enforcement prevents drift.
**Consequences:** [`tasks.md`](tasks.md) D1 enforces this; [`launch-checklist.md`](launch-checklist.md) §3 requires a passing retention-job rehearsal in `staging`; [`deployment.md`](deployment.md) §9 names this commitment.
**References:** [`intelligence-layer.md`](intelligence-layer.md) §4; [`architecture.md`](architecture.md) §6 / §7; [`deployment.md`](deployment.md) §9.

### DEC-6 — Eval-pass thresholds: precision ≥ 0.80, recall ≥ 0.70 on the keeper label

**Date:** 2026-04-27
**Status:** Accepted
**Context:** [`spec.md`](spec.md) §12 Q2 left the eval threshold open. The 300-frame golden set with photographer-as-judge labels has natural disagreement at the boundary; the threshold has to acknowledge that.
**Decision:** Precision ≥ 0.80 on the keeper label and recall ≥ 0.70 on the keeper label, on the 300-frame golden set, are required before any model or policy change is promoted to `production`. Per-reason confusion matrix is computed and reviewed but does not have a numeric threshold.
**Rationale:** Precision matters more than recall in this product because a missed keeper is recoverable on Screen 2 review (the photographer can mark it manually), but a non-keeper that gets surfaced to the client is the visible failure mode. The recall floor at 0.70 prevents the model from being so conservative that the wedge collapses.
**Consequences:** [`tasks.md`](tasks.md) C5 enforces; [`launch-checklist.md`](launch-checklist.md) §2 has the corresponding checkbox; the threshold revisits if photographer-as-judge labeling shows it is structurally unreachable.
**References:** [`intelligence-layer.md`](intelligence-layer.md) §5; [`plan.md`](plan.md) §3 Q2.

### DEC-7 — CSV export contains filenames only

**Date:** 2026-04-27
**Status:** Accepted
**Context:** [`spec.md`](spec.md) §12 Q3 asked whether the CSV export includes AI labels alongside filenames.
**Decision:** The CSV export contains **filenames only**. AI labels (`sharp`, `eyes-open`, `composition`, `duplicate-of-<id>`) are not exported.
**Rationale:** The CSV is consumed by Lightroom for the photographer's final edit pass; AI labels are an implementation detail that the photographer's downstream tools should not depend on. Keeping the export shape stable also keeps the AI-presentation rule in [`design.md`](design.md) §4 honest (AI never appears on the client surface; the export is photographer-side, but consistency is cheap).
**Consequences:** [`tasks.md`](tasks.md) B8 produces a narrow, stable export. If a future iteration ever needs AI labels in the export, the change is a fresh decision and a versioned export, not an in-place schema break.
**References:** [`plan.md`](plan.md) §3 Q3; [`spec.md`](spec.md) §12 Q3; [`design.md`](design.md) §4.

### DEC-8 — Stage 13 iteration touch: signal that triggers the first iteration

**Date:** 2026-04-29
**Status:** Accepted
**Context:** The BuildSolid reference example demonstrates Stage 13 (Iteration) by a brief revisit touch. The example needs to *show* what an iteration entry looks like in this project's decisions log without actually iterating to a second product version.
**Decision:** The **first iteration trigger** for this project is **override rate > 50% sustained across at least three photographers in a calendar week**, as measured on the production override-rate dashboard ([`intelligence-layer.md`](intelligence-layer.md) §5). When that signal fires, the first iteration is a revisit of [`intelligence-layer.md`](intelligence-layer.md) §2 (model and policy) **updated in place** (per `framework/docs/constitution.md` §3 principle 9), with the existing single-style scoring model replaced by a per-style variant. No parallel `intelligence-layer-v2.md` is created.
**Rationale:** The override-rate signal is the most direct production proxy for the "AI is wrong on my style" failure mode in [`discovery.md`](discovery.md) §3 Theme 5. Three photographers (rather than one) is the threshold to avoid reacting to a single outlier. Updating in place preserves the constitution's iteration rule.
**Consequences:** When this signal fires, [`intelligence-layer.md`](intelligence-layer.md) §2 is edited in place with a paired entry in [`changelog.md`](changelog.md) (already shown as the iteration touch under "Unreleased" → Notes). [`mvp-scope.md`](mvp-scope.md) Optional C is updated to remove "single neutral style" from the deferred list and DEC-1 is superseded by a forward-link entry that records the move from neutral to per-style scoring.
**References:** `framework/docs/constitution.md` §3 principle 9; [`intelligence-layer.md`](intelligence-layer.md) §5, §8; DEC-1 (current single-style decision that the iteration would supersede); [`changelog.md`](changelog.md) Unreleased.

### DEC-9 — Brownfield alignment for stalled-gallery dashboard state

**Date:** 2026-07-02
**Status:** Accepted
**Context:** A brownfield compatibility review selected this tracked reference project as the target for an Existing Project Change in Expert Mode. The existing-state read found that [`user-journeys.md`](user-journeys.md) §1 and [`design.md`](design.md) §3 already describe a `stalled` gallery state after 14 days without client finalization, and [`architecture.md`](architecture.md) §4 already includes `stalled` in the Gallery status vocabulary. [`mvp-scope.md`](mvp-scope.md), [`spec.md`](spec.md), [`plan.md`](plan.md), and [`tasks.md`](tasks.md) did not make that state buildable or reviewable, creating artifact drift.
**Decision:** Keep the stalled-gallery behavior in scope as part of the existing photographer dashboard capability: after 14 days without client finalization, the dashboard surfaces the gallery as `stalled` and lets the photographer manually re-share the delivery link. The product still does not send automated client reminders or nudges.
**Rationale:** This is not a new product direction. It makes an already-accepted journey failure mode and UX state explicit in the downstream scope, spec, plan, and task contract. Manual re-share preserves the non-goal against client-side reminders while still giving the photographer an actionable dashboard state.
**Consequences:** The brownfield change enters at Stage 3 (MVP Scope). Stages 1-2 remain unchanged. [`mvp-scope.md`](mvp-scope.md), [`spec.md`](spec.md), [`plan.md`](plan.md), and [`tasks.md`](tasks.md) are updated in place. No new project artifact, external integration, reminder system, or implementation code is introduced.
**References:** [`founder-intent.md`](founder-intent.md) §3; [`mvp-scope.md`](mvp-scope.md) §2-§3; [`non-goals.md`](non-goals.md) §1; [`user-journeys.md`](user-journeys.md) §1; [`design.md`](design.md) §3; [`architecture.md`](architecture.md) §4; [`spec.md`](spec.md) §7/§10; [`plan.md`](plan.md) §5/§9; [`tasks.md`](tasks.md) B7.

### DEC-10 — Stage 13 iteration for task status portability

**Date:** 2026-07-03
**Status:** Accepted
**Context:** Review of the accepted stalled-gallery brownfield pass recorded a follow-up risk: most tasks in [`tasks.md`](tasks.md) omitted the `Status` field required by the Stage 9 implementation-support procedure. The feedback is recorded as [`known-issues.md`](known-issues.md) KI-9. This accepted entry preserves the original Stage 13 treatment because the finding followed acceptance of the artifact set; under the current compact lifecycle, the same-scope correction would remain ordinary Existing Project Change.
**Decision:** Re-enter at Stage 8 (Task Breakdown) in Existing Project Change / Expert Mode and update [`tasks.md`](tasks.md) in place so the task shape and every existing task carry a `Status` field. Set every task to `Not started`, because this reference example remains artifact-level only and no would-build implementation task has begun.
**Rationale:** The change is bounded to implementation-state reconstructability. It does not alter product intent, target audience, product direction, scope, UX, AI behavior, architecture, deployment, launch plan, task ordering, or acceptance criteria. Adding `Status` fields aligns the accepted reference backlog with the Stage 9 contract while preserving the example's would-build stop point.
**Consequences:** [`plan.md`](plan.md) §5 records the impact analysis before the backlog update. [`tasks.md`](tasks.md) is updated in place; no task is marked `Done`, `In progress`, or `Blocked`. No new permanent example, canonical artifact, external integration, runtime, tool, script, or repository structure is introduced.
**References:** [`known-issues.md`](known-issues.md) KI-9; [`plan.md`](plan.md) §5; [`tasks.md`](tasks.md).

### DEC-11 — Clarify the neutral scorer and unresolved integration boundaries

**Date:** 2026-08-25
**Status:** Accepted
**Context:** Cross-artifact review found that DEC-1's title, DEC-3's worker wording, and shorthand descriptions of DEC-4 could be read more narrowly or more finally than their accepted bodies.
**Decision:** DEC-1's body controls over its misleading title: v1 uses one neutral scorer across the selected event-and-portrait shoot types in aggregate, while per-style weighting remains deferred. DEC-3 continues to prohibit a general-purpose worker farm but permits one provider-neutral daily trigger for the idempotent application-owned retention purge. DEC-4 selects provider criteria and a single-provider launch shape, not a specific provider; integration remains blocked until a later accepted entry names the provider and records its dated written no-retention/no-training commitment.
**Rationale:** These readings preserve the accepted product scope while making the scorer, retention enforcement, and provider gate executable without rewriting historical entries.
**Consequences:** All downstream scorer wording uses the aggregate event-and-portrait interpretation. The narrow purge does not authorize a general worker system. C1 remains `Blocked` until the provider entry exists, and no file may imply a selected provider before then. Provider choice, self-hosting, localization, multi-region operation, on-call changes, deletion automation, and other deferred work are not alternate first-iteration triggers; DEC-8's sustained override-rate signal remains the sole accepted first trigger.
**References:** DEC-1, DEC-3, DEC-4; [`mvp-scope.md`](mvp-scope.md) §2 / Optional C; [`architecture.md`](architecture.md) §3 / §6; [`tasks.md`](tasks.md) C1 / D1.

### DEC-12 — Supplement 90-day deletion with restore-safe enforcement

**Date:** 2026-08-25
**Status:** Accepted
**Context:** DEC-5 binds storage and application-data deletion after 90 days but does not state how database snapshots and restored environments preserve that promise.
**Decision:** Store opaque deletion tombstones outside the application database's snapshot lineage and retain each until every snapshot capable of containing the deleted records has expired. Before a restored environment receives traffic or is promoted, apply those tombstones and current-time expiry, purge affected active and derived records, and verify completion. Missing tombstones, purge failure, or failed verification blocks promotion.
**Rationale:** A backup must not reactivate data that the active system has already deleted under DEC-5. Isolating tombstones from snapshots and enforcing them before traffic closes that restore gap without changing the 90-day rule.
**Consequences:** D1, deployment recovery, monitoring, and launch readiness cover storage lifecycle, scheduled datastore purge, tombstone retention, and restore-time purge. These controls must operate before real client photos are admitted.
**References:** DEC-5; [`intelligence-layer.md`](intelligence-layer.md) §4; [`architecture.md`](architecture.md) §4 / Optional C; [`deployment.md`](deployment.md) §5 / §7; [`tasks.md`](tasks.md) D1; [`launch-checklist.md`](launch-checklist.md) §3 / §5.

---

## Optional: supersession index

> Derived navigation only. A later accepted entry may state that it supersedes or reverts an earlier entry, but accepted historical bytes remain unchanged. No supersession is indexed at this time.
