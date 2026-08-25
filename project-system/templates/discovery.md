# Discovery — Project template

> **Purpose.** Capture discovery notes — both raw observations and structured findings — about the user, the problem, and current alternatives. Discovery is the evidence base for the rest of the workflow; later artifacts (`product-thesis.md`, `problem-statement.md`, `mvp-scope.md`) cite or compress from here.
>
> **Workflow phase.** Phase 1 — Founder Discovery.
>
> **Driving skill.** `founder-discovery` (in Founder Mode) consumes raw notes here and presses on the assumptions; `idea-compressor` reads structured findings to produce the thesis.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Required sections are non-negotiable; optional sections are clearly marked.
> - Stable headings — downstream skills rely on them.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Optional** for Lightweight/Internal Build unless user/audience/problem evidence is being collected or materially revised.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it distinguishes raw observations from structured findings, names current alternatives, and identifies hypotheses or open questions still needing evidence. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/discovery.md`.

Related artifacts: [`founder-intent.md`](founder-intent.md), [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md).

---

## 1. Who was talked to or observed

> Bullet list. Each entry: who (role + context, anonymized if needed), how (interview, shadowing, public posts, prior experience), and when (date or rough period). It is fine for some entries to be the founder's own prior experience — say so. Aim for 3–8 distinct sources.

- <…>
- <…>
- <…>

## 2. Raw observations

> The unprocessed evidence. Quotes, behaviors, workarounds, frustrations, surprises. Resist the urge to summarize here — that is what the next section is for. If a quote is paraphrased, mark it.

- <…>
- <…>
- <…>

## 3. Structured findings

> Group the raw observations into 3–7 themes. Each theme: a one-line claim, then 2–3 supporting observations from §2. A theme is only worth keeping if it shows up across multiple sources.

### Theme 1 — <name>

**Claim:** <one-line claim>.
**Supporting observations:** <reference §2 items or quote them>.

### Theme 2 — <name>

**Claim:** <…>.
**Supporting observations:** <…>.

> Add more themes as needed. Keep the same shape.

## 4. Current alternatives

> What do users do today instead of the proposed product? Include the obvious competitors *and* the silent ones (spreadsheets, group chats, doing nothing). For each: name, how it is used, where it falls short. This feeds [`problem-statement.md`](problem-statement.md).

- **<alternative>:** how used → where it falls short.
- **<alternative>:** how used → where it falls short.
- **<alternative>:** how used → where it falls short.

## 5. Hypotheses to test next

> The hypotheses Founder Discovery has surfaced but not yet resolved. Each hypothesis: a one-line claim and the cheapest test that would confirm or kill it. These feed the next pass through `founder-discovery` or land in [`decisions.md`](decisions.md) once resolved.

- **H1:** <claim> — *test:* <…>
- **H2:** <claim> — *test:* <…>
- **H3:** <claim> — *test:* <…>

---

## Optional sections

### A. Market and competitive scan *(optional)*

> A short scan of the broader space — adjacent products, related tools, regulatory or platform constraints. Keep it tight; this is not a market report.

### B. Quotes worth preserving *(optional)*

> A small number of quotes that capture user voice or pain in a way the structured findings cannot. Cite the source from §1.

### C. Open questions for the founder *(optional)*

> Questions the discovery process raised that the founder must answer before later phases can land. Move resolved items into [`decisions.md`](decisions.md).
