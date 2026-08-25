# Discovery — Photographer SaaS

Synthetic discovery notes about freelance photographers, their delivery workflow, and possible alternatives. This is illustrative input that the remaining workflow compresses from, not evidence of conducted research. Later artifacts ([`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`mvp-scope.md`](mvp-scope.md)) cite or compress these scenario assumptions.

Workflow phase: **Phase 1 — Founder Discovery.** Driving skill: `founder-discovery` (in Founder Mode) consumes raw notes here and presses on the assumptions; `idea-compressor` reads structured findings to produce the thesis.

Related artifacts: [`founder-intent.md`](founder-intent.md), [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md).

---

## 1. Synthetic participants and illustrative observations

Every person, interview, quotation, date, count, permission, and forum-scan reference below is fictional scenario material. No real participant was interviewed or anonymized, and no public-post scan was conducted.

- **Maya Chen — synthetic founder persona.** Illustrative seven-year wedding/portrait background and fourteen-delivery self-observation set.
- **P2 — synthetic wedding-photographer persona.** Illustrative four-year background and hosted-gallery workflow.
- **P3 — synthetic family/portrait persona.** Illustrative nine-year background and hosted/private-storage workflow.
- **P4 — synthetic branded-portrait persona.** Illustrative small-business gallery workflow.
- **P5 — synthetic senior wedding-photographer persona.** Illustrative hosted-gallery and prior AI-culling experience.
- **Illustrative public-post signal.** A hypothetical January–April 2026 forum scan used to demonstrate how supporting evidence might be summarized.

The deliberately small synthetic sample is friend-of-founder biased by design. P2–P5 are fictional identifiers, not anonymized real participants.

## 2. Raw observations

The quotations, paraphrases, dates, and measurements below are synthetic scenario inputs, not real testimony.

- *(Maya, journaled 2026-03-09)* "Just spent 4 h 12 m culling a 2,400-image wedding before the client even sees it. Half of those four hours was deleting near-duplicates and obvious blinks."
- *(P2, paraphrased)* "I send the gallery and then I wait. Sometimes a week. I always end up sending a 'just checking in' email."
- *(P3, paraphrased)* "Clients pick way too many images. I have to nudge them down to whatever the contract says. It feels rude every time."
- *(P4)* "I batch my brand shoots. The AI cull would help me most because the same poses repeat across clients and I'm scrolling through near-identical frames."
- *(P5, paraphrased)* "I tried an AI culler tool last year. It was opinionated about 'good photos' in a wedding-specific way that didn't match my style. I went back to hand-culling."
- *(Public posts)* Repeated theme: 'time between gallery sent and selections received' is the part of the workflow photographers feel least in control of. Less common but present: 'I would pay for an AI cull if it learned my taste' (cited skeptically — P5 is the counter-evidence).
- *(Maya)* "Almost every client opens the gallery within 24 hours but takes 5–14 days to actually select. The opening is fast; the deciding is slow."
- *(Maya)* "Clients message back with 'these are all great, can you just pick'." This happens 2–3 times per quarter.
- *(P3)* "I have one tool for sharing galleries, one for selections, one for invoicing, one for image culling. I do not want a fifth tool unless it replaces at least one."

## 3. Structured findings

These findings are hypotheses synthesized from the fictional observations above. A real downstream project must establish its own evidence before treating them as validated.

### Theme 1 — The bottleneck is between editing and final selection, not editing itself

**Claim:** Photographers' biggest unrecovered time is in the *delivery loop* (cull → deliver → wait → final-select), not in editing.
**Supporting observations:** Maya's 4 h 12 m culling note (§2); P2's "send and wait"; the public-posts theme of "least in control"; Maya's 5–14 day client-deciding window.

### Theme 2 — Existing gallery tools are good at hosting, weak at *helping the photographer get to delivered*

**Claim:** Pixieset / Pic-Time / ShootProof are reliable hosts but do not reduce the photographer's pre-delivery time.
**Supporting observations:** P2 uses Pixieset and still hand-culls; P3 stitches multiple tools; P5's prior AI-cull tool failure (style mismatch) suggests the AI feature has to be built, not bolted.

### Theme 3 — Clients open fast and decide slow

**Claim:** Selection latency is a client-behavior problem the photographer cannot fix by emailing harder.
**Supporting observations:** Maya's 24-hour-open / 5–14-day-decide observation; P3's "they pick too many" frustration; P4's batch repetition implying same dynamic applies to small-business clients.

### Theme 4 — Photographers will not adopt a tool unless it replaces something

**Claim:** A new tool that adds itself to a workflow is dead on arrival; one that subtracts a tool can succeed.
**Supporting observations:** P3's explicit "unless it replaces at least one"; the founder constraint in [`founder-intent.md`](founder-intent.md) §5 about not being another overhead surface.

### Theme 5 — AI must respect the photographer's taste, not override it

**Claim:** An opinionated AI cull that does not match the photographer's style will be rejected; the photographer must remain the decision-maker.
**Supporting observations:** P5's failed-prior-AI-tool experience; P4's "near-identical frames" framing (where the AI is helping, not deciding); Maya's anti-goal in [`founder-intent.md`](founder-intent.md) Optional B (no auto-retouch, selection only).

## 4. Current alternatives

The real product names below are descriptive examples only; no endorsement, affiliation, completed evaluation, or current-market verification is claimed.

- **Pixieset:** hosted galleries with built-in client-favorite selection → strong host, no AI, no time-saving in the cull step.
- **Pic-Time:** hosted galleries with sales/store features → strong host, leans toward selling prints, no AI cull, more surface than Maya wants.
- **ShootProof:** galleries + lightweight studio management → does several things at once; most photographers Maya talked to use it for one or two of those, not all.
- **Self-hosted (S3 + a static gallery generator):** flexible and cheap → no client-selection UX, no AI, photographer eats the rough edges.
- **Hand-culling in Lightroom + emailing JPEGs:** the silent default for photographers who haven't adopted a gallery tool yet → highest control, highest time cost, no client-side selection record.
- **Prior AI-cull tools** (e.g., Aftershoot-style products): exist; tend to be opinionated about "good photos" in a way that does not match every photographer's style → P5's experience.
- **Doing nothing** — accepting the long delivery loop as the cost of doing freelance work → an illustrative alternative in this synthetic scenario, not a measured market finding.

## 5. Hypotheses to test next

- **H1:** A solo photographer's delivery time drops by ≥50% if AI pre-marks suggested favorites and the client UI starts from a pickable subset → *test downstream:* use synthetic fixtures first, then a properly authorized real gallery.
- **H2:** Photographers accept suggestions when each one is overridable and explained → *test downstream:* use a synthetic prototype, then recruit properly consented participants.
- **H3:** Clients finalize faster when the gallery defaults to a reviewed subset with an expand-to-all affordance → *test downstream:* establish an authorized comparison with appropriate participants and legal treatment.

Test results update the artifact that owns the affected claim. Add a [`decisions.md`](decisions.md) entry only when a meaningful choice, exception, deferral, or tradeoff is accepted.

---

## Optional sections

### A. Market and competitive scan

For scenario purposes, hosted-gallery products such as Pixieset, Pic-Time, ShootProof, and CloudSpot illustrate one category, while products such as Aftershoot, Imagen, and Narrative Select illustrate a separate AI-culling category. The hypothesized opportunity is a delivery workflow with integrated suggestions. This is illustrative positioning, not completed market research; a real downstream project must verify current products and claims.

### B. Synthetic quotes worth preserving

- Maya, journal: "The deciding is slow."
- P3: "I do not want a fifth tool unless it replaces at least one."
- P5: "It was opinionated about 'good photos' in a wedding-specific way that didn't match my style."

### C. Open questions for the founder

- The scorer scope is resolved by DEC-1's body and clarified by DEC-11: one neutral scorer across selected event-and-portrait shoot types, with per-style weighting deferred.
- CSV export is resolved by DEC-7: filenames only; AI labels are not exported.
