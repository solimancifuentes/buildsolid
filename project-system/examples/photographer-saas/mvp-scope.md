# MVP Scope — Photographer SaaS

The smallest valuable build that proves the project's thesis. Every implementation task is checked against this file. **Minimalism is the rule** — when two options work, the smaller one wins; cut, then cut again.

> This is a wholly synthetic worked scenario. Its people, research, measurements, dates, permissions, galleries, and outcomes are illustrative hypotheses, not completed real-world evidence.

Workflow phase: **Phase 3 — MVP Scope.** Driving skill: `mvp-scope` (paired with [`non-goals.md`](non-goals.md) to lock the cuts).

Related artifacts: [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`non-goals.md`](non-goals.md), [`user-journeys.md`](user-journeys.md), [`spec.md`](spec.md).

---

## 1. The thesis the MVP must prove

The smallest thing that proves a freelance photographer's time-to-delivered-gallery drops by at least half, and a client's decide-time drops materially, when AI image suggestion is built into the delivery loop instead of bolted on as a desktop tool.

## 2. In scope (must-haves)

- **Gallery upload from a local folder of edited JPEGs** — required because the photographer's loop starts at "edited", not "raw", and the product must accept the file form they already produce.
- **AI image-suggestion pass at upload time** — required because the wedge in [`product-thesis.md`](product-thesis.md) is AI-pre-marked favorites; without this, the product is just another hosted gallery.
- **Photographer review-and-override UI for the AI's suggestions** — required because [`discovery.md`](discovery.md) §3 Theme 5 says photographers reject AI that overrides their taste; the photographer must remain the decision-maker.
- **Client delivery link that defaults to the photographer-reviewed keeper subset, with an "expand to all" affordance** — required because the prospective "show keepers first" behavior is the hypothesis intended to shorten client decide-time (H3 in [`discovery.md`](discovery.md) §5).
- **Client selection capture (favorite / final-pick toggles)** — required because the loop only closes when the photographer can see what the client picked.
- **Photographer notification when a client finalizes selections** — required because chasing-by-email is one of the per-gallery frictions in [`problem-statement.md`](problem-statement.md) §2; without this, the photographer is back to nudging.
- **Photographer dashboard with one row per gallery (status: uploading / suggesting / review / sent / open / finalized / stalled)** — required so the photographer can see at a glance which galleries are blocked on them vs. blocked on the client, including a manual re-share action when a client has not finalized after 14 days.

That is seven items. Anything more is suspect.

## 3. Explicit cuts (would-be-nice, deferred)

- **Print/digital sales storefront** — cut because [`non-goals.md`](non-goals.md) excludes commercial mechanics in the MVP; this is what Pic-Time and ShootProof bundle, and bundling it dilutes the wedge.
- **Watermarking and download-permission tiers** — cut because per-image rights-management UI is not load-bearing for the thesis. A real project must establish its own rights and contract treatment through qualified review.
- **Multi-shooter / second-photographer collaboration** — cut because the audience is *solo* freelance photographers (`product-thesis.md` §3); collaboration is a different product.
- **Client comments / feedback threads** — cut because the worked scenario treats selection, not discussion, as the bottleneck.
- **Lightroom / Capture One plugin integration** — cut because building a desktop integration is a separate engineering surface; manual export → upload is acceptable for v1, and the cost of the integration cannot be justified before the loop itself is proven.
- **Style-specific weighting by shoot type** — cut. DEC-1's body, clarified by DEC-11, selects one neutral scorer across the MVP's event-and-portrait shoot types; wedding-, portrait-, and brand-specific weighting remains deferred and is reconsidered only if DEC-8's trigger fires.
- **Mobile native apps for photographer or client** — cut because the worked scenario assumes desktop or tablet use and treats responsive web as sufficient for the initial test.
- **Email reminders to the client** — cut because nudging-by-email is the behavior the AI-pre-marked subset is meant to eliminate; a stalled gallery may expose manual re-share for the photographer, but the product must not auto-nudge the client.

## 4. Success criteria

These are future validation thresholds for a real, properly consented downstream pilot; none has been achieved by this synthetic example.

- Five participating photographers deliver at least one full gallery each within two weeks.
- Median photographer time from upload to delivery-link sent is under 15 minutes for a 600-image shoot, measured against a participant-specific baseline.
- Median client time from delivery-link opened to finalized is under five days.
- At least three of five participating photographers say in a week-three interview that they would not return to the prior workflow.
- No real client photo enters the system before the retention/restore controls are active, and no photo is sent to a provider before the provider gate is accepted.

## 5. Failure criteria

- Photographers complete the loop but say the AI suggestions are "too generic" or "wrong on my style" — indicates the AI capability did not land and the wedge collapses ([`discovery.md`](discovery.md) §3 Theme 5 risk).
- Clients revert to "can you just pick for me?" at the same rate as before — indicates the pre-marked-subset UX did not change client behavior.
- Photographers stop uploading after the first one or two galleries — indicates the loop felt like more overhead than it removed (Theme 4 risk).
- Per-gallery or per-photographer AI cost exceeds the accepted AI-cost ceiling in [`intelligence-layer.md`](intelligence-layer.md) §6.

## 6. Time and effort budget

The synthetic scenario uses an illustrative budget of **10–15 hours per week × 12 weeks** (120–180 hours); it is a planning bound, not a measured result. If a downstream build cannot fit it, stop for scope requalification before extending the budget. Any removal of a required capability needs an accepted decision and in-place artifact reconciliation; there is no pre-authorized cut order. The constitution's minimalism rule applies.

---

## Optional sections

### A. Phased path

The future downstream MVP uses two internal phases:

1. **Phase 1 — manual loop, no AI.** Exercise Upload → review → deliver → select → notify with synthetic fixtures. It may be built before provider selection, but no real client photo is admitted until the 90-day storage/database purge and restore-safe tombstone controls are active.
2. **Phase 2 — AI suggestion plugged in.** Replace the stub only after the later accepted provider entry exists and task C1 is unblocked.

This split prevents provider selection from blocking the manual loop. Moving to per-style scoring is not automatic: DEC-8's sustained override-rate threshold is the sole accepted first Stage-13 trigger.

### B. Dependencies on external systems

- **Object storage** for original and thumbnail images — fallback: any S3-compatible provider; a single-provider lock-in is a project risk and is captured in [`architecture.md`](architecture.md) §5.
- **Managed AI provider** — the specific provider is unresolved. Integration is `Blocked` until a later accepted entry names it and dates its written no-retention/no-training commitment; any future fallback must preserve the same minimized boundary.
- **Transactional email provider** for the photographer's "client finalized" notification — fallback: any SMTP provider; not load-bearing for the thesis.

### C. Explicitly deferred AI capabilities

- Auto-retouch / auto-color / generative edits — out of scope by founder anti-goal ([`founder-intent.md`](founder-intent.md) Optional B). Not deferred — *forbidden*.
- Style-specific weighting across the selected event-and-portrait shoot types — deferred; it is reconsidered only if DEC-8's accepted trigger fires.
- Learning the photographer's taste over time (per-photographer fine-tune) — deferred; the MVP uses a single neutral scoring model. A later iteration may add per-photographer adjustment.
- AI-written client emails or AI summaries of selections — out of scope; the loop closes with the photographer notification, not a generated message.
