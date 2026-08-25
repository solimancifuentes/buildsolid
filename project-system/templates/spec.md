# <Project> — Product Specification

> **Purpose.** Project-level **product spec**: what this project (or this version of it) is, who it serves, and what must be true for it to ship. The spec is the contract every implementation task is checked against.
>
> **Workflow phase.** Phase 7 — Spec Creation.
>
> **Driving skill.** `spec-planner`.
>
> **How to use this template.**
> - Replace `<Project>` and any `<…>` placeholder with project-specific content.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the spec filled.
> - Stable headings — `plan.md`, `tasks.md`, the QA reviewer skill, and the security reviewer skill rely on them. Do not rename without updating those.
> - **The spec is implementation-neutral.** It says what must be true; the *how* is in [`plan.md`](plan.md).
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Required after impact analysis** for Existing Project Change, and **Required** for Lightweight/Internal Build before implementation work can be planned or checked.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it states target users, problems, goals, non-goals, journeys, required capabilities, architecture/intelligence summaries, acceptance criteria, risks, and open questions at the depth selected by the profile. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/spec.md`.

Related artifacts: [`founder-intent.md`](founder-intent.md), [`product-thesis.md`](product-thesis.md), [`problem-statement.md`](problem-statement.md), [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md), [`user-journeys.md`](user-journeys.md), [`design.md`](design.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`plan.md`](plan.md), [`tasks.md`](tasks.md), [`decisions.md`](decisions.md).

---

## 1. Overview

> One short paragraph. The same compressed thesis as [`product-thesis.md`](product-thesis.md), here framed as the spec's overview. State what this version is and what it is for.

<…>

## 2. Target users

> One short paragraph plus a bullet for each user type if more than one. Mirrors [`product-thesis.md`](product-thesis.md) §3 and [`founder-intent.md`](founder-intent.md) §2. Be specific.

<…>

## 3. User problems

> Bullet list. The problems this version addresses, drawn from [`problem-statement.md`](problem-statement.md). Each bullet: a one-line problem statement. Do not list solutions here — solutions belong in §4 / §7.

- <…>
- <…>
- <…>

## 4. Goals

> Numbered list of concrete, verifiable goals. **Each goal is testable** — a reader should be able to say "yes, this version achieved that" or "no, it did not." Vague goals (e.g., "delight users") are not goals.

- **G1.** <…>
- **G2.** <…>
- **G3.** <…>

## 5. Non-goals

> Bullet list. Mirrors [`non-goals.md`](non-goals.md), restated in spec form. Each bullet: one line. Anything not on this list is in scope unless explicitly cut elsewhere.

- <…>
- <…>
- <…>

## 6. User journeys

> Reference [`user-journeys.md`](user-journeys.md) and list the journeys this spec covers by name. Do not re-state the journeys here — point at them.

- See [`user-journeys.md`](user-journeys.md): <journey 1>, <journey 2>, <journey 3>.

## 7. Required capabilities

> The capabilities the system must provide for the goals to be met. Each capability: name and a one-line description. This list is the bridge from problems (§3) to tasks ([`tasks.md`](tasks.md)).

- **<capability>** — <…>.
- **<capability>** — <…>.
- **<capability>** — <…>.

## 8. Architecture summary

> One short paragraph. The shape of the system at the highest level. The full design lives in [`architecture.md`](architecture.md); this section is the elevator pitch.

<…>

## 9. Intelligence layer summary

> One short paragraph. What the AI does at the highest level. Full design lives in [`intelligence-layer.md`](intelligence-layer.md). If the project has no intelligence layer, write `N/A - reason: no load-bearing AI layer` and remove the heading from §10's acceptance criteria.

<…>

## 10. Acceptance criteria

> The checklist of conditions that must all be true for this version to ship. Group by area. Each item is a single line.

**Product**

- [ ] <…>
- [ ] <…>

**Architecture**

- [ ] <…>

**Intelligence layer**

- [ ] <…>

**Quality**

- [ ] <…>
- [ ] <…>

**Documentation**

- [ ] <…>

## 11. Risks

> The risks that could prevent this version from meeting its goals, plus the mitigation flagged for each. This is *flagging*, not designing — the actual mitigation lives in [`plan.md`](plan.md).

- **R1. <name>** — <one-line risk> — *mitigation:* <one-line approach>.
- **R2. <name>** — <…> — *mitigation:* <…>.
- **R3. <name>** — <…> — *mitigation:* <…>.

## 12. Open questions

> Questions deferred to [`plan.md`](plan.md) or to explicit human decisions. Do not block the spec from being accepted on these — block implementation on them.

- **Q1.** <…>
- **Q2.** <…>

---

## Optional sections

### A. Versioning and amendments *(optional)*

> If this spec is for a version of an existing project, name the prior version and what changed at the spec level. Cross-references [`changelog.md`](changelog.md).

### B. External constraints *(optional)*

> Constraints the spec inherits from outside the project — regulatory, contractual, integration partner, parent product. Each: one line, source named.

### C. Out-of-scope alternatives considered *(optional)*

> Alternative product shapes that were considered and explicitly rejected. Briefly, with reasons. Prevents the same alternatives from being re-litigated mid-build.
