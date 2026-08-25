# Intelligence Layer — Photographer SaaS

The AI capabilities in the photographer SaaS, designed as a **system layer** — not as decorative features. This artifact is the single source of truth for what the AI does, how it knows when it's wrong, and what happens when it is.

Workflow phase: **Phase 5 — Intelligence Layer.** Driving skill: `intelligence-layer-architect`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`mvp-scope.md`](mvp-scope.md), [`user-journeys.md`](user-journeys.md), [`architecture.md`](architecture.md), [`design.md`](design.md), [`spec.md`](spec.md), [`decisions.md`](decisions.md).

---

## 1. Role of the intelligence layer

The intelligence layer **suggests which images in a shoot are most likely to be keepers** and labels each suggestion with a reason (sharpness, expression, composition, near-duplicate). It does not decide; the photographer reviews every suggestion and overrides freely (Screen 2 in [`design.md`](design.md) §3). It does not modify any image. It does not run on client surfaces. The deterministic logic of the product — uploads, gallery state, delivery links, selections, notifications — is owned by the regular application code; the AI's only job is the per-frame suggestion at upload time. The user (the photographer) is in the loop on every frame; the client never sees AI-labeled output (per [`design.md`](design.md) §4).

## 2. Capabilities

The MVP has exactly **one AI capability**. Adding a second would push the project past its budget and would dilute the wedge.

### Capability — Image suggestion

**What it does:** At gallery upload time, scores every uploaded JPEG along four dimensions — *sharpness* (in-focus vs. soft / motion-blurred), *expression* (eyes open, neutral-to-positive face, no obvious blink), *composition* (rule-of-thirds, framing, headroom), and *near-duplicate-of-N* (visually redundant with another frame in the same shoot). Combines the four into a single per-frame "suggested keeper" boolean plus a label set explaining why. Returns the score and labels for every frame; does not return any data the photographer cannot see.

**Why it matters:** This is the wedge in [`product-thesis.md`](product-thesis.md) §2 made concrete. Without this capability, the product is a slower Pixieset; with it, the photographer's pre-cull time drops from hours to minutes ([`mvp-scope.md`](mvp-scope.md) §4).

**Inputs:** The application resolves each uploaded frame internally, downscales the JPEG, and sends the provider only the JPEG bytes plus an opaque per-frame ID. Storage paths, photographer or client identity, gallery identity, filenames, EXIF, captions, and cost-attribution fields remain internal. Each request is scoped to one gallery.

**Outputs:** Per frame: a numeric score (0.0–1.0), a `suggested` boolean (derived from the score plus a per-shoot threshold), and a label set drawn from a closed vocabulary: `sharp`, `eyes-open`, `composition`, `duplicate-of-<frame-id>`. The output is consumed by Screen 2 ([`design.md`](design.md) §3) for the photographer to review.

**Where it surfaces in the UX:** Only on the photographer's Upload + AI-review screen ([`design.md`](design.md) §3 Screen 2). The client never sees AI labels.

**Prompt / policy:** A short structured policy describes the four scoring dimensions, the label vocabulary, and the rule for combining them into the `suggested` boolean. The full policy text lives alongside a future implementation; this artifact does not embed it. Policy text is treated as code: every change goes through review, while [`decisions.md`](decisions.md) is used only when a change resolves a meaningful accepted choice, exception, deferral, or tradeoff. The policy constrains output to the closed vocabulary above so downstream code can rely on shape.

**Model choice:** Unresolved. Provider integration is blocked until a later append-only accepted decision names one managed vision-language provider and records its dated written no-retention/no-training commitment, as required by DEC-4 and clarified by DEC-11. A provider change is not DEC-8's first-iteration trigger. On-device inference remains out of scope.

**Evals:** A downstream implementation must create a frozen **300-frame**, photographer-as-judge golden set with properly established rights and consent. The shipped example contains no real corpus and claims no permission. Each frame carries a keeper/non-keeper label and dominant reason; evaluation reports keeper precision/recall and a per-reason confusion matrix.

