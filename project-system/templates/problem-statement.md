# Problem Statement — Project template

> **Purpose.** Articulate the problem the project addresses, the people who suffer it, and the alternatives they currently use. The problem statement is what every later scope decision is checked against — if a feature does not address something here, it is suspect.
>
> **Workflow phase.** Phase 2 — Idea Compression (paired with `product-thesis.md`).
>
> **Driving skill.** `idea-compressor`.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Optional** for Lightweight/Internal Build unless the problem, sufferers, severity, or alternatives are new or changed.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it identifies who has the problem, what hurts, why it persists, current alternatives, and severity/frequency in concrete terms. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/problem-statement.md`.

Related artifacts: [`founder-intent.md`](founder-intent.md), [`discovery.md`](discovery.md), [`product-thesis.md`](product-thesis.md), [`mvp-scope.md`](mvp-scope.md).

---

## 1. Who has this problem

> One short paragraph. The same primary user named in [`product-thesis.md`](product-thesis.md) §3, here described in terms of *what they do day-to-day* that creates the problem. Include scale signals if known (rough population size, frequency of the pain). Keep it grounded in observations from [`discovery.md`](discovery.md).

<…>

## 2. The problem

> 1–2 short paragraphs. State the problem in plain language. Avoid solutions and avoid feature lists. A reader who has never heard of this project should be able to nod along and say "yes, that is a real problem."

<…>

## 3. Why the problem persists

> 3–5 bullets. The structural reasons the problem has not already been solved. Skill gaps? Tooling cost? Workflow inertia? Platform limitations? Each bullet should be a single line.

- <…>
- <…>
- <…>

## 4. Current alternatives

> Mirrors [`discovery.md`](discovery.md) §4 in compressed form. For each alternative: name, what it does, where it falls short for the user in §1. Include silent alternatives (spreadsheets, group chats, doing nothing) — they are usually the real competition.

- **<alternative>:** what it does → where it falls short.
- **<alternative>:** what it does → where it falls short.
- **<alternative>:** what it does → where it falls short.

## 5. Severity and frequency

> One short paragraph. How painful is the problem when it hits, and how often does it hit? "Mildly annoying once a quarter" and "blocks the user every Friday afternoon" lead to very different products. Be honest — over-stating severity is the most common failure mode here.

<…>

---

## Optional sections

### A. Problem boundaries *(optional)*

> 2–4 bullets explicitly naming related problems this project does **not** address. This is a softer version of [`non-goals.md`](non-goals.md) and helps the agent avoid scope creep when later phases tempt expansion.

### B. Existing data on the problem *(optional)*

> Citations or references that quantify the problem (industry reports, public surveys, prior internal studies). Skip if there are none — "no public data" is a valid answer.

### C. Anti-personas *(optional)*

> Users who *might* look like the primary user but for whom this product is a poor fit. Naming them prevents the project from drifting toward the wrong audience.
