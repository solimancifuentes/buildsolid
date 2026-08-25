# Photographer SaaS — Tasks

Discrete, verifiable work units that turn [`plan.md`](plan.md) into a buildable backlog. Tasks are organized by phase. Each task is small enough for a single agent session and is reviewed against [`plan.md`](plan.md), [`spec.md`](spec.md), and the project's principles.

This is a BuildSolid v0.1 reference example. Per [`README.md`](README.md) §1, the example stops at the artifact level — these tasks describe the *would-build* backlog. They are not executed in this example.

Workflow phase: **Phase 8 — Task Breakdown.** Driving skill: `task-breakdown`.

Governing artifacts (highest applicable authority first):

1. [`decisions.md`](decisions.md) — accepted choices and clarifications.
2. [`spec.md`](spec.md) — reconciled product contract.
3. [`plan.md`](plan.md) — implementation order.

If they conflict, stop and reconcile the lower-authority artifact; do not execute the conflict.

---

## How to read this file

Each task uses this shape:

```
### <ID> — <Title>
**Description:** what the task does and why.
**Files:** the files created or modified.
**Inputs:** what the agent must read before starting.
**Acceptance:** the verifiable outcome.
**Status:** Not started / In progress / Blocked / Done.
**Parallelizable:** yes / no / yes-after-<ID>.
**Review:** which Checkpoint or review gate applies (plan §9).
**Dependencies:** task IDs that must be accepted first.
```

Phase letters mirror [`plan.md`](plan.md) §5: A = Plumbing, B = Manual loop, C = Intelligence layer, D = Pre-launch hardening, E = Launch.

**Default rules every task inherits:**

- The project's [`spec.md`](spec.md) governs scope; non-goals from [`non-goals.md`](non-goals.md) hold throughout.
- Task `Status` uses only these values: `Not started`, `In progress`, `Blocked`, or `Done`.
- In a downstream Build-mode implementation, continue accepted reversible work and ask only when blocked, but stop for missing authority, safety context, or a consequential action; this artifact-only example does not enter Build Mode.
- When a task lacks the human's preference, intent, or decision context that cannot be safely inferred, it must ask — using whatever clarification tooling the harness provides, with plain inline questioning as the agent-neutral fallback.
- Routine test, review, deployment, and remediation results belong in task, review, pull-request, or change provenance. Add a decision only for a meaningful accepted choice, exception, deferral, or tradeoff.
- Irreversible or high-impact actions (provisioning live infra, configuring a real DNS record, sending real client email, deleting any data) require explicit human confirmation regardless of mode.
- Until D1 is `Done`, every upload, scoring, eval, rehearsal, and restore exercise uses synthetic fixtures; no real client photo is admitted.
- No provider call occurs until C1's later-entry dependency is accepted. Thereafter only downscaled JPEG bytes plus opaque frame IDs cross the boundary.
- C1 is `Blocked` by its direct missing provider decision; dependent C2–C5 remain `Not started` until their prerequisites are accepted.

---

## Phase A — Plumbing

### A1 — Project scaffold and deploy pipeline

**Description:** Initialize the source repository for the would-build (web client, API service, ops). Stand up a minimal deploy pipeline that takes `main` to staging.
**Files:** `client/`, `api/`, `ops/` skeletons; CI configuration.
**Inputs:** [`plan.md`](plan.md) §4, §5 Phase A.
**Acceptance:** an empty client renders, an empty API responds to `/health`, and a push to `main` deploys to staging.
**Status:** Not started.
**Parallelizable:** no (foundational).
**Review:** Checkpoint A.
**Dependencies:** none.

### A2 — Photographer signup and login

**Description:** Email + password signup and login. No team setup, no profile, no SSO. Standard password reset by email.
**Files:** `api/auth/*`, `client/auth/*`.
**Inputs:** [`spec.md`](spec.md) §7 (signup capability), [`design.md`](design.md) tone-and-voice rules.
**Acceptance:** a new photographer can sign up, log out, log back in, and reset their password — all on staging.
**Status:** Not started.
**Parallelizable:** yes-after-A1.
**Review:** Checkpoint A.
**Dependencies:** A1.

### A3 — Photographer dashboard skeleton

**Description:** Render the dashboard screen ([`design.md`](design.md) §3 Screen 1) for a logged-in photographer with an empty-state message.
**Files:** `client/dashboard/*`, `api/galleries/*` (read endpoint with empty result).
**Inputs:** [`design.md`](design.md) §3 Screen 1, §3 cross-screen patterns.
**Acceptance:** a logged-in photographer sees the dashboard with the empty-state copy from [`design.md`](design.md) Optional D.
**Status:** Not started.
**Parallelizable:** yes-after-A2.
**Review:** Checkpoint A.
**Dependencies:** A2.

