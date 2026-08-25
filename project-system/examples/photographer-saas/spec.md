# Photographer SaaS — Product Specification

Project-level product spec for the photographer SaaS reference example: what this v1 is, who it serves, and what must be true for it to ship. The spec is the contract any future implementation task is checked against.

This is a BuildSolid v0.1 reference example. Per [`README.md`](README.md) §1, this spec defines the v1 the example *would* ship; the example itself stops at the artifact level and produces no real implementation.

> The scenario, research corpus, people, measurements, permissions, galleries, eval data, and outcomes are synthetic and illustrative. Every implementation, provider selection, real-data use, legal conclusion, deployment, and live result below remains future downstream work.

Workflow phase: **Phase 7 — Spec Creation.** Driving skill: `spec-planner`.

Related artifacts: [`founder-intent.md`](founder-intent.md), [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md), [`user-journeys.md`](user-journeys.md), [`design.md`](design.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`plan.md`](plan.md), [`tasks.md`](tasks.md), [`decisions.md`](decisions.md).

---

## 1. Overview

The photographer SaaS is a minimalist delivery platform for solo, full-time freelance photographers. It accepts a folder of edited JPEGs from a shoot, runs an AI image-suggestion pass that pre-marks the best frames (sharpness, expression, composition, near-duplicate culling), lets the photographer review and override, sends a private delivery link to the client, captures the client's selections, and notifies the photographer when the client finalizes. v1 is the smallest version of that loop that proves the photographer's time-to-delivered-gallery drops by at least half ([`product-thesis.md`](product-thesis.md) §1).

## 2. Target users

The direct user is a **solo, full-time freelance photographer** delivering 5–40 galleries per month, event-and-portrait shaped (weddings, portraits, branded shoots). The indirect user is the **client receiving the gallery**, who interacts with the product through an unauthenticated delivery link.

- **Photographer (primary).** Authenticated; owns galleries; reviews AI suggestions; sends delivery links; sees finalized selections.
- **Client (secondary).** Unauthenticated; opens a delivery link; sees the photographer's reviewed subset by default; selects favorites; finalizes.

## 3. User problems

Drawn from [`problem-statement.md`](problem-statement.md):

- Photographers lose two-to-four hours per shoot to manual pre-cull of near-duplicate / clearly-not-keeper frames before delivery.
- Photographers wait five-to-fourteen calendar days for clients to make selections, with no in-product mechanism to compress that time.
- Existing gallery tools host photos but do not reduce photographer time-to-delivered-gallery.
- Existing AI-cull tools live as desktop apps and do not connect to client delivery, leaving the photographer to glue the loop by hand.
- Photographers reject AI culls that override their style, so the AI must surface suggestions, not verdicts.

## 4. Goals

- **G1.** Ship the seven thesis-bearing capabilities from [`mvp-scope.md`](mvp-scope.md) §2 plus the three required enabling controls in §7: photographer auth, filenames-only CSV export, and retention/restore enforcement.
- **G2.** In a future downstream implementation, walk the primary journey on a properly consented real gallery only after retention, provider, and required legal gates pass; this example records no such walkthrough.
- **G3.** Enforce the minimized provider boundary and the 90-day storage/database purge, external tombstones, and restore-before-promotion controls in DEC-11/DEC-12.
- **G4.** Use the illustrative future-pilot thresholds in [`mvp-scope.md`](mvp-scope.md) §4; this synthetic example claims no achieved metric.
- **G5.** Hold the initial-launch projection for ≤10 active photographers under $200/month; do not confuse that budget with the separate technical-capacity envelope.
- **G6.** Honor every non-goal in [`non-goals.md`](non-goals.md); a feature outside that envelope is not added without a decision recorded.

## 5. Non-goals

Mirrors [`non-goals.md`](non-goals.md), restated in spec form:

- No print or digital sales storefront.
- No watermarking or per-image rights management UI.
- No client comments / feedback threads.
- No multi-shooter or team collaboration.
- No Lightroom / Capture One plugin in v1.
- No native mobile apps.
- No client-side reminders / nudging.
- No marketplace, photographer directory, or community feed.
- No on-device AI inference, no per-photographer fine-tune, no custom model training.
- No public API.
- No auto-retouch, auto-color, or generative edits.
- No use of client photos for AI training.

