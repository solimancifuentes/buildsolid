# User Journeys — Photographer SaaS

The few flows that actually matter for the photographer SaaS MVP. The list is short on purpose. Anything beyond what is here should be questioned against [`mvp-scope.md`](mvp-scope.md). The journeys named here drive [`design.md`](design.md), [`architecture.md`](architecture.md), and [`spec.md`](spec.md).

> This is a wholly synthetic worked scenario. Its people, research, measurements, permissions, galleries, and outcomes are illustrative; no real journey, consent, provider call, or result is claimed.

Workflow phase: **Phase 4 — UX Direction.** Driving skill: `ux-minimalist`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`mvp-scope.md`](mvp-scope.md), [`design.md`](design.md), [`spec.md`](spec.md).

---

## 1. Primary journey — Deliver → Select → Finalize

The single most important flow the MVP exists to support. If this journey works end-to-end with AI-pre-marked favorites and the metrics in [`mvp-scope.md`](mvp-scope.md) §4 land, the thesis is alive.

**User:** A solo, full-time freelance photographer (per [`product-thesis.md`](product-thesis.md) §3), and the client they are delivering a shoot to.

**Trigger:** The photographer has finished editing a shoot in Lightroom or Capture One and exported a folder of edited JPEGs. The shoot is between 200 and 2,500 images. In a future real implementation, this trigger is admitted only after D1's retention/restore controls, provider selection where applicable, rights/consent, and required legal treatment are satisfied; the worked example performs none of it.

**Goal:** Get the photographer-reviewed keeper subset into the client's hands, beginning from AI suggestions when the provider gate is satisfied, and receive the client's finalized selections back in materially less photographer-time and client-calendar-time than the photographer's prior workflow.

**Success:** The photographer sees a "finalized" status for the gallery in the dashboard, with a list of the client's picks, in less than 5 days from delivery; the photographer's own time spent in the loop (upload → review → send) is under 15 minutes for a 600-image shoot.

**Steps:**

1. *Photographer uploads* a folder of edited JPEGs into a new gallery from the dashboard.
2. *After the provider gate is accepted, system runs the AI image-suggestion pass* — only downscaled JPEG bytes and opaque frame IDs cross the provider boundary; every frame is scored for sharpness, expression, composition, and near-duplicate-of-N (see [`intelligence-layer.md`](intelligence-layer.md) §2).
3. *Photographer reviews* the pre-marked subset and records per-image `kept` or `rejected` overrides; the closed-vocabulary suggestion reason remains visible but is not rewritten as a user-authored label.
4. *Photographer sends a delivery link* to the client. The link is a private URL; no client account is required.
5. *Client opens the link*, sees the photographer-reviewed keeper subset by default, and can expand to all images if they want. The client toggles a star/favorite on each image they want; "Finalize selections" is a single explicit action.
6. *System notifies the photographer* (transactional email) that the client finalized.
7. *Photographer sees finalized selections* in the dashboard and can export the picked filenames as a list (CSV) for their final edit pass.

**Failure modes:**

- AI scoring fails or times out at upload → fall back to "no pre-marks; photographer marks by hand" rather than blocking the loop ([`intelligence-layer.md`](intelligence-layer.md) §2 Fallbacks).
- An image carries prompt-injection content → closed-schema output, no tools, minimized input, one-gallery isolation, rejection/manual fallback, and photographer override bound impact but do not make injection impossible.
- Client opens the link, sees only the pre-marked subset, and asks "where are the rest?" → the "expand to all" affordance must be obvious; if the click-through rate to "expand to all" is over 90%, the default-subset UX has not landed.
- Client never finalizes → after 14 days the dashboard surfaces the gallery as "stalled"; the photographer can manually re-share the link from the dashboard. The MVP does not auto-nudge the client (per [`non-goals.md`](non-goals.md) §1).
- Override rate exceeds 50% and is sustained across at least three photographers in one calendar week → DEC-8's sole accepted first Stage-13 trigger; start an in-place model/policy assessment.

**Where the AI layer shows up:** Step 2 (scoring at upload) and step 3 (per-frame reason labels surfaced to the photographer). Nowhere else — the AI does not write emails, does not pick for the client, and does not modify any image.

## 2. Secondary journey — *(not included)*

The MVP intentionally has only one journey. Two candidate "second journeys" were considered and folded back into the primary:

- **"Photographer revisits a delivered gallery to update selections"** is the same primary journey resumed at step 6/7; it does not require a separate flow.
- **"Photographer onboards / signs up"** is necessary plumbing but not a BuildSolid-shaped journey; the MVP keeps signup minimal (email + password, no team setup) and out of the journey list. If signup ever requires its own design effort, it would surface here.

If a second journey ever genuinely lands (for example, a Lightroom plugin flow), it would be added here only after [`mvp-scope.md`](mvp-scope.md) is updated to make it required.

## 3. Third journey — *(not included)*

No third journey. The MVP is one loop. A third journey would almost certainly indicate scope creep; if one is proposed, it must first be justified in [`mvp-scope.md`](mvp-scope.md) §2 with explicit reason it is required, and recorded in [`decisions.md`](decisions.md).

## 4. Cross-journey patterns

Because the MVP has a single journey, "cross-journey patterns" reduce to **internal consistency within the primary journey**:

- The photographer is always the decision-maker. The system surfaces suggestions and closed-vocabulary reasons; the photographer accepts or overrides the `kept`/`rejected` state without rewriting the reason label. The client is shown the photographer's *post-review* subset, not the raw AI output.
- The client never authenticates. Delivery links are private URLs with sufficient entropy; selections are tied to the link, not to a client account ([`architecture.md`](architecture.md) §4).
- Photo data remains inside the photographer → product → client flow except for the minimized provider call: downscaled JPEG bytes plus opaque frame IDs only; no identity, gallery, filename, metadata, cross-gallery context, or cost attribution crosses ([`intelligence-layer.md`](intelligence-layer.md) §4).
- Every step that could fail (scoring, email delivery, gallery upload) has an explicit fallback that keeps the loop usable, even if degraded ([`intelligence-layer.md`](intelligence-layer.md) §2 / [`architecture.md`](architecture.md) §5).

---

## Optional sections

### A. Anti-journeys

- **No "client invites another client" flow.** The product never forwards a delivery link from one client to another; the photographer owns the share boundary.
- **No "photographer browses other photographers' galleries" flow.** Galleries are private; there is no community surface ([`non-goals.md`](non-goals.md) §3).
- **No "AI generates a photo for the gallery" flow.** The AI suggests; the AI never creates ([`non-goals.md`](non-goals.md) §5).

### B. Edge-case journeys

- **Gallery export after finalization** — the photographer needs the picked filenames (as a CSV) for their final edit pass in Lightroom. Folded into step 7 of the primary journey rather than promoted to its own journey.
- **Account recovery / password reset** — necessary plumbing; standard email-based reset, not journey-shaped.

### C. Journey-level metrics

These are future measurement definitions, not observed results.

- **Photographer time-in-loop per gallery:** time from upload-start to delivery-link-sent. Target in [`mvp-scope.md`](mvp-scope.md) §4 is < 15 min for a 600-image shoot.
- **Client decide-time per gallery:** time from delivery-link-opened to finalized. Target is < 5 days median.
- **AI-suggestion override rate per gallery:** the fraction of AI-suggested frames the photographer overrides during step 3. DEC-8's sole first Stage-13 trigger is >50% sustained across at least three photographers in a calendar week ([`intelligence-layer.md`](intelligence-layer.md) §8).