### A4 — Object-storage integration with signed URLs

**Description:** Connect the API to S3-compatible object storage. Mint signed PUT URLs for photographer uploads and signed GET URLs for the client view.
**Files:** `api/storage/*`.
**Inputs:** [`architecture.md`](architecture.md) §3 (Object storage), §6 (decisions).
**Acceptance:** a test upload via signed URL succeeds; a test signed GET retrieves the same bytes; no public-read URLs are minted.
**Status:** Not started.
**Parallelizable:** yes-after-A1.
**Review:** Checkpoint A.
**Dependencies:** A1.

### A5 — Application data store schema baseline

**Description:** Provision the relational data store and create the schema for the seven application-data entities in [`architecture.md`](architecture.md) §4. The external retention-control `DeletionTombstone` is not in that database schema and is added under D1.
**Files:** `api/data/migrations/*`.
**Inputs:** [`architecture.md`](architecture.md) §4.
**Acceptance:** schema exists in staging; all seven application-data entities can be inserted and queried with stub data; no tombstone is stored in the database snapshot lineage.
**Status:** Not started.
**Parallelizable:** yes-after-A1.
**Review:** Checkpoint A.
**Dependencies:** A1.

### A6 — Golden-set labeling kickoff (parallel work)

**Description:** In a future real implementation, assemble a rights-cleared 300-frame golden set independent of this example's synthetic research corpus; label keeper/non-keeper and dominant reason.
**Files:** `ops/golden-set/index.csv` (filenames + labels); the image bytes themselves are stored separately and not committed.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §5.
**Acceptance:** 300 frames are labeled; source rights and required participant consent are documented; no claim is made that the example already has this set.
**Status:** Not started.
**Parallelizable:** yes (runs in parallel with A2–A5 and Phase B).
**Review:** Checkpoint C precursor.
**Dependencies:** none structural; needs founder time.

---

## Phase B — Manual loop end-to-end

### B1 — Gallery upload from a folder of JPEGs

**Description:** Implement the photographer's upload step. Drop a folder, persist Image rows, store bytes via signed PUT URLs (A4), generate thumbnails.
**Files:** `client/upload/*`, `api/galleries/upload/*`.
**Inputs:** [`design.md`](design.md) §3 Screen 2, [`architecture.md`](architecture.md) §4.
**Acceptance:** using a generated or otherwise rights-cleared synthetic 600-JPEG fixture, every Image row is persisted, thumbnails render, and upload resumes after a network blip.
**Status:** Not started.
**Parallelizable:** no.
**Review:** Checkpoint B.
**Dependencies:** A2, A3, A4, A5.

### B2 — Photographer review-and-mark UI (no AI)

**Description:** Build Screen 2's review surface with no AI suggestions yet. The photographer can mark each image `kept` or `rejected`; this manual state is independent of the later closed-vocabulary suggestion reasons.
**Files:** `client/review/*`, `api/photographer-overrides/*`.
**Inputs:** [`design.md`](design.md) §3 Screen 2, §4 cross-screen patterns.
**Acceptance:** a photographer can mark every image in a 600-frame gallery; per-image kept/rejected state persists across reload; the "send delivery link" action becomes available once review is complete.
**Status:** Not started.
**Parallelizable:** yes-after-B1 (UI + state persistence are independent of upload internals).
**Review:** Checkpoint B.
**Dependencies:** B1.

### B3 — Delivery-link minting and sending

**Description:** Mint a high-entropy delivery-link token; let the photographer copy/share it. No client-account requirement; optional expiry.
**Files:** `api/delivery-links/*`, `client/share/*`.
**Inputs:** [`spec.md`](spec.md) §7 (delivery link), [`architecture.md`](architecture.md) §3 (boundary).
**Acceptance:** a photographer can mint a link for a reviewed gallery; opening the link in a fresh, unauthenticated session loads the gallery (B4 dependency); the link can be revoked.
**Status:** Not started.
**Parallelizable:** yes-after-B2.
**Review:** Checkpoint B.
**Dependencies:** B2.

### B4 — Client delivery view (default-keepers + show-all)

