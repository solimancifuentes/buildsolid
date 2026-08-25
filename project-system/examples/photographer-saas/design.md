# Design — Photographer SaaS

UX direction for the photographer SaaS MVP: design principles, key screens, tone of voice, references. This is not a visual specification; it is the durable, agent-readable description of how the product should feel to use.

Workflow phase: **Phase 4 — UX Direction** (paired with [`user-journeys.md`](user-journeys.md)). Driving skill: `ux-minimalist`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`user-journeys.md`](user-journeys.md), [`architecture.md`](architecture.md), [`spec.md`](spec.md).

---

## 1. Design principles

- **Photographer-time is the metric** — because the wedge in [`product-thesis.md`](product-thesis.md) §2 is recovered hours, not feature count; every screen is judged by whether it reduces or adds friction in the loop.
- **The photographer remains the decision-maker** — because [`discovery.md`](discovery.md) §3 Theme 5 says photographers reject AI that overrides their taste; the UI must surface AI suggestions as suggestions, not verdicts.
- **Show keepers first to the client; expand on demand** — because the client default-view is the lever that compresses decide-time; a full-gallery default would erase the wedge.
- **Two surfaces, no more** — because the photographer surface (dashboard + gallery review) and the client surface (delivery link) are the only two; any third surface is suspect.
- **No spinners; show what we have, then update** — because every loading state photographers wait through is loop time; partial states beat blocking states.
- **Fewer screens, fewer states, fewer choices** — the minimalism rule applied to UX: when two layouts work, the smaller one wins.

## 2. Tone and voice

The product speaks the way a senior photo editor speaks to a working photographer: concise, procedural, never apologetic on the photographer's behalf, never enthusiastic about photos that have not yet been chosen. Error messages name the problem and the next step ("Upload paused — re-trying. You can keep working."). The product never says "delight," "seamless," "magic," or "AI" in user-facing copy except when surfacing the source of a suggestion; instead of "Our AI thinks this is your best frame" it says "Suggested — sharp, eyes open." Empty states say what the screen is for in one sentence, never advertise what could be there ("No galleries yet. Upload a folder of edited JPEGs to start.").

## 3. Key screens

The MVP ships four screens. Three are photographer-facing; one is client-facing. Fewer screens would force a journey to combine, which the journeys in [`user-journeys.md`](user-journeys.md) §1 do not allow.

### Screen 1 — Photographer dashboard

**Purpose:** A single list of every gallery the photographer is currently working on, with status and the action that is currently blocking the loop.
**Primary action:** "New gallery" (which opens the upload screen).
**Most important state:** Each row shows status — `uploading`, `suggesting`, `review`, `sent`, `open`, `finalized`, `stalled` — and a one-line "what's blocked on whom" (e.g., "Waiting on you to review", "Waiting on client", "Client viewed 2 days ago").

### Screen 2 — Upload + AI-review

