# Non-Goals — Project template

> **Purpose.** Make explicit what the project will **not** do. Non-goals are how scope creep is prevented; an item that is not on this list will tend to drift back into scope. Every non-goal includes its reason — without the reason, the cut will be re-litigated.
>
> **Workflow phase.** Phase 3 — MVP Scope (paired with `mvp-scope.md`).
>
> **Driving skill.** `mvp-scope`.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - **Stable headings** — downstream skills rely on them.
> - **Every non-goal must have a reason.** A non-goal without a "because" is incomplete.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Required at lightweight depth** for Lightweight/Internal Build when explicit exclusions or deferred scope need to constrain work.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it names excluded product, user, business, technical, AI, and process scope with enough rationale to prevent relitigation during implementation. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/non-goals.md`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`mvp-scope.md`](mvp-scope.md), [`decisions.md`](decisions.md).

---

## 1. Product non-goals

> Capabilities the product will not have in the current scope. Each item: a one-line statement and a one-line reason. Keep the language plain ("no <X>"); do not use marketing tone.

- **No <…>** — because <…>.
- **No <…>** — because <…>.
- **No <…>** — because <…>.

## 2. User-segment non-goals

> Audiences the project is not for in the current scope. Naming them prevents the product from drifting to please a population the thesis was not built around. Cross-references [`product-thesis.md`](product-thesis.md) §3 (the primary audience).

- **Not for <…>** — because <…>.
- **Not for <…>** — because <…>.

## 3. Business-model non-goals

> Revenue, distribution, or commercial mechanics the project explicitly avoids in the current scope. Examples: "no enterprise sales", "no marketplace fees in v1", "no advertising-supported tier."

- **No <…>** — because <…>.
- **No <…>** — because <…>.

## 4. Technical non-goals

> Technical capabilities the project will not build, even if they are tempting. Examples: real-time collaboration, on-device inference, custom model training, multi-region deployment. Cross-references [`architecture.md`](architecture.md).

- **No <…>** — because <…>.
- **No <…>** — because <…>.

## 5. AI / intelligence-layer non-goals

> AI capabilities the project explicitly will not include, despite being feasible. Treats AI as a designed layer, not as a temptation. Cross-references [`intelligence-layer.md`](intelligence-layer.md).

- **No <…>** — because <…>.
- **No <…>** — because <…>.

## 6. Process for revisiting non-goals

> One short paragraph. Non-goals can be reconsidered, but not silently. State here that any move from non-goal to in-scope must be recorded as a decision in [`decisions.md`](decisions.md) with rationale, and must update both this file and [`mvp-scope.md`](mvp-scope.md). The BuildSolid constitution's iteration rule applies: update artifacts in place; do not create parallel versions.

<…>

---

## Optional sections

### A. Founder-level anti-goals *(optional)*

> Personal preferences from [`founder-intent.md`](founder-intent.md) Optional B that have hardened into project-level non-goals. Move them here when they are firmly outside scope, not just "would prefer to avoid."

### B. Non-goals previously considered and rejected as non-goals *(optional)*

> Items that were considered for this list but were ultimately kept in scope. State each, briefly, with the reason it stayed in scope. This prevents the same debate from being re-opened in the future without new evidence.