**Description:** Build Screen 3. Default view shows the photographer's `kept` subset; "Show all" expands to every image; star/favorite toggle per image; explicit "Finalize selections" action.
**Files:** `client/client-view/*`.
**Inputs:** [`design.md`](design.md) §3 Screen 3, [`user-journeys.md`](user-journeys.md) §1.
**Acceptance:** a client (unauth) opens the link, sees the kept subset by default, can expand, can favorite, can finalize; finalize is a single explicit action.
**Status:** Not started.
**Parallelizable:** yes-after-B3.
**Review:** Checkpoint B.
**Dependencies:** B3.

### B5 — Client selection capture

**Description:** Persist client favorites; on finalize, lock the selection set against further changes from this delivery link.
**Files:** `api/selections/*`.
**Inputs:** [`architecture.md`](architecture.md) §4 (Selection entity).
**Acceptance:** favorites persist across client reloads; finalize sets `finalized = true` and prevents further toggles via the same link.
**Status:** Not started.
**Parallelizable:** yes-after-B4.
**Review:** Checkpoint B.
**Dependencies:** B4.

### B6 — Photographer notification on client finalize

**Description:** Send a transactional email to the photographer when a client finalizes a delivery link.
**Files:** `api/notifications/*`.
**Inputs:** [`spec.md`](spec.md) §7, [`architecture.md`](architecture.md) §5 (transactional email).
**Acceptance:** when a test gallery is finalized, the photographer's email address receives a single email within 60 seconds; no email is sent for non-finalize events.
**Status:** Not started.
**Parallelizable:** yes-after-B5.
**Review:** Checkpoint B.
**Dependencies:** B5.

### B7 — Photographer dashboard live status

**Description:** Hook the dashboard up to live gallery state; show the seven statuses ([`design.md`](design.md) §3 Screen 1) per gallery, including the `stalled` state after 14 days without client finalization.
**Files:** `client/dashboard/*`, `api/galleries/list/*`.
**Inputs:** [`mvp-scope.md`](mvp-scope.md) §2, [`design.md`](design.md) §3 Screen 1, §4 status vocabulary, [`spec.md`](spec.md) §10 Product.
**Acceptance:** the dashboard shows correct status per gallery in real time after each loop step (`uploading` → `suggesting` → `review` → `sent` → `open` → `finalized`); a sent/open gallery with no finalization after 14 days appears as `stalled` with manual re-share available; no automated client reminder is sent.
**Status:** Not started.
**Parallelizable:** yes-after-B5.
**Review:** Checkpoint B.
**Dependencies:** B5.

### B8 — Finalized-selections view + CSV export

**Description:** Screen 4 (finalized view) plus a CSV export of picked filenames per [`plan.md`](plan.md) §3 Q3.
**Files:** `client/finalized/*`, `api/selections/export/*`.
**Inputs:** [`design.md`](design.md) §3 Screen 4.
**Acceptance:** the photographer sees picks in a dense grid; CSV download contains exactly the picked filenames, no AI labels.
**Status:** Not started.
**Parallelizable:** yes-after-B5.
**Review:** Checkpoint B.
**Dependencies:** B5.

---

## Phase C — Intelligence layer plugged in

### C1 — Model-call boundary with input allow-list and output schema validation

**Description:** After provider selection, build the boundary that sends downscaled JPEG bytes plus opaque per-frame IDs only; reject non-conforming output and strip every identifying, filename, metadata, gallery, and cost-attribution field.
**Files:** `api/ai/boundary/*`.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §2, §4, §7; [`architecture.md`](architecture.md) §8.
**Acceptance:** tests prove the literal allow-list, one-gallery isolation, no tools or outbound callbacks, schema rejection/manual fallback, and image-mediated prompt injection as a possible risk bounded by the accepted mitigations.
**Status:** Blocked.
**Parallelizable:** yes-after-A4 (storage), A5 (data store).
**Review:** Checkpoint C.
**Dependencies:** A4, A5, and the later append-only accepted provider entry required by DEC-4/DEC-11.

### C2 — Per-frame scoring at upload time

**Description:** After upload, run the scoring pass for every frame; persist Suggestion rows; surface AI pre-marks on Screen 2.
**Files:** `api/ai/scoring/*`, `client/review/*`.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §2, [`design.md`](design.md) §3 Screen 2 + Optional E.
**Acceptance:** a 600-frame upload completes scoring within 5 minutes wall time on staging; pre-marks render on Screen 2 with the reason label visible; photographer overrides persist independently of AI output.
**Status:** Not started.
**Parallelizable:** yes-after-C1, B2.
**Review:** Checkpoint C.
**Dependencies:** C1, B2.

