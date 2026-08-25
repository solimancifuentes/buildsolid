# Launch Checklist — Photographer SaaS

The list of things that must be **true** before the photographer SaaS is launched to its first users. Launch is the moment the product becomes accountable to people outside the team — this checklist is what prevents the easy mistakes from happening on launch day.

> **Stop-point notice (per [`README.md`](README.md) §1).** This artifact is a BuildSolid v0.1 reference example fill. It describes the *would-launch* checklist that a real implementation phase would walk. It is not a record of a launched product — none of the boxes below are actually checked. Treat it as a planning artifact, not as a release log.

> **Legal and evidence posture.** These unchecked items are illustrative readiness requirements. A real launch remains blocked until qualified, jurisdiction-specific review determines applicable regimes and required notices, terms, consent, deletion, subprocessor, consumer, and related treatment; the scenario records no completed review or live result.

Workflow phase: **Phase 12 — Launch Prep.** Driving skill: `launch-prep`.

Related artifacts: [`spec.md`](spec.md), [`mvp-scope.md`](mvp-scope.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`deployment.md`](deployment.md), [`decisions.md`](decisions.md).

---

## 1. Product

The product itself works for the journey named in [`user-journeys.md`](user-journeys.md).

- [ ] Primary journey ([`user-journeys.md`](user-journeys.md) §1) completes end-to-end without manual intervention outside the seven listed steps.
- [ ] All [`spec.md`](spec.md) §10 acceptance criteria are checked.
- [ ] Empty / loading / error states are handled for each of the four key screens ([`design.md`](design.md) §3 + Optional D).
- [ ] Photographer can revoke a delivery link.
- [ ] Photographer can extend retention beyond 90 days for a specific gallery.
- [ ] CSV export of finalized selections returns filenames only ([`plan.md`](plan.md) §3 Q3).

## 2. Intelligence layer

The AI layer ([`intelligence-layer.md`](intelligence-layer.md)) is evaluated and bounded before launch.

- [ ] A real, rights-cleared 300-frame golden set has been assembled and labeled; the scenario's synthetic research is not that eval corpus.
- [ ] The complete eval meets DEC-6's precision ≥0.80 and recall ≥0.70 thresholds; a partial run cannot pass the gate.
- [ ] A later append-only accepted entry names the AI provider and dates its written no-retention/no-training commitment; task C1 remains `Blocked` until then.
- [ ] The provider boundary forwards only downscaled JPEG bytes and an opaque frame ID; all identifying, gallery, filename, metadata, and cost-attribution fields remain internal.
- [ ] Closed-schema output validation, single-gallery isolation, non-conforming-output rejection, and the manual fallback are tested.
- [ ] Image-mediated prompt injection is tested as a possible input risk; the closed schema, tool-less boundary, minimized inputs, isolation, and rejection path are mitigations, not proof of impossibility.
- [ ] Per-gallery and monthly cost ceilings are configured and observable, and the initial-cost projection is not represented as the architecture's capacity limit.

## 3. Infrastructure and deployment

The deployment is rehearsed, not improvised on the day.

- [ ] `staging` deploy procedure ([`deployment.md`](deployment.md) §3) has been exercised end-to-end.
- [ ] `production` deploy procedure has been exercised at least once with a no-op release before opening to photographers.
- [ ] Rollback procedure ([`deployment.md`](deployment.md) §4) has been exercised end-to-end; rollback time measured and within 30 minutes.
- [ ] Secrets are in the deployment platform's managed secret store ([`deployment.md`](deployment.md) §2) — none committed to the repository, verified by a secret scanner pre-commit hook.
- [ ] Backups configured per [`deployment.md`](deployment.md) §7; recovery test passed within the last quarter.
- [ ] Observability dashboards ([`deployment.md`](deployment.md) §5) are populated and read by the on-call founder.
- [ ] Object-storage lifecycle deletion and the idempotent application-owned database purge are active before any real client photo is admitted.
- [ ] Opaque deletion tombstones are retained outside database snapshot lineage until every capable snapshot expires.
- [ ] A restore applies tombstones and current-time expiry before promotion or traffic; any failure blocks promotion and is observable.

## 4. Security

A security pass has been done — not aspirationally, actually.

- [ ] Security review against the project's threat model has been completed ([`tasks.md`](tasks.md) D4).
- [ ] Photographer authentication works for the supported flows (signup, login, password reset).
- [ ] Client surface is unauthenticated and scoped strictly to the delivery-link token (no other route exposes client photos).
- [ ] No `Critical` or `High` `Open` issue at launch ([`known-issues.md`](known-issues.md)).
- [ ] Logs do not contain image bytes, photographer identity, client identity, or AI provider's raw responses for individual frames ([`deployment.md`](deployment.md) §5; [`intelligence-layer.md`](intelligence-layer.md) §4).
- [ ] Third-party dependencies are at supported versions; no known-vulnerable versions.
- [ ] AI boundary unit tests pass: input allow-list, output schema validation, single-gallery batch-scope, no cross-photographer context.

## 5. Privacy and legal readiness

