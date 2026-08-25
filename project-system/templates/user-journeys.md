# User Journeys — Project template

> **Purpose.** Capture the **few flows that actually matter** for the product. BuildSolid projects keep this list short on purpose — typically **1–3 journeys** for an MVP. Anything beyond that should be questioned against [`mvp-scope.md`](mvp-scope.md). Journeys named here drive the design (`design.md`), the architecture (`architecture.md`), and the spec (`spec.md`).
>
> **Workflow phase.** Phase 4 — UX Direction.
>
> **Driving skill.** `ux-minimalist`.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) while drafting; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Profile applicability.** This artifact is **Required** for New Product Build, **Conditional** for Existing Project Change, and **Optional** for Lightweight/Internal Build unless user flows, journeys, or acceptance paths matter to the build.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it describes the primary flows, actor intent, trigger, steps, success state, failure/edge cases, and cross-journey patterns needed by design, spec, and QA. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/user-journeys.md`.

Related artifacts: [`product-thesis.md`](product-thesis.md), [`mvp-scope.md`](mvp-scope.md), [`design.md`](design.md), [`spec.md`](spec.md).

---

## 1. Primary journey — <name>

> The single most important flow the MVP exists to support. This is the journey that, if it works, the thesis is alive — and if it fails, the thesis is dead.

**User:** <who is moving through this journey — should match [`product-thesis.md`](product-thesis.md) §3>.
**Trigger:** <what causes this user to start the journey>.
**Goal:** <what the user is trying to accomplish>.
**Success:** <what "done" looks like for the user — concrete enough to recognize>.

**Steps:**

1. <…>
2. <…>
3. <…>
4. <…>

**Failure modes:**

- <…>
- <…>

**Where the AI layer shows up *(if any)*:** <one line, or `N/A - reason: no load-bearing AI layer in this journey`>.

## 2. Secondary journey — <name> *(include only if needed)*

> Use this section only if the MVP genuinely requires a second flow. If the second journey is "the same user but later" or "the admin view of the same flow," consider folding it into §1.

**User:** <…>.
**Trigger:** <…>.
**Goal:** <…>.
**Success:** <…>.

**Steps:**

1. <…>
2. <…>
3. <…>

**Failure modes:**

- <…>

**Where the AI layer shows up *(if any)*:** <…>.

## 3. Third journey — <name> *(rare; include only with strong reason)*

> Most v0.1 MVPs do not have three core journeys. If this section is filled, [`mvp-scope.md`](mvp-scope.md) must explicitly justify it.

**User:** <…>.
**Trigger:** <…>.
**Goal:** <…>.
**Success:** <…>.

**Steps:**

1. <…>
2. <…>

**Failure modes:**

- <…>

**Where the AI layer shows up *(if any)*:** <…>.

## 4. Cross-journey patterns

> Short paragraph. State the patterns the journeys share — same user across journeys? Same data flowing between them? Same AI capability? This prevents accidental divergence in design and architecture.

<…>

---

## Optional sections

### A. Anti-journeys *(optional)*

> Flows the product explicitly does **not** support, even if they look related. For example: "no admin journey for inviting collaborators in v1." Keeps the surface area honest.

### B. Edge-case journeys *(optional)*

> Rare but important flows — error recovery, account migration, data export. Include only if [`mvp-scope.md`](mvp-scope.md) names them as required.

### C. Journey-level metrics *(optional)*

> If the project tracks per-journey metrics (completion rate, time-to-success), name them here. Cross-references the project's success criteria in [`mvp-scope.md`](mvp-scope.md) §4.