### C3 — Fallback path when scoring fails

**Description:** When the AI provider is unavailable, times out, or returns non-conforming output, fall through to a manual-mark experience; move the gallery from `suggesting` to the canonical `review` status and mark affected per-image scoring state `not-scored`.
**Files:** `api/ai/scoring/*`, `client/review/*`.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §2 Fallbacks, §3.
**Acceptance:** a forced provider outage in staging produces a usable, no-pre-marks gallery within 60 seconds; the loop still completes; the fallback event is logged.
**Status:** Not started.
**Parallelizable:** yes-after-C2.
**Review:** Checkpoint C.
**Dependencies:** C2.

### C4 — Cost-ceiling enforcement

**Description:** Implement per-gallery and per-photographer-per-month cost ceilings at the model-call boundary; throttle by sampling within near-duplicate clusters when a ceiling is approached.
**Files:** `api/ai/cost/*`.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §6, [`architecture.md`](architecture.md) §7.
**Acceptance:** a synthetic gallery designed to exceed $0.20 of scoring cost is throttled to ≤ $0.20; the throttle behavior is tested and observable; per-photographer monthly cost is alerted at the $5.00 ceiling.
**Status:** Not started.
**Parallelizable:** yes-after-C2.
**Review:** Checkpoint C.
**Dependencies:** C2.

### C5 — Eval harness against the 300-frame golden set

**Description:** Build the eval harness that runs the current model + policy against the golden set (A6) and reports precision/recall on the keeper label and the per-reason confusion matrix.
**Files:** `ops/evals/*`.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §5, [`plan.md`](plan.md) §3 Q2 (threshold).
**Acceptance:** a single command runs the complete 300-frame eval and produces a report; the complete report shows precision ≥ 0.80 and recall ≥ 0.70 on the keeper label before the launch gate, with the per-reason matrix attached. A partial run cannot complete C5 or pass Checkpoint C.
**Status:** Not started.
**Parallelizable:** yes-after-A6, C2, D1.
**Review:** Checkpoint C.
**Dependencies:** A6, C2, D1. A6 may source and label the rights-cleared set outside the product system, but C5 may not admit or evaluate those real images until D1's retention/restore controls are `Done`.

---

## Phase D — Pre-launch hardening

### D1 — 90-day retention enforcement

**Description:** Activate the 90-day object-storage lifecycle and one provider-neutral daily trigger that invokes an idempotent application-owned database purge. Write opaque deletion tombstones outside database snapshot lineage and apply them with current-time expiry before any restore is promoted.
**Files:** `api/retention/*`, `ops/storage-lifecycle/*`, and restore/promotion safeguards.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §4; [`architecture.md`](architecture.md) §6 / §7; [`decisions.md`](decisions.md) DEC-5 and DEC-12.
**Acceptance:** controls are active before any real photo is admitted; an expired synthetic gallery is absent from storage and the data store; extensions are honored; tombstones outlive every capable snapshot; restore promotion blocks unless tombstones and current-time expiry succeed; failures are observable.
**Status:** Not started.
**Parallelizable:** yes-after-A4, A5.
**Review:** Checkpoint D.
**Dependencies:** A4, A5.

### D2 — Qualified legal/privacy review and required public artifacts

**Description:** Obtain qualified, jurisdiction-specific review to determine applicable regimes and required notices, terms, consent, retention, deletion, subprocessor, consumer, and related treatment; implement and link exactly what that review requires.
**Files:** the review record plus every product-facing legal/privacy artifact and link that review requires.
**Inputs:** [`intelligence-layer.md`](intelligence-layer.md) §4, [`launch-checklist.md`](launch-checklist.md) §5, [`decisions.md`](decisions.md) DEC-4 and DEC-11.
**Acceptance:** review is documented; every required artifact and treatment is implemented and linked; the selected provider is named wherever required.
**Status:** Not started.
**Parallelizable:** yes-after-D1.
**Review:** Checkpoint D.
**Dependencies:** D1, C1.

### D3 — Observability dashboards

**Description:** Stand up the dashboards for the signals named in [`deployment.md`](deployment.md) §5 and [`intelligence-layer.md`](intelligence-layer.md) Optional E (per-route latency, error rate, AI scoring latency, override rate, fallback rate, monthly cost).
**Files:** `ops/dashboards/*`.
**Inputs:** [`deployment.md`](deployment.md) §5, [`intelligence-layer.md`](intelligence-layer.md) Optional E.
**Acceptance:** every signal in those references is read off a dashboard within 30 seconds of generating a synthetic event in staging.
**Status:** Not started.
**Parallelizable:** yes-after-C2.
**Review:** Checkpoint D.
**Dependencies:** C2.

