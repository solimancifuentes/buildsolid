# Founder Intent — Project template

> **Purpose.** This artifact captures **why this project exists, for whom, and what success looks like to the founder.** It is the first durable output of the BuildSolid workflow and the anchor every later artifact (`product-thesis.md`, `mvp-scope.md`, `spec.md`, …) refers back to. It is read by the AI coding agent before any other project artifact and by the founder when they have lost the thread.
>
> **Workflow phase.** Phase 1 — Founder Discovery (per the BuildSolid context package).
>
> **Driving skill.** `founder-discovery` (pressure-tests intent) and `idea-compressor` (consumes intent to produce the thesis).
>
> **How to use this template.**
> - Replace `<…>` placeholders with your answers.
> - Keep blockquoted guidance (lines starting with `>`) only while drafting; remove or replace it before considering the artifact filled.
> - Required sections are non-negotiable; optional sections are clearly marked.
> - Section headings are stable; downstream skills rely on them — do not rename.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Required read; update if intent, audience, constraints, or a durable project profile or mode choice changed** for Existing Project Change, and **Required at lightweight depth** for Lightweight/Internal Build.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it states the founder, audience, reason for existence, success definition, constraints, and any deliberately durable project profile or mode choice clearly enough to anchor later artifacts. A transient session profile or mode is not required. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/founder-intent.md` shows a worked example.

Related artifacts (linked elsewhere in this project): [`discovery.md`](discovery.md), [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md).

---

## 1. Who the founder is

> One paragraph. Name, role, relevant experience for this project, and the angle they bring. Not a resume — the parts that matter for **this** project.

<…>

## 2. Who this is for

> One paragraph naming the **primary user** in concrete terms. Include their context, what they currently do, and how to recognize them. Avoid abstractions like "creators" or "small businesses"; pick a sharper subset.

<…>

## 3. Why this exists

> One paragraph. The motivating insight or itch behind the project. What is broken, missing, or under-served that you saw and decided to address? Keep it short — the full problem analysis lives in [`problem-statement.md`](problem-statement.md).

<…>

## 4. What success looks like (to the founder)

> 3–5 bullets. Concrete enough to recognize when achieved; aspirational enough to be worth building. Include a personal definition of success — not just metrics. If the founder would consider the project a success at a small scale, say so explicitly.

- <…>
- <…>
- <…>

## 5. Constraints the founder is naming up front

> 3–5 bullets, each one a single line. Time, money, energy, dependence on a day job, hard ethical lines, technologies the founder will or will not touch. These constraints feed [`mvp-scope.md`](mvp-scope.md) and [`non-goals.md`](non-goals.md).

- <…>
- <…>
- <…>

## 6. Active project profile and mode at intake

> Record a profile or mode here only when the founder deliberately makes it a durable cross-session project choice. The profile shapes workflow depth; the mode shapes the agent's question density and tone. Ordinary session posture is resolved and stated in the interaction, not persisted here, and this artifact is ready without a transient profile or mode. Complete only the applicable durable-choice line below and remove any unused placeholder. If neither choice is durable, remove both placeholder lines and retain the short no-durable-choice statement instead; do not use an N/A placeholder. See `AGENTS.md` §6 for definitions.

Durable profile: **<New Product Build | Existing Project Change | Lightweight/Internal Build>** — <one-sentence reason this should govern future sessions>.
Durable mode: **<Guided | Founder | Expert | Build>** — <one-sentence reason this should govern future sessions>.

No durable project profile or mode choice is recorded. Resolve and state session posture from the current instruction and accepted project state.

---

## Optional sections

> Include the following only when they materially clarify intent. Omit unused optional content. Use `N/A - reason: <reason>` only when an omission needs durable explanation.

### A. Founder background relevant to this project *(optional)*

> Include only if specific prior work, prior failures, or domain expertise is load-bearing for the agent's understanding. Skip generic biography.

### B. Anti-goals at the personal level *(optional)*

> Personal preferences the founder wants the project not to drift into — for example, "no enterprise sales", "no API platform", "no community ops". These are *founder-level* anti-goals; project-level non-goals live in [`non-goals.md`](non-goals.md).

### C. Origin story *(optional)*

> One short paragraph if the origin moment is genuinely useful context. Skip if not.

### D. Open questions for Founder Discovery *(optional)*

> Questions the founder cannot answer yet. They feed the next pass through `founder-discovery` and may move into [`discovery.md`](discovery.md) or [`decisions.md`](decisions.md) once resolved.