**Purpose:** Combine the upload step (drop a folder of JPEGs) and the AI-review step (accept / override the AI's pre-marked subset) into one screen so the photographer never tabs between them. While images upload and score, the screen progressively populates with thumbnails and pre-marks; the photographer can begin reviewing as soon as the first batch lands.
**Primary action:** "Send delivery link to client" (becomes available once review is complete).
**Most important state:** Per-image — `pending`, `suggested (reason: sharp / eyes-open / composition / duplicate-of-<id>)`, `kept`, `rejected`. The reason label is always visible on suggested frames so the photographer never has to ask why.

### Screen 3 — Client delivery link

**Purpose:** Show the client the photographer's reviewed gallery, defaulting to the photographer-reviewed keeper subset, and let the client mark favorites and finalize.
**Primary action:** "Finalize selections" (single, explicit action; no ambiguity about whether the client is done).
**Most important state:** Two views — `keepers (default)` and `all`. A non-intrusive "Show all" affordance is always reachable; the count of additional images is shown so the client knows what they are expanding into.

### Screen 4 — Finalized selections (photographer view)

**Purpose:** Show the photographer the client's picked images in a dense grid, with a download/export-as-CSV affordance for the final edit pass in Lightroom.
**Primary action:** "Download filenames (CSV)".
**Most important state:** Picks visible at a glance; non-picks accessible via "Show non-picks" but visually de-emphasized.

A photographer signup / login screen exists but is not journey-bearing. It is intentionally generic (email + password, no team, no profile setup) and is not promoted in this list.

## 4. Cross-screen patterns

- **State vocabularies are distinct and mapped deliberately.** Gallery lifecycle uses `uploading | suggesting | review | sent | open | finalized | stalled`. Per-image review uses `pending | suggested | kept | rejected`, plus `not-scored` for manual fallback. Screen 4 presents finalized client selections as `pick` or `non-pick`. Transitions between these domains are explicit; no artifact treats the vocabularies as interchangeable.
- **AI presentation is consistent.** Anywhere the system surfaces a suggestion to the photographer, it is labeled with one or more reasons from the closed vocabulary `sharp | eyes-open | composition | duplicate-of-<id>`, never as an unexplained verdict. The client surface receives only the photographer's post-review subset and no AI label.
- **Loading states are progressive, not blocking.** Screen 1 populates with cached state immediately; Screen 2 paints thumbnails as they arrive; Screen 3 shows the keepers as soon as any have rendered. No screen has a full-page spinner.
- **Error states name the problem and the next step.** No "something went wrong"; every error has a concrete next action.

## 5. Out of scope for design

- **No marketplace screen / public profile / community feed** — because [`non-goals.md`](non-goals.md) §3 cuts these.
- **No print-sales or storefront screen** — because [`non-goals.md`](non-goals.md) §1 cuts commerce.
- **No client comments or messaging UI** — because [`non-goals.md`](non-goals.md) §1 cuts client-side discussion.
- **No mobile native UI** — because [`non-goals.md`](non-goals.md) §1 cuts native mobile; the four screens are responsive web, sufficient for tablet and mobile-web use.

---

## Optional sections

### A. Visual references

- **Linear (linear.app) dashboard** — an illustrative reference for the dense, status-led row layout of Screen 1 and the "every row tells you what's blocked on whom" pattern.
- **Lightroom Library module's filmstrip** — an illustrative reference for Screen 2 review density and a familiar gallery-review pattern to test later.
- **Pixieset client gallery** — an illustrative reference for a minimal delivery-link layout; the example's planned design differs by defaulting to the keeper subset rather than the full gallery.

These real product names are descriptive interface references only. They are not research sources, partners, endorsements, or evidence that those products were evaluated for this synthetic example.

### B. Accessibility commitments

The product targets **WCAG 2.1 AA** for the photographer surface (Screens 1, 2, 4). The client surface (Screen 3) targets the same level on the keepers default view; the "Show all" expanded view is given the same care as a stretch goal but is not blocking for v1 launch. Specific commitments: keyboard navigation across the gallery grid, visible focus states, color-contrast at AA on the status vocabulary, alt-text on UI chrome (image alt-text is not generated by the product — the photographer's own caption, if any, is used).

### C. Localization plan

Single-locale (English, US) for v1. Localization is deferred work, not an alternate first-iteration trigger under DEC-8.

### D. Empty / loading / error states

- **Empty.** Dashboard shows "No galleries yet. Upload a folder of edited JPEGs to start." Upload-review screen shows "Drop a folder here, or click to choose."
- **Loading.** No spinners. Screens populate progressively as data arrives. Where work is happening in the background, a small inline progress indicator (e.g., "Scoring 412 of 600") is shown without blocking interaction.
- **Error.** Each error names the problem ("Upload paused — network error") and the next step ("Retrying. Keep working.") in a non-modal banner. The product never shows a generic "something went wrong" message.

### E. AI-presentation guidelines

When the AI's output is shown to the user, it is:

- **Labeled.** Every AI-surfaced suggestion shown to the photographer has a reason from the closed vocabulary (`sharp`, `eyes-open`, `composition`, `duplicate-of-<id>`).
- **Qualified.** The product says "Suggested" not "Best." The photographer remains the chooser.
- **Undoable.** Every AI suggestion is a one-click override. Override state is persistent; the AI never re-overrides the photographer.
- **Bounded.** The AI never appears on the client surface as a labeled "AI." The client sees the photographer's post-review subset; the photographer's labels are not surfaced to the client.

These rules are enforced by [`intelligence-layer.md`](intelligence-layer.md) §7 (safety boundaries).