### D4 — Security review (AI/image boundary + conventional appsec)

**Description:** Run the risk-first security pass: review the AI/image/data boundary first, then conventional application security. Both surfaces must pass before readiness.
**Files:** ordinary review/change provenance; persistent failures added to [`known-issues.md`](known-issues.md); a decision only for a meaningful accepted choice, exception, or tradeoff.
**Inputs:** [`spec.md`](spec.md) §10 Quality, [`intelligence-layer.md`](intelligence-layer.md) §7.
**Acceptance:** review complete; no `Critical` or `High` `Open` issues at conclusion; AI boundary tests pass.
**Status:** Not started.
**Parallelizable:** yes-after-C5, D1.
**Review:** Checkpoint D.
**Dependencies:** C5, D1.

### D5 — Load rehearsal

**Description:** Run a staging load rehearsal with five concurrent active photographers each uploading a 600-frame gallery; capture latency and AI scoring time; verify they meet [`architecture.md`](architecture.md) §7 targets.
**Files:** ordinary review/change provenance; persistent failures added to [`known-issues.md`](known-issues.md); a decision only for a meaningful accepted choice, exception, or tradeoff.
**Inputs:** [`architecture.md`](architecture.md) §7.
**Acceptance:** targets met; if not met, fix lands or a documented mitigation is recorded.
**Status:** Not started.
**Parallelizable:** yes-after-C2.
**Review:** Checkpoint D.
**Dependencies:** C2.

### D6 — Launch checklist walkthrough

**Description:** Walk every item in [`launch-checklist.md`](launch-checklist.md) §1–§9; check the boxes that are true; record blockers for the rest in [`known-issues.md`](known-issues.md) with a fix plan.
**Files:** outcome reflected in [`launch-checklist.md`](launch-checklist.md), blockers recorded.
**Inputs:** [`launch-checklist.md`](launch-checklist.md).
**Acceptance:** every required item is checked; no provider, retention/restore, security, legal, or real-data blocker is merely waived by mitigation; founder acceptance follows the evidence.
**Status:** Not started.
**Parallelizable:** no.
**Review:** Checkpoint D.
**Dependencies:** D1, D2, D3, D4, D5.

---

## Phase E — Launch

### E1 — Onboard five photographers and run the loop

**Description:** In a future real implementation, onboard a properly consented five-photographer cohort after all D6 gates. Each delivers at least one full gallery through the MVP within two weeks. Watch the metrics in [`mvp-scope.md`](mvp-scope.md) §4.
**Files:** task/review/change provenance and [`changelog.md`](changelog.md); persistent issues recorded in [`known-issues.md`](known-issues.md); a decision only for a meaningful accepted choice.
**Inputs:** [`mvp-scope.md`](mvp-scope.md) §4, [`launch-checklist.md`](launch-checklist.md).
**Acceptance:** the properly consented cohort meets the prospective thresholds in [`mvp-scope.md`](mvp-scope.md) §4; this reference example records no result.
**Status:** Not started.
**Parallelizable:** no.
**Review:** Checkpoint E.
**Dependencies:** D6.

### E2 — Post-launch first-week monitoring

**Description:** Watch the dashboards for the first seven days post-launch; respond to any `Severity-1` incident; record observed behavior vs. expected.
**Files:** task/review/change provenance; persistent issues recorded in [`known-issues.md`](known-issues.md); a decision only for a meaningful accepted choice.
**Inputs:** [`launch-checklist.md`](launch-checklist.md) Optional C.
**Acceptance:** seven days complete; no unresolved `Critical` issue; founder records a one-paragraph summary of what worked and what did not.
**Status:** Not started.
**Parallelizable:** no.
**Review:** Checkpoint E (final).
**Dependencies:** E1.

---

## Task index

| Phase | Count |
|---|---|
| A — Plumbing | 6 |
| B — Manual loop | 8 |
| C — Intelligence layer | 5 |
| D — Pre-launch hardening | 6 |
| E — Launch | 2 |
| **Total** | **27** |

The total is intentionally small. If the backlog or time projection grows materially, stop for scope requalification. Adding or removing a required capability needs the owning artifacts and an accepted decision updated first; this example defines no automatic cut order.

At this reference stop point, C1 is `Blocked` by the missing provider entry and the other 26 tasks are `Not started`; none is `In progress` or `Done`.
