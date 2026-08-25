# Design — Project template

> **Purpose.** Capture **UX direction**: the design principles, the key screens, the tone of voice, and the references the project draws from. This is not a visual design specification or a Figma export — it is the durable, agent-readable description of how the product should feel to use.
>
> **Workflow phase.** Phase 4 — UX Direction (paired with `user-journeys.md`).
>
> **Driving skill.** `ux-minimalist`.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Minimalism rule** applies here harder than anywhere else. Cut screens, cut states, cut variants.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Need-triggered** for Lightweight/Internal Build when UX direction, screen behavior, tone, or accessibility materially affect the work.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it defines UX principles, tone, key screens, cross-screen patterns, and out-of-scope design boundaries at the depth required by the selected profile. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/design.md`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`user-journeys.md`](user-journeys.md), [`architecture.md`](architecture.md), [`spec.md`](spec.md).

---

## 1. Design principles

> 3–6 short principles that govern every UX decision in the project. Each principle: a one-line rule and a one-line reason. Avoid generic principles ("clean", "intuitive"); pick principles that would lead a designer to a *different* answer than the default.

- **<principle>** — because <…>.
- **<principle>** — because <…>.
- **<principle>** — because <…>.

## 2. Tone and voice

> One short paragraph. How does the product speak to the user — in copy, in error messages, in onboarding? Pick a tone with a specific shape (e.g., "calm and procedural; never apologetic for the user's situation"). Keep examples of phrases the product *would* and *would not* say.

<…>

## 3. Key screens

> The screens the MVP must include, in the order the user encounters them in [`user-journeys.md`](user-journeys.md). For each screen: a one-line purpose, the primary action, and the most important state. Bias toward fewer screens — combining related views into one screen is usually the right call.

### Screen 1 — <name>

**Purpose:** <…>.
**Primary action:** <…>.
**Most important state:** <…>.

### Screen 2 — <name>

**Purpose:** <…>.
**Primary action:** <…>.
**Most important state:** <…>.

> Add more screens only if [`user-journeys.md`](user-journeys.md) requires them.

## 4. Cross-screen patterns

> Short paragraph. Patterns shared across screens — navigation, loading states, error displays, AI-generated content presentation. Naming them here prevents per-screen drift.

<…>

## 5. Out of scope for design

> 2–4 bullets. Screens, states, or interaction patterns that are explicitly **not** in MVP design scope. Feeds [`non-goals.md`](non-goals.md).

- **No <…>** — because <…>.
- **No <…>** — because <…>.

---

## Optional sections

### A. Visual references *(optional)*

> Pointers (URLs or file paths) to designs, products, or screenshots that exemplify the desired look-and-feel. Keep the list short; cite *why* each reference matters in one line.

### B. Accessibility commitments *(optional)*

> The accessibility level the project commits to (e.g., WCAG 2.1 AA), and any project-specific accessibility guarantees. If accessibility is in scope but no commitment is named here, the project has not actually committed.

### C. Localization plan *(optional)*

> If the product ships in multiple languages or locales, name the strategy: which locales, when, what is delegated to humans vs machine translation. Skip if the MVP is single-locale.

### D. Empty / loading / error states *(optional)*

> A small set of design notes for the states most often skipped during prototyping. Include only if the project has a specific opinion (e.g., "no spinners; show what we have, then update").

### E. AI-presentation guidelines *(optional)*

> If the AI layer surfaces generated output to the user, how is it labeled, qualified, and undoable? Cross-references [`intelligence-layer.md`](intelligence-layer.md). Keeps user trust calibrated.