## 6. User journeys

See [`user-journeys.md`](user-journeys.md):

- Primary journey — **Deliver → Select → Finalize** ([`user-journeys.md`](user-journeys.md) §1).
- No secondary or third journey in v1; signup / login is plumbing, not a journey.

## 7. Required capabilities

The capabilities the system must provide for the goals to be met. The list bridges from problems (§3) to tasks ([`tasks.md`](tasks.md)).

- **Photographer signup / login** — minimum-viable email + password, no team setup.
- **Gallery creation from a folder of JPEG uploads** — drag-and-drop or click; resilient to network blips during upload.
- **AI image-suggestion pass at upload time** — per-frame score + label set ([`intelligence-layer.md`](intelligence-layer.md) §2); fallback to no-pre-marks on failure.
- **Photographer review-and-override UI** — per-image accept / reject with the suggestion reason visible.
- **Delivery link minting and sending** — high-entropy token, unauthenticated client access, optional expiry.
- **Client selection capture** — favorite / final-pick toggles, single explicit "Finalize" action.
- **Photographer notification on client finalize** — transactional email; no auto-nudging the client.
- **Photographer dashboard** — one row per gallery with status and "what's blocked on whom", including `stalled` after 14 days without client finalization and a manual re-share action.
- **CSV export of finalized selections** — filenames only, for the photographer's final edit pass.
- **90-day retention enforcement** — storage lifecycle deletion plus one provider-neutral daily trigger invoking an idempotent application-owned database purge; opaque tombstones remain outside snapshot lineage and are applied with current-time expiry before any restore is promoted.

## 8. Architecture summary

A single-page web client, thin API service, S3-compatible object storage, relational data store, transactional email, and an as-yet-unselected managed AI provider. The narrow daily purge trigger does not add a general-purpose worker system. Full design lives in [`architecture.md`](architecture.md).

## 9. Intelligence layer summary

One per-frame suggestion capability behind a `Blocked` provider gate. After a later accepted entry names the provider and dates its written no-retention/no-training commitment, the boundary may send only downscaled JPEG bytes plus opaque frame IDs. Closed-schema output, no tools, single-gallery isolation, minimized inputs, rejection, and human override mitigate—but do not make impossible—image-mediated prompt injection. Full design lives in [`intelligence-layer.md`](intelligence-layer.md).

## 10. Acceptance criteria

The checklist of conditions that must all be true for v1 to ship.

**Product**

- [ ] All seven thesis-bearing capabilities plus photographer auth, filenames-only CSV export, and retention/restore enforcement work end-to-end.
- [ ] Primary journey ([`user-journeys.md`](user-journeys.md) §1) walks cleanly with no required manual intervention outside the seven steps.
- [ ] A gallery that remains unfinalized for 14 days appears as `stalled` on the photographer dashboard, with manual re-share available and no automated client reminder sent.
- [ ] Empty / loading / error states ([`design.md`](design.md) Optional D) handled for each of the four key screens.
- [ ] Photographer can revoke a delivery link.
- [ ] Photographer can extend retention beyond 90 days for a specific gallery.

**Architecture**

- [ ] System matches the four-component shape in [`architecture.md`](architecture.md) §3 (web client, API service, object storage, managed AI provider) — no extra long-running services, no public API, no native mobile.
- [ ] Every provider request contains only downscaled JPEG bytes and opaque frame IDs from one gallery; identifying, filename, metadata, and cost-attribution fields remain internal.
- [ ] Cross-gallery and cross-photographer context is prevented by tested request isolation; this is a mitigation, not an impossibility claim.
- [ ] Storage lifecycle deletion and the idempotent database purge are active before real photos; external tombstones survive capable snapshots; restores apply tombstones and current-time expiry before promotion and fail closed.

**Intelligence layer**

