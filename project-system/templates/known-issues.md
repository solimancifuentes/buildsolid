# Known Issues — Project template

> **Purpose.** Running list of **bugs, gaps, and intentional debt that must persist across sessions**. Known-issues is the durable answer to "what remains broken, missing, or intentionally deferred?" — read by anyone landing on the project, anyone preparing to ship, and anyone planning later work.
>
> **Workflow phase.** Cross-cutting; surfaces especially during Phase 10 (QA and Review) and Phase 13 (Iteration).
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) only at the top as a how-to-read header; remove or replace before considering the artifact filled.
> - Stable headings — downstream skills rely on them.
> - **Every entry has a category, a severity, and a status.** Bare descriptions are not enough.
> - **Authority.** Entries here are accepted working memory for persistent bugs, gaps, and intentional debt. If resolving an issue requires a meaningful accepted scope, architecture, launch, or debt tradeoff, record that decision in [`decisions.md`](decisions.md).
> - **Iteration intake.** An entry may support substantive Stage 13 learning when the material-change threshold is met. It does not force Stage 13, iteration, or a decision entry for same-scope bugs, review remediation, maintenance, retry, or ordinary correction.
> - **Persistence threshold.** Do not add an issue that is found and resolved within the same task, review, pull request, or maintenance pass unless a fresh agent still needs the record. Keep ordinary correction provenance in the task, review, pull request, or change record.
> - **Profile applicability.** This artifact is **Need-triggered** for New Product Build and Existing Project Change when bugs, gaps, accepted limitations, or intentional debt must persist across sessions, and **Optional** for Lightweight/Internal Build.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when it records current bugs, gaps, intentional debt, status, impact, owner or next review point, and resolution history when persistent issues exist. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/known-issues.md`.

Related artifacts: [`spec.md`](spec.md), [`tasks.md`](tasks.md), [`decisions.md`](decisions.md), [`changelog.md`](changelog.md), [`launch-checklist.md`](launch-checklist.md).

---

## How to read this file

Entries are grouped by **category**: bugs, gaps, intentional debt. Within each category, entries are sorted by **severity** (highest first). Each entry uses this shape:

```
### <ID> — <Title>
**Category:** Bug / Gap / Intentional debt
**Severity:** Critical / High / Medium / Low
**Status:** Open / In progress / Accepted / Resolved
**Discovered:** <YYYY-MM-DD>
**Description:** <one short paragraph>
**Workaround:** <one line, or "none">
**References:** <links to tasks, decisions, prior changelog entries>
```

**ID format.** Use `KI-N` (KI-1, KI-2, …) so IDs do not collide with task or decision IDs.

**Entry threshold.** Add an entry only when the issue, gap, limitation, blocker, or intentional debt must remain reconstructable across sessions. This file may provide evidence for a substantive Stage 13 route, but persistence alone does not make an issue Stage 13 work.

**Severity guidance.**

- **Critical:** blocks shipping or causes data loss.
- **High:** blocks a key journey or violates a stated commitment.
- **Medium:** affects a non-key journey or has a viable workaround.
- **Low:** cosmetic, minor friction, or affects a small audience.

**Status transitions.** A new issue starts at **Open**. It moves to **In progress** when a fix is being attempted, to **Accepted** if the project makes a meaningful choice not to fix it (with rationale logged in [`decisions.md`](decisions.md)), or to **Resolved** when fixed. Link the resolving task, review, pull request, change, or [`changelog.md`](changelog.md) entry; an ordinary fix does not require a decision.

**Evidence and proposals.** A bug report, validation note, or user complaint is evidence/event input until reviewed and added here. A proposed fix is not accepted project direction until it is recorded in the relevant artifact or decision.

> Resolved entries can be archived to the bottom of the file for readability, but do not delete them — the historical record matters.

---

## Bugs

> Persistent things that are broken. Includes regressions, mis-features, and behavior the project committed to but does not deliver when the issue remains relevant beyond the current correction pass.

### KI-1 — <Title>

**Category:** Bug
**Severity:** <Critical | High | Medium | Low>
**Status:** Open
**Discovered:** <YYYY-MM-DD>
**Description:** <one short paragraph>.
**Workaround:** <one line, or "none">.
**References:** <…>.

> Add new bug entries above this one in the file (most severe first); replace this template entry with a real one.

---

## Gaps

> Persistent things that are missing — capabilities scoped in but not yet built, or product expectations that need a documented place to live until the gap closes.

### KI-2 — <Title>

**Category:** Gap
**Severity:** <…>
**Status:** Open
**Discovered:** <YYYY-MM-DD>
**Description:** <…>.
**Workaround:** <…>.
**References:** <…>.

---

## Intentional debt

> Choices the project made deliberately — usually for speed — that are recorded so they do not silently calcify. Each entry should reference the [`decisions.md`](decisions.md) entry where the trade-off was accepted.

### KI-3 — <Title>

**Category:** Intentional debt
**Severity:** <…>
**Status:** Accepted
**Discovered:** <YYYY-MM-DD>
**Description:** <…>.
**Workaround:** <…>.
**References:** [`decisions.md`](decisions.md) DEC-<N>.

---

## Resolved (archive)

> Move resolved entries here so the active sections stay short. Each archived entry keeps its full record and adds a `Resolved:` date. Do not delete — the trail matters.

### KI-<N> — <Title>

**Category:** <…>
**Severity:** <…>
**Status:** Resolved
**Discovered:** <YYYY-MM-DD>
**Resolved:** <YYYY-MM-DD>
**Description:** <…>.
**References:** <resolving task, review, pull request, change, or [`changelog.md`](changelog.md) entry>.

---

## Optional sections

### A. Triaging cadence *(optional)*

> One short paragraph stating how often known issues are reviewed and by whom. For a solo MVP, "weekly self-review on Friday" is a valid answer — but it must be stated.

### B. Severity-1 response policy *(optional)*

> The response policy for Critical issues. Cross-references [`deployment.md`](deployment.md) §6 (incident response). Skip if covered there.

### C. Issue intake from outside the project *(optional)*

> If the project takes bug reports from external users, name the channel and how reports become entries here.
