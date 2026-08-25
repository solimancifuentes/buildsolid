# Intelligence Layer — Project template

> **Purpose.** When AI is load-bearing or an accepted intelligence layer is materially changed, describe the project's **AI capabilities** as a designed system layer — not as decorative features. BuildSolid treats AI as an intelligence layer with capabilities, prompts (or policies), models, evals, fallbacks, costs, and safety. This artifact is the single source of truth for *what the AI does, how it knows when it's wrong, and what happens when it is*.
>
> **Workflow phase.** Phase 5 — Intelligence Layer.
>
> **Driving skill.** `intelligence-layer-architect`.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Every capability must address all of: prompts/policies, model choice, evals, fallbacks, cost, safety.** A capability missing any of these is a draft, not a capability.
> - **Profile applicability.** This artifact is **Need-triggered** for New Product Build, Existing Project Change, and Lightweight/Internal Build. Create or update it only when AI is load-bearing or the work materially changes an accepted intelligence layer.
> - **No N/A-only artifact.** If AI is not load-bearing and no accepted intelligence layer is materially changed, record a material exclusion in the owning compact applicability record when needed; do not create this file solely to say N/A. An existing `N/A - reason: <reason>` intelligence-layer artifact remains valid. In an otherwise applicable artifact, a numbered section that is materially inapplicable may use that same specific token; unresolved AI design or safety work is not N/A.
> - **Section depth.** When this artifact applies, keep every numbered stable heading and complete each applicable section. Use a specific `N/A - reason` only for a materially inapplicable section; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** Where the intelligence layer applies, this artifact is ready only when it defines AI role, capabilities, model/data flow, eval strategy, cost model, safety boundaries, and iteration loop, with any material in-file omission explained by a specific `N/A - reason`. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/intelligence-layer.md`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`mvp-scope.md`](mvp-scope.md), [`user-journeys.md`](user-journeys.md), [`architecture.md`](architecture.md), [`design.md`](design.md), [`spec.md`](spec.md), [`decisions.md`](decisions.md).

---

## 1. Role of the intelligence layer

> One short paragraph. What the AI layer does for the product (and what it does *not* do). State the boundary clearly: where AI helps, where deterministic logic owns the answer, and where the user is in the loop. A reader should not have to guess.

<…>

## 2. Capabilities

> Each AI capability gets its own subsection. List the smallest possible set — typically **1–3 capabilities for an MVP**. If the list grows beyond that, push back on [`mvp-scope.md`](mvp-scope.md).

### Capability — <name>

**What it does:** <one short paragraph>.
**Why it matters:** <ties to a journey in [`user-journeys.md`](user-journeys.md) or a thesis claim in [`product-thesis.md`](product-thesis.md)>.
**Inputs:** <data/text/images/etc. and where it comes from>.
**Outputs:** <what is returned, and how it is consumed by the product>.
**Where it surfaces in the UX:** <screen / flow reference from [`design.md`](design.md)>.

**Prompt / policy:** <one short paragraph; if a long prompt is needed, link to a separate file under this project rather than embedding>.
**Model choice:** <which model or family, and why this one over alternatives>.
**Evals:** <how this capability is measured — golden examples, scoring rubric, regression set; named explicitly>.
**Fallbacks:** <what happens when the capability fails, times out, or is unavailable>.
**Cost profile:** <expected cost per call and per active user; cost ceiling>.
**Safety considerations:** <prompt-injection, data exfiltration, misuse, hallucination management — what is mitigated, what is accepted>.

### Capability — <name>

> Repeat the same shape. If a project has only one capability, delete this section.

## 3. Cross-capability concerns

> One short paragraph. Issues that span every capability — shared safety guardrails, a unified observability story, a shared failure mode. Keeps the layer coherent.

<…>

## 4. Data flow into and out of models

> 3–6 bullets. What data leaves the system into model providers, what stays inside the system, and any retention/privacy commitments. If the project has a privacy commitment that depends on the layer, state it here.

- **Sent to providers:** <…>.
- **Never sent to providers:** <…>.
- **Retained by providers:** <…>.
- **Logged in this system:** <…>.

## 5. Eval strategy

> One short paragraph plus 3–5 bullets. How the project knows the AI layer is working — *before* and *after* changes. Include the size of the golden set, the cadence of evals, and who is responsible.

<…>

- **Golden set:** <…>.
- **Cadence:** <…>.
- **Owner:** <…>.

## 6. Cost model

> One short paragraph. The expected per-user cost of the AI layer at MVP scale, and the ceiling above which the project either prices differently, throttles, or cuts the capability. Names the assumption explicitly so it can be re-checked when usage data arrives.

<…>

## 7. Safety boundaries

> 3–6 bullets. The hard "no"s: things the AI must not do or say, regardless of prompt. Examples: financial advice, medical diagnosis, copying user-private content into shared output, generating content for unauthorized parties. State each as a rule and a check.

- **<rule>** — checked by <…>.
- **<rule>** — checked by <…>.

## 8. Iteration loop

> One short paragraph. How prompts, models, and evals are updated over time. Cross-references [`decisions.md`](decisions.md) — every material change to a prompt or model is a decision and is logged.

<…>

---

## Optional sections

### A. Capability dependencies *(optional)*

> If capabilities depend on each other (e.g., capability B uses capability A's output), describe the dependency and the failure-handling between them.

### B. Caching and memoization *(optional)*

> If the project caches model outputs, describe what is cached, when it is invalidated, and what staleness is acceptable. Skip if no caching is used.

### C. Provider redundancy *(optional)*

> If the project supports multiple providers for the same capability, name them and the switch policy.

### D. Compliance posture *(optional)*

> Specific regulatory regimes (HIPAA, GDPR, COPPA, etc.) and how the AI layer respects them. State concrete commitments, not aspirations.

### E. Observability for the AI layer *(optional)*

> Metrics, logs, and traces specific to the intelligence layer — request latency, token counts, eval scores, fallback-rate. Cross-references [`deployment.md`](deployment.md).
