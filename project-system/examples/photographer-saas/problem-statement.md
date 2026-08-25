# Problem Statement — Photographer SaaS

The problem this example addresses, the people who suffer it, and the alternatives they currently use. Every later scope decision is checked against this file — if a feature does not address something here, it is suspect.

> **Synthetic-scenario notice.** Every persona, quotation, interview, observation, measurement, date, population estimate, forum/survey reference, permission, and gallery in this worked example is synthetic and illustrative. Real product and organization names below are descriptive comparisons only; they imply no endorsement and no conducted research.

Workflow phase: **Phase 2 — Idea Compression** (paired with [`product-thesis.md`](product-thesis.md)). Driving skill: `idea-compressor`.

Related artifacts: [`founder-intent.md`](founder-intent.md), [`discovery.md`](discovery.md), [`product-thesis.md`](product-thesis.md), [`mvp-scope.md`](mvp-scope.md).

---

## 1. Who has this problem

The worked scenario targets solo, full-time freelance photographers whose work is **event-and-portrait shaped** — weddings, family sessions, branded portraits, and small-business headshots. It assumes 5–40 galleries per month and 200–2,500 edited images per gallery. Audience scale, tool use, and pain frequency are hypotheses for later validation, not measured population facts.

## 2. The problem

The worked scenario posits two frictions between "editing done" and "client signed off on final picks": repetitive pre-delivery culling and slow client selection. It uses illustrative estimates of two to four hours per typical shoot and five to fourteen days of client-decision time. The product hypothesis is that existing gallery tools do not compress both parts of that loop; a real downstream project must measure its own baseline before treating the mechanism or severity as established.

## 3. Why the problem persists

The scenario uses these hypotheses for why the problem could persist:

- Hosted-gallery products may optimize for hosting or sales rather than photographer time.
- AI-cull products may remain separate from client delivery, leaving the loop to be joined manually.
- Photographers are stylistically opinionated; an AI cull that imposes a generic "good photo" definition gets rejected (per [`discovery.md`](discovery.md) §3 Theme 5).
- The illustrative planning premise assumes vision-model inference only recently became affordable enough to test per-frame scoring; a real project must verify current pricing.
- The bottleneck is distributed and per-gallery; photographers absorb it as "the cost of doing business" rather than treating it as a fixable workflow.

## 4. Current alternatives

The named products are descriptive examples only; this example did not conduct or verify a competitive study.

- **Pixieset:** hosts galleries with client favoriting → no AI, no time savings on the cull side.
- **Pic-Time:** hosts galleries with print-sales focus → broader feature surface than photographers want; no AI cull.
- **ShootProof:** galleries plus light studio management → solves several problems lightly, none of them the cull-and-decide loop.
- **Self-hosted (S3 + static gallery):** flexible, no SaaS cost → no client-selection UX, no AI, photographer eats every rough edge.
- **Hand-culling in Lightroom + emailing JPEGs:** the silent default → maximum control, maximum time cost, no client-side selection record.
- **Desktop AI-cull tools (Aftershoot et al.):** speed up culling on the photographer's machine → do not deliver, do not collect selections; the loop is still glued by hand.
- **Doing nothing — accepting the long delivery loop:** an illustrative alternative in the synthetic scenario.

## 5. Severity and frequency

For planning, the scenario assumes two to four hours of pre-cull work and five to fourteen days of client-decision latency per gallery. Those figures and any derived monthly range are unvalidated hypotheses; a real downstream project must measure its own baseline before claiming severity, recoverable time, or capacity impact.

---

## Optional sections

### A. Problem boundaries

- This problem is *not* the problem of editing a RAW file. Editing speed is largely solved by Lightroom presets and the photographer's own muscle memory; the product does not touch it.
- This problem is *not* the problem of selling prints to clients. Print sales are a separate revenue surface; the MVP does not enter it.
- This problem is *not* the problem of running a photography business (contracts, invoicing, scheduling). Studio CRMs handle that; the MVP does not compete with them.
- This problem is *not* the problem of high-volume non-portrait photography (real estate, sports, school days), where the cull-and-decide loop is structurally different.

### B. Existing data on the problem

The PPA survey, r/photography discussion, WeddingPros discussion, and related claims are synthetic source references within the worked scenario. No survey or forum scan was conducted or verified for this example. A real downstream project must cite primary sources and collect its own evidence before treating the problem as established.

### C. Anti-personas

- **High-volume school / sports / real-estate photographers.** Their workflow is throughput-shaped; selection is not their bottleneck. The product is not for them.
- **Studio photographers with assistants and a culling team.** The bottleneck shifts to coordination, not photographer-time-per-gallery; existing studio CRMs serve them better.
- **Hobbyists and pro-am photographers.** The product's price/value pitch hinges on recovered hours per month; without sustained client volume, the math does not work.
