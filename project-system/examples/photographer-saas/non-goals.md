# Non-Goals — Photographer SaaS

What this project will **not** do, and why. Non-goals are how scope creep is prevented; an item that is not on this list will tend to drift back into scope. Every non-goal includes its reason — without the reason, the cut will be re-litigated.

> This is a wholly synthetic worked scenario. Its people, research, measurements, dates, permissions, galleries, and outcomes are illustrative assumptions, not completed real-world evidence.

Workflow phase: **Phase 3 — MVP Scope** (paired with [`mvp-scope.md`](mvp-scope.md)). Driving skill: `mvp-scope`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`mvp-scope.md`](mvp-scope.md), [`decisions.md`](decisions.md).

---

## 1. Product non-goals

- **No print or digital sales storefront** — because the wedge is photographer time-to-delivered-gallery, not commerce; bundling a storefront dilutes the wedge ([`product-thesis.md`](product-thesis.md) §2).
- **No watermarking, download-permission tiers, or rights-management UI** — per-image rights UI is not load-bearing for the thesis. The example makes no contractual-rights conclusion; a real project must establish its own rights and contract treatment.
- **No client comments or feedback threads** — the worked scenario assumes selection, not discussion, is the bottleneck.
- **No multi-shooter / second-photographer collaboration** — because the audience is *solo* freelance photographers; collaboration is a different product.
- **No Lightroom / Capture One plugin** — because manual export → upload is acceptable for v1; building a desktop integration is a separate engineering surface and would push the MVP past its budget ([`mvp-scope.md`](mvp-scope.md) §6).
- **No native mobile apps** — the worked scenario assumes desktop or tablet use and treats responsive web as sufficient for the initial test.
- **No client-side reminders or nudging** — because the pre-marked-subset UX is meant to *eliminate* the need to nudge; if the loop still requires reminders, the wedge has not landed.

## 2. User-segment non-goals

- **Not for high-volume school / sports / real-estate photographers** — the worked scenario assumes their bottleneck is throughput, not selection ([`problem-statement.md`](problem-statement.md) Optional C).
- **Not for studio photographers with assistants or culling teams** — the worked scenario assumes their bottleneck is coordination.
- **Not for hobbyists or pro-am photographers** — the worked scenario assumes the recovered-hours value pitch requires sustained gallery volume.
- **Not for clients who want to assemble their own custom album** — because that is a sales/print product surface, and the MVP excludes commerce.

## 3. Business-model non-goals

- **No enterprise sales** — because the audience is solo photographers and the MVP must work at small scale ([`founder-intent.md`](founder-intent.md) §4).
- **No marketplace, no photographer directory, no community feed** — because the product never inserts itself into the photographer ↔ client relationship ([`product-thesis.md`](product-thesis.md) Optional B).
- **No advertising-supported tier** — because client photos are private and ad targeting against them is incompatible with the data-handling commitments in [`intelligence-layer.md`](intelligence-layer.md) §4.
- **No commission or transaction fees on photographer-client deals** — because the MVP does not enter that relationship; commission is what print-sale gallery tools do, and it is not the wedge here.
- **No referral program in v1** — because the founder's adoption goal ([`founder-intent.md`](founder-intent.md) §4) is small-scale and personal-network-shaped; a referral program is overhead the MVP does not need.

## 4. Technical non-goals

- **No real-time collaboration** — because two photographers do not edit the same gallery in this product; multi-shooter support is already cut.
- **No on-device AI inference** — the planned boundary uses an as-yet-unselected managed provider; provider integration remains `Blocked` until DEC-4/DEC-11's later-entry condition is satisfied.
- **No custom model training or per-photographer fine-tune in v1** — one neutral scorer covers the selected event-and-portrait shoot types; per-style work is reconsidered only if DEC-8's accepted trigger fires.
- **No multi-region deployment** — because the audience is initially North-American and a single region keeps the cost ceiling within reach ([`architecture.md`](architecture.md) §7); cross-region failover is a later concern.
- **No public API** — because exposing an API is a different product surface and a different security posture; the MVP does not need it.
- **No general-purpose background-processing platform** — upload-time scoring remains application-owned, and one provider-neutral daily trigger may invoke the idempotent application-owned retention purge. Any broader recurring-work system is out of scope.

## 5. AI / intelligence-layer non-goals

- **No auto-retouch, auto-color, or generative edits to images** — because the founder anti-goal ([`founder-intent.md`](founder-intent.md) Optional B) explicitly forbids it; the AI suggests, never alters.
- **No AI-written client emails or AI-generated selection summaries** — because the loop closes with a structured photographer notification, not generated prose; generated text introduces hallucination risk for no thesis-critical gain.
- **No provider that retains or trains on submitted photos** — the specific provider is unresolved, and integration is `Blocked` until a dated written commitment is recorded in a later accepted decision entry.
- **No AI moderation of client choices** — because the photographer remains the decision-maker; an AI that overrides the photographer's selection is the failure mode P5 reported in [`discovery.md`](discovery.md) §2.
- **No cross-photographer or cross-gallery model context** — each provider call is isolated to one gallery and carries only downscaled image bytes plus opaque frame IDs; identity and cost attribution remain internal.

## 6. Process for revisiting non-goals

Non-goals can be reconsidered, but not silently. Any move from non-goal to in-scope must be:

1. Recorded as a decision in [`decisions.md`](decisions.md) with rationale (what changed, what evidence supports the move).
2. Reflected in both this file (remove the entry, link to the decision) and [`mvp-scope.md`](mvp-scope.md) (add the entry to §2 with the same justification).
3. Reviewed against the thesis in [`product-thesis.md`](product-thesis.md) §1 and the budget in [`mvp-scope.md`](mvp-scope.md) §6 — if the new scope blows either, the move is rejected.

The BuildSolid constitution's iteration rule (`framework/docs/constitution.md` §3 principle 9) applies: update both files in place; do not create parallel "v2" copies.

---

## Optional sections

### A. Founder-level anti-goals

The following items from [`founder-intent.md`](founder-intent.md) Optional B have hardened from personal-preference into project-level non-goals:

- No generative AI that modifies the photographer's image (auto-retouch / auto-color / synthetic edits) — appears as §5 above.
- No mobile-first product — appears as §1 above.
- No marketplace / community / directory — appears as §3 above.
- No enterprise sales — appears as §3 above.

### B. Non-goals previously considered and rejected as non-goals

- **"Photographer notification when client finalizes selections"** was briefly considered as a non-goal (could be replaced by manual-check on the dashboard) but was kept *in scope* — without the notification, the photographer is back to manual chasing, which is the friction the product is trying to remove. The decision is recorded in [`decisions.md`](decisions.md) DEC-3.
- **"Photographer dashboard with one row per gallery"** was considered for the cut list (could be inferred from email notifications) but was kept *in scope* — for photographers running 5–40 galleries per month, a per-gallery status view is the cheapest way to see what is blocked on whom. Recorded in [`decisions.md`](decisions.md) DEC-3.