- [ ] A later accepted entry names the provider and dates its written no-retention/no-training commitment; C1 remains `Blocked` until then.
- [ ] The closed output vocabulary is enforced by schema validation at the model-call boundary; non-conforming outputs fall through to the manual path.
- [ ] The complete future real, rights-cleared 300-frame golden set meets DEC-6's precision/recall threshold; the example contains no such corpus or result.
- [ ] Fallbacks for scoring failure are tested and observable.
- [ ] Image-mediated prompt injection is tested as possible, with the closed schema, tool-less boundary, minimization, isolation, output rejection, and photographer override verified as mitigations.
- [ ] Per-gallery cost ceiling ($0.20) is enforced; per-month cost ceiling ($5.00 / active photographer) is alerted on.

**Quality**

- [ ] Latency targets in [`architecture.md`](architecture.md) §7 are met in a staging-load rehearsal.
- [ ] Security review passes — no high or critical issues open at launch ([`launch-checklist.md`](launch-checklist.md) §4).
- [ ] No client photo, image content, or photographer/client identifying field appears in any log line ([`intelligence-layer.md`](intelligence-layer.md) §4).

**Documentation**

- [ ] [`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md), [`spec.md`](spec.md), [`plan.md`](plan.md), [`tasks.md`](tasks.md), [`decisions.md`](decisions.md), [`changelog.md`](changelog.md), [`known-issues.md`](known-issues.md) all current at launch.
- [ ] Qualified, jurisdiction-specific review is complete and every notice, term, consent, deletion, subprocessor, consumer, or related artifact it requires is implemented and linked.

## 11. Risks

- **R1. AI suggestions feel "wrong" on a photographer's style.** The wedge is at risk when override rate exceeds 50% and is sustained across at least three photographers in one calendar week—DEC-8's sole accepted first-iteration trigger. *Mitigation:* run the complete golden-set eval before any change ships ([`intelligence-layer.md`](intelligence-layer.md) §5) and monitor the exact production signal without treating other metrics as alternate triggers.
- **R2. Client decide-time does not drop.** If clients ignore the keepers default, the client-side wedge is gone. *Mitigation:* watch the "expand to all" click-through rate; treat > 90% as a UX failure ([`user-journeys.md`](user-journeys.md) §1 failure modes).
- **R3. Provider gate cannot be satisfied.** No integration begins without the later accepted provider entry and dated written commitment; the manual loop remains available with synthetic fixtures.
- **R4. Cost ceiling breached.** Per-gallery scoring exceeds $0.20 or per-photographer monthly cost exceeds $5.00. *Mitigation:* ceiling enforced at the model-call boundary (sample within near-duplicate clusters when ceiling approached); cost alert configured ([`launch-checklist.md`](launch-checklist.md) §2).
- **R5. Future pilot adoption lower than five in two weeks.** Validation needs a properly consented real cohort. *Mitigation:* recruit only after provider, retention/restore, security, and qualified legal gates pass; do not treat synthetic personas as participants.
- **R6. Solo founder time budget overrun.** Spec scope cannot be delivered in 120–180 hours. *Mitigation:* stop for scope requalification and an accepted decision before removing any required capability; no dashboard, notification, or hard gate has a pre-authorized cut order.

## 12. Open questions

- **Q1.** Specific AI provider: unresolved; a later append-only accepted entry must name it and date the written commitment before C1 can leave `Blocked`.
- **Q2.** Eval threshold: resolved by DEC-6 (precision ≥ 0.80, recall ≥ 0.70; no per-reason hard threshold).
- **Q3.** CSV shape: resolved by DEC-7 (filenames only).

---

## Optional sections

### A. Versioning and amendments

This file is the current product contract. Accepted iterations update it and related artifacts in place, with an append-only decision and changelog entry when the decision threshold is met; do not create parallel `spec-v2` or `specs/v2/spec` files.

### B. External constraints

- Qualified, jurisdiction-specific review must determine which regimes apply and what privacy, terms, consent, deletion, subprocessor, consumer, or other treatment is required. This example reaches no legal conclusion.

### C. Out-of-scope alternatives considered

- **A studio-management platform with delivery as one of many features** — rejected because that is the Pic-Time / ShootProof shape, and the wedge is specifically *not* studio management.
- **A photographer marketplace** — rejected by [`non-goals.md`](non-goals.md) §3; the product never enters the photographer ↔ client commercial relationship.
- **An AI-cull desktop plugin** — rejected because the desktop-plugin shape is what existing AI-cull products do, and the integration with delivery is the wedge.
