# MVP Scope — Project template

> **Purpose.** Define the smallest valuable build that proves the project's thesis. The MVP scope is what every implementation task is checked against. **Minimalism is the rule** — when two options work, the smaller one wins; cut, then cut again.
>
> **Workflow phase.** Phase 3 — MVP Scope.
>
> **Driving skill.** `mvp-scope` (paired with `non-goals` to lock the cuts).
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Required at lightweight depth** for Lightweight/Internal Build when scope, cuts, success, or failure criteria are new or changed.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it states the thesis to prove, must-haves, explicit cuts, success/failure criteria, and time/effort budget proportionate to the selected profile. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/mvp-scope.md`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`non-goals.md`](non-goals.md), [`user-journeys.md`](user-journeys.md), [`spec.md`](spec.md).

---

## 1. The thesis the MVP must prove

> One paragraph, restated from [`product-thesis.md`](product-thesis.md) §1 in MVP terms. Phrase it as "the smallest thing that proves <X>." This sentence is the test every in-scope item must pass.

<…>

## 2. In scope (must-haves)

> The set of capabilities the MVP must include for the thesis to be testable. **Bias hard toward fewer items.** A solo MVP that ships should usually be 3–7 items here, not 15. Each item: a one-line capability, then a one-line reason it is required. If the reason references something outside [`product-thesis.md`](product-thesis.md) or [`problem-statement.md`](problem-statement.md), question it.

- **<capability>** — required because <…>.
- **<capability>** — required because <…>.
- **<capability>** — required because <…>.

## 3. Explicit cuts (would-be-nice, deferred)

> Capabilities that *almost* made it but were cut to keep the MVP small. For each: a one-line capability and a one-line reason it was cut (cost, scope, risk, lack of evidence). These feed [`non-goals.md`](non-goals.md) so they do not silently re-enter scope.

- **<capability>** — cut because <…>.
- **<capability>** — cut because <…>.
- **<capability>** — cut because <…>.

## 4. Success criteria

> 3–5 bullets. Concrete, measurable conditions that, if true, confirm the MVP proved the thesis. Examples: "10 freelance photographers complete a delivery using the app in week 1"; "median delivery time drops by 50% vs the user's current workflow." Avoid vague success metrics like "good user feedback."

- <…>
- <…>
- <…>

## 5. Failure criteria

> 2–4 bullets. Conditions that, if true, indicate the MVP failed and the project should reconsider its thesis or its scope. State these now — not when failure happens.

- <…>
- <…>

## 6. Time and effort budget

> One short paragraph. The rough effort window for the MVP — measured in weeks of solo work, or whatever unit fits the founder. If the budget is more than one quarter of solo work, push back on §2 and §5; the MVP is probably not minimal yet.

<…>

---

## Optional sections

### A. Phased path *(optional)*

> If the MVP itself has internal phases (e.g., "ship the manual flow first, then add AI suggestions"), name them here in order. Each phase should be independently shippable. If phases would split the MVP into multiple releases, ask whether the *first* phase should actually be the MVP.

### B. Dependencies on external systems *(optional)*

> External services, APIs, models, or data the MVP depends on. Each entry: name, role, fallback if it disappears. Naming the fallback up front prevents the project from being silently coupled to a single provider.

### C. Explicitly deferred AI capabilities *(optional)*

> AI capabilities that were tempting but are not in MVP scope. Cross-references [`intelligence-layer.md`](intelligence-layer.md). Helps prevent "AI feature creep" during implementation.
