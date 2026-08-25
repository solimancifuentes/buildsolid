# Founder Intent — Photographer SaaS

This artifact captures **why this project exists, for whom, and what success looks like to the founder.** It anchors every later artifact in this directory ([`product-thesis.md`](product-thesis.md), [`mvp-scope.md`](mvp-scope.md), [`spec.md`](spec.md), and the rest). Read it before any other artifact in this example.

> **Synthetic scenario.** Maya Chen, her biography, quotations, measurements, dates, prior tools, client work, network, and origin story are fictional and illustrative. This artifact does not describe a real founder or conducted research.

Workflow phase: **Phase 1 — Founder Discovery** (with the **Phase 0 — Intake** note in §6 / §7 below). Driving skills: `founder-discovery` (pressure-tests intent) and `idea-compressor` (consumes intent to produce the thesis).

Related artifacts: [`discovery.md`](discovery.md), [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md).

---

## 1. Who the founder is

Maya Chen is a freelance wedding and portrait photographer with seven years of full-time client work. She runs a one-person studio: she shoots, she culls, she edits, she delivers. She is not a software engineer by training, but she has learned enough scripting and AI tooling over the past two years to prototype workflows for herself, and she has decided to build the next one as a real product. She is the founder, the designer, and the first user. The relevant angle she brings is not "product manager who happens to know photographers" — she is a working photographer who has felt every step of the delivery loop on her own time.

## 2. Who this is for

The primary user is a **solo, full-time freelance photographer** whose work is event-and-portrait shaped — weddings, family sessions, branded portraits, small-business headshots — who delivers between five and forty galleries a month to private clients. They cull and edit in Lightroom or Capture One, they deliver via a hosted gallery (Pixieset, Pic-Time, ShootProof, or a self-hosted folder), and they wait for the client to come back with favorites. They are not staff photographers, agency photographers, or pro-am hobbyists; the workflow has to absorb a real volume without becoming overhead.

## 3. Why this exists

The motivating insight is that the **delivery loop** — the slice between "edit done" and "client signed off on final picks" — is where the photographer's time leaks the most and where existing gallery tools are weakest. Maya watched herself spend two to four hours per shoot manually pre-culling near-duplicates and "obviously not the keeper" frames before she could even hand a gallery to a client, and another one to two hours nudging the client back through email when their selections stalled. The full problem analysis lives in [`problem-statement.md`](problem-statement.md); the itch is that no existing tool treats the photographer's *time* as the scarce resource and the AI image-suggestion capability as the lever.

## 4. What success looks like (to the founder)

- Maya can deliver a 600-image gallery to a client with AI-suggested favorites pre-marked, in under fifteen minutes of her own time after editing finishes.
- A client receives a delivery link, makes selections, and finalizes them without Maya having to send a follow-up email.
- Five to ten other freelance photographers Maya knows replace at least one of their existing gallery tools with this product within the first quarter after launch.
- Maya considers the project a success at small scale — if it serves the ten photographers she trusts personally, it has met its bar; growth beyond that is bonus, not requirement.
- The project does not pull Maya away from shooting work; it is a tool she uses and improves between shoots, not a startup she is funded to grow.

## 5. Constraints the founder is naming up front

- Solo budget: roughly one quarter of part-time solo work (~10–15 hours/week) to ship the MVP, no co-founder, no funding round.
- No team to hire or manage; everything must be doable by one person.
- Photographers' shoots are private; **no client photo data may be used for model training, shared with marketing, or persisted longer than needed for delivery and selection** (see [`intelligence-layer.md`](intelligence-layer.md) §4).
- Maya will not touch crypto, NFT, social-feed, or generative-art-from-RAW directions; those are personal anti-goals (Optional B below).
- Within the synthetic scenario, the future MVP must fit the persona's active client schedule; this is an illustrative operating constraint, not an observed commitment.

## 6. Active project profile and mode at intake

Profile: **New Product Build** — Maya is building this photographer SaaS from a one-paragraph idea with no existing codebase, product, or accepted artifact set to start from.
Mode: **Founder** — the synthetic photographer-builder wants the workflow to pressure-test audience, problem, willingness to pay, differentiation, and scope before building. A later session may use Expert Mode when the current instruction and accepted state support it; no mandatory stage-boundary reconfirmation or orchestrator handoff is required.

## 7. Raw idea at intake (Stage 0)

> *Synthetic intake statement shown verbatim within the scenario, not a real founder quotation. It demonstrates what a Stage 0 note looks like. Preserve this scenario input; if its framing changes, append a dated fictional update rather than silently rewriting it.*

> *2026-04-27, Founder Mode.* "I want to build a small SaaS for freelance photographers like me. The core idea is: I upload a shoot, an AI helps me cull and pick the best images, I send a delivery link to my client, the client picks their favorites, and I'm done. The piece nobody else does well is the AI suggestion — sharpness, expression, composition, near-duplicates. Pixieset and the others let you upload and share, but they don't help you get to a deliverable in less time. I don't want to build a Lightroom replacement and I don't want to build payments. I want the smallest thing that proves a photographer's time-to-delivered-gallery drops by half."

---

## Optional sections

### A. Founder background relevant to this project

Within the synthetic narrative, Maya has built two prior internal tools for herself: a Python script that renames RAW files according to her shoot taxonomy, and a Lightroom export macro. These details establish scenario constraints; they are not completed real-world work.

### B. Anti-goals at the personal level

- No enterprise sales or studio-management features.
- No marketplace, no photographer directory, no community feed.
- No generative AI that modifies the photographer's image (no auto-retouch, no auto-color, no synthetic edits). The intelligence layer assists with selection only; it never alters the file.
- No mobile-first product. The first surface is desktop because that is where culling and delivery happen.

These are stronger than [`non-goals.md`](non-goals.md): they are personal-to-the-founder lines that even a re-scoped MVP must not cross.

### C. Origin story

Within the synthetic narrative, a 2025 wedding delivery required six hours of culling and twelve days of client selection. Maya uses that fictional event as the founder anchor for the four-step flow in [`user-journeys.md`](user-journeys.md) §1.

### D. Open questions for Founder Discovery

- How does the AI suggestion behave when the client overrides it? (Surfaced in [`discovery.md`](discovery.md) §5 H2; resolved at [`intelligence-layer.md`](intelligence-layer.md) §1.)
- Is there an audience of photographers for whom selection is *not* a bottleneck (high-volume school, real-estate, sports)? (Surfaced in [`discovery.md`](discovery.md) §5 H1; addressed by the anti-persona note in [`problem-statement.md`](problem-statement.md) Optional C.)
- Does the illustrative first-quarter adoption goal require onboarding work the MVP does not plan? This remains a prospective downstream product question; DEC-1 does not resolve it, and it does not change the artifact-only stop point.