The controls are illustrative design measures, not compliance conclusions.

- [ ] Qualified, jurisdiction-specific review has determined the applicable regimes and required privacy notices, terms, consent, retention, deletion, subprocessor, and consumer treatment.
- [ ] Every artifact required by that review is current and linked from the required product surfaces.
- [ ] The AI provider, object-storage provider, and transactional-email provider are disclosed wherever the review requires.
- [ ] The 90-day storage/database deletion, tombstone retention, and restore-before-promotion controls in §3 are verified.
- [ ] Any photographer-deletion request process required by the review is documented and rehearsed with synthetic data.

## 6. Communications

The launch reaches the right people in a way that lets them succeed.

- [ ] Landing page or first-impression surface is live (a single-page site is sufficient for v1).
- [ ] Five real pilot photographers have been recruited with appropriate consent and confirmed they will deliver one full gallery within the first two weeks ([`mvp-scope.md`](mvp-scope.md) §4); this synthetic example claims no existing cohort.
- [ ] Support channel is named in the product (an email address is sufficient for v1) and the founder commits to a 24-hour response window during launch.
- [ ] First 24-hour response plan is agreed: founder watches the dashboards, responds to support emails, no shipping unrelated changes.

## 7. Metrics

The project will know, on the day, whether the launch worked.

- [ ] Activation metric (photographer time-from-upload-to-delivery-link-sent) is defined ([`mvp-scope.md`](mvp-scope.md) §4) and instrumented; dashboard renders the number.
- [ ] Client decide-time metric (delivery-link-opened-to-finalized) is instrumented; dashboard renders.
- [ ] AI override rate is instrumented at the per-gallery and per-photographer level ([`intelligence-layer.md`](intelligence-layer.md) §5).
- [ ] Failure metrics ([`mvp-scope.md`](mvp-scope.md) §5: photographers stop uploading after 1–2 galleries or clients revert to "you pick") are named in advance and watched; separately, DEC-8's sole first-iteration trigger is override rate >50% sustained across at least three photographers in one calendar week.
- [ ] Success and failure thresholds are stated in advance: < 15 min photographer-time, < 5 day client-decide-time, ≥ 3 of 5 photographers say they would not go back.
- [ ] Dashboard exists where the founder reads activation, client decide-time, and override rate within minutes.

## 8. Operations and on-call

The first hours after launch are owned, not improvised.

- [ ] On-call is staffed for the launch window: founder pages on Severity-1 ([`deployment.md`](deployment.md) §6).
- [ ] Severity definitions and response loop are documented ([`deployment.md`](deployment.md) §6).
- [ ] At least one practiced incident drill has happened (forced AI provider outage in `staging` — see [`tasks.md`](tasks.md) C3).
- [ ] A status communication channel is identified (founder posts to a known location — Twitter / personal blog / email — when an incident is in progress).

## 9. Decisions and open questions

Every launch-affecting decision is logged, and every blocker is named.

- [ ] Every unresolved accepted-decision dependency is satisfied, including the later provider-selection entry required by DEC-4 and DEC-11.
- [ ] No `Critical` or `High` `Open` item remains in [`known-issues.md`](known-issues.md); a hard gate cannot be passed by merely noting a mitigation.
- [ ] Post-launch iteration routing preserves DEC-8: the first Stage-13 trigger is override rate above 50% sustained across at least three photographers in one calendar week; missed timing targets and incidents remain operating signals, not alternate accepted triggers.
- [ ] The founder accepts launch readiness explicitly and records the acceptance in [`decisions.md`](decisions.md).

---

## Optional sections

### A. Marketing assets

Single-page landing site that names the product, the wedge, the target audience (solo full-time freelance photographers), and a "request access" mailto link or simple form. No paid ads, no PR push at launch. Five photographers pre-committed by personal outreach are sufficient for v1.

### B. Legal and contracts

No legal artifact is pre-decided by this example. Qualified, jurisdiction-specific review determines whether privacy notices, terms of service, consent, deletion handling, subprocessor disclosures, consumer terms, or other treatment is required before a real launch.

### C. Post-launch monitoring rota

For the first seven days post-launch, the founder watches the dashboards twice daily (morning + late afternoon) and responds to support emails within 24 hours. Day 8–14 transitions to a once-daily rhythm. After day 14, the launch is no longer "the launch" — it is operations, and the regular cadence in [`deployment.md`](deployment.md) §6 applies.

### D. Rollback decision tree

- If the issue is a regression isolated to the most recent release **and** no client selections have been accepted under the new schema → roll back immediately.
- If client selections have been accepted under a new schema → forward-fix; rollback would lose data. The forward-fix is time-boxed to one hour; if not solvable, the founder accepts limited downtime over data loss.
- If the issue is a privacy or retention regression → immediately contain the affected processing and preserve storage lifecycle, database purge, and tombstone enforcement. Roll back only when doing so cannot hide or lose accepted selections or reactivate expired data; otherwise keep traffic blocked and forward-fix under containment. Data integrity and deletion enforcement take precedence over continuity.