**Fallbacks:** If the scoring pass fails, times out, or is unavailable, the gallery falls through to a "no pre-marks; photographer marks by hand" state. The loop still completes; the wedge is reduced for that gallery only. Fallback events are logged so the failure rate is visible. If a single frame fails to score, it is shown as `not-scored` and the photographer can mark it manually; the rest of the gallery continues.

**Cost profile:** The synthetic planning target is ≤ **$0.05 per gallery** at approximately 600 frames, conditional on later provider selection and pricing verification. The per-photographer target is ≤$2.00/month at the scenario's typical volume, below the accepted $5.00/month AI-cost ceiling—not a revenue ceiling. Hard per-gallery ceiling: **$0.20**; a future implementation caps inferences rather than spending past it.

**Safety considerations:** Image-mediated prompt injection is possible even with JPEG-only input. Its impact is mitigated, not eliminated, by the closed, schema-validated output vocabulary, the tool-less provider boundary (no outbound calls back into the system), and data minimization (downscaled JPEG bytes plus an opaque per-frame ID only). Data exfiltration remains the primary risk: the model must never receive identifying metadata, must never have cross-gallery context, and must run on a provider that does not retain submitted images for any purpose, including model training ([§4](#4-data-flow-into-and-out-of-models)). Unexpected or non-conforming model output is rejected as a scoring failure and falls through to the manual path; schema-conforming suggestions still remain subject to photographer review and override.

## 3. Cross-capability concerns

The MVP has only one capability, so cross-capability concerns reduce to **internal consistency within the suggestion capability**:

- The closed label vocabulary is the contract between the model, the application, and the UI. A new label cannot be added without a paired update to the policy, the application code, and the design.
- Eval cadence and golden-set versioning apply per-capability and are owned by the founder (§5). When the MVP grows a second capability later, the eval owner must split.
- Budget and cost-ceiling enforcement are implemented once at the model-call boundary, not per-capability, so the same ceiling applies cleanly when capabilities are added in a later iteration.
- Fallback behavior — "the loop still completes without the AI" — is a global invariant of the product. Any future capability must specify its own fallback before being accepted, per [`project-system/templates/intelligence-layer.md`](../../../project-system/templates/intelligence-layer.md) §2.

## 4. Data flow into and out of models

- **Sent to providers:** the JPEG bytes (downscaled to the smallest size the model accepts without accuracy loss) and a per-frame opaque ID. Nothing else.
- **Never sent to providers:** the photographer's name, the client's name, the gallery title, the gallery ID, any other client identifying data, EXIF GPS coordinates, or any user account data.
- **Retained by providers:** provider integration is blocked until a later accepted entry verifies a dated written commitment of zero retention and no training on submitted images. No provider call occurs before that gate is satisfied.
- **Logged in this system:** per-call latency, success/failure status, returned label set, and aggregate cost. Image bytes are **not** logged after the call returns; per-call logs are scrubbed of frame contents.
- **Cross-gallery context:** forbidden. Every gallery's scoring pass is isolated; no shared embedding store, no retrieval-augmented context across photographers or clients ([`non-goals.md`](non-goals.md) §5).
- **Client photo lifetime:** active images, caches, scores, selections, and other derived data are deleted 90 days after finalization unless the photographer explicitly extends that gallery. Storage lifecycle and the daily application purge enforce deletion. Opaque tombstones remain outside the database snapshot lineage until every capable snapshot expires; restores apply tombstones and current-time expiry before promotion or traffic ([`deployment.md`](deployment.md) §7; DEC-12).

## 5. Eval strategy

A downstream implementation evaluates every model or policy change against the frozen golden set and monitors override rate after launch. The full 300-frame set must reach precision ≥ 0.80 and recall ≥ 0.70 before promotion; a partial run is intermediate evidence only and cannot pass the gate.

- **Golden set:** 300 hand-labeled frames as described in §2; versioned alongside the policy and model.
- **Cadence:** every model change, every policy text change, and on a calendar pass once a month regardless. A monthly run is required to catch silent provider drift.
- **Owner:** the synthetic founder persona is the planned v1 eval owner. A real downstream project must assign actual ownership; growth beyond ten photographers may justify a later decision but is not DEC-8's first-iteration trigger.

The sole first-iteration trigger is **override rate > 50% sustained across at least three photographers in a calendar week**, as accepted in DEC-8. That signal starts an in-place Stage 13 model/policy assessment; it does not select a provider, change eval ownership, or automatically activate per-style scoring.

## 6. Cost model

The MVP's per-active-photographer AI cost target is **≤ $2.00/month** at typical volume (5–40 galleries × ≤ $0.05/gallery). The cost ceiling is **$5.00/month per active photographer**; sustained usage above that ceiling means the per-gallery scoring path is cheaper to throttle (sample within near-duplicate clusters, score those clusters once and propagate the label) than to keep paying. The first cost re-check is at the end of MVP launch month; the cost assumption is named explicitly so it can be revisited when real usage data arrives. If MVP usage shows the ceiling is reachable in normal operation, the project either prices the photographer accordingly, throttles, or cuts the AI capability — that decision would be recorded in [`decisions.md`](decisions.md).

## 7. Safety boundaries

- **The AI never modifies an image** — checked by the absence of any image-write code path in the model call boundary; the call returns scores and labels, not bytes.
- **The AI never sees cross-photographer or cross-gallery data** — checked by per-call input scoping and a unit test that fails if a request batch contains frames from more than one gallery.
- **The AI never receives client-identifying data or photographer-identifying data** — checked by an allow-list that forwards only downscaled image bytes plus an opaque per-frame ID, with everything else stripped at the boundary.
- **The AI's output vocabulary is closed** — checked by schema validation of every model response; non-conforming responses are dropped and the gallery falls through to manual marking.
- **The AI never appears on the client surface** — checked by a UI-level invariant (the client gallery component cannot read AI labels) and a regression test.
- **Provider switch never widens the boundary** — checked by the per-provider commitment review recorded in [`decisions.md`](decisions.md) before any provider is added or changed.

## 8. Iteration loop

Prompts, policy, model choice, and the golden set are updated in place. Routine review and eval evidence stays with the task, review, change, or operational record; a `DEC-N` entry is appended only for a meaningful accepted choice, exception, deferral, or tradeoff. DEC-8's override-rate signal drives the first substantive assessment; eval scores gate promotion. No parallel "v2" artifact is created.

---

## Optional sections

### A. Capability dependencies

Not applicable in v0.1 — the MVP has one capability. When a second is added (e.g., per-photographer style adjustment), this section will document the dependency between it and the suggestion capability.

### B. Caching and memoization

A downstream implementation may cache per-frame scores by content hash within the source gallery. Cache entries follow the same deletion lifecycle as the image. No cache is shared across galleries or photographers.

### C. Provider redundancy

The architecture can accommodate a second provider, but the first provider is still unresolved and no integration exists. A secondary remains a later candidate; before activation it requires its own accepted commitment review, boundary verification, cost check, and full eval-score parity.

### D. Compliance posture

The privacy, security, retention, and deletion controls in this synthetic example are illustrative design measures, not a compliance conclusion or legal advice. A real launch requires qualified, jurisdiction-specific review to determine applicable regimes and required notices, terms, consent, retention, deletion, subprocessor, consumer, and related treatment.

### E. Observability for the AI layer

Per model call: latency, success/failure, label set, cost. Per gallery: override rate, fallback rate, cost. Per photographer: monthly cost, monthly override rate. Dashboard surfacing for these signals lives in [`deployment.md`](deployment.md) §5; the dashboard exists as a planned artifact for v0.1 and is not stood up live in this example.
