# Decisions — Project template

> **Purpose.** Running log of meaningful decisions made about **this project** — accepted choices, overrides, deferrals, rejections, and tradeoffs concerning scope, architecture, intelligence-layer behavior, deployment, or other durable direction. The decisions log is the durable memory for "why is this project shaped this way?" Conversations are not the system of record; this file is.
>
> **Workflow phase.** Cross-cutting; use it when a phase produces a meaningful judgment that needs durable rationale, not as a required record for every phase or correction.
>
> **How to use this template.**
> - Replace `<…>` placeholders.
> - Keep blockquoted guidance (`>` lines) only at the top of the file as a how-to-read header; remove or replace before considering the artifact filled.
> - **Append-only.** Add new entries at the bottom. Do not edit accepted decisions in place — supersede them with a new entry that links back.
> - **Authority.** Accepted entries are canonical project memory. Proposed entries are not canonical until human review accepts them.
> - **Iteration.** Use a Stage 13 decision entry only for substantive post-acceptance learning that changes intent, scope, architecture, acceptance, launch treatment, or cross-stage direction. Reference persistent evidence in `known-issues.md` when it exists and name the re-entry stage.
> - **Ordinary correction.** Same-scope bugs, review remediation, maintenance, retry, and ordinary correction use task, review, pull-request, or change provenance. They do not require a decision entry unless meaningful judgment, acceptance, rejection, deferral, override, or tradeoff occurs.
> - **ID prefix.** Use `DEC-N` (DEC-1, DEC-2, …) so IDs do not collide with task IDs in [`tasks.md`](tasks.md) and the project keeps a stable, local sequence.
> - Stable headings — downstream skills rely on the entry shape.
> - **Profile applicability.** This artifact is **Required** for New Product Build, Existing Project Change, and Lightweight/Internal Build whenever meaningful project decisions, overrides, deferrals, or rationale exist.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This artifact is ready only when decisions are preserved in append-only form with context, decision, rationale, consequences, and references sufficient to reconstruct why the project changed. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/decisions.md`.
>
> **This file is the project-level decisions log.** Record only downstream project decisions here. Changes to BuildSolid's Framework or Project System source belong to BuildSolid's own governance and review process, not this project log.

Related artifacts: [`spec.md`](spec.md), [`plan.md`](plan.md), [`tasks.md`](tasks.md), [`architecture.md`](architecture.md), [`intelligence-layer.md`](intelligence-layer.md), [`mvp-scope.md`](mvp-scope.md), [`non-goals.md`](non-goals.md).

---

## How to read this file

Each decision uses this shape:

```
### DEC-<N> — <Title>
**Date:** YYYY-MM-DD
**Status:** Proposed / Accepted
**Context:** what prompted the decision.
**Decision:** what was decided.
**Rationale:** why.
**Consequences:** what this implies for downstream work.
**References:** links to spec/plan/tasks/architecture sections, prior decisions.
```

**ID format.** Use `DEC-N` for every entry. Do not reuse bare letter prefixes that could overlap with task IDs.

**Entry threshold.** Add an entry only when a human or accepted project process resolves a meaningful choice, override, deferral, rejection, or tradeoff whose rationale must survive across sessions. A routine validation result or same-scope correction is not a decision by itself.

**Authority state.** A `Proposed` entry is a reviewable proposal, not accepted project truth. It may inform discussion, but it cannot override accepted artifacts. A decision becomes canonical when human review accepts it and its status is changed to `Accepted`.

**Status transitions.** An accepted entry remains byte-preserved. To replace or revert it, append a new **Accepted** entry whose decision and `References` explicitly identify the earlier entry it supersedes or reverts. Current authority follows that later accepted entry; the earlier entry's original status remains historical truth.

**Append, do not rewrite.** New decisions go at the bottom. A later accepted entry records any supersession or revert; the original entry stays unchanged so future contributors can reconstruct the path.

---

## Entries

> Add new decisions below this line.

### DEC-1 — <Title>

**Date:** <YYYY-MM-DD>
**Status:** <Proposed | Accepted>
**Context:** <what prompted the decision>.
**Decision:** <what was decided, in one or two sentences>.
**Rationale:** <why this option was chosen over alternatives>.
**Consequences:** <what this implies for downstream work>.
**References:** <links to spec/plan/tasks/architecture sections, prior decisions>.

> Replace this template entry with the project's first real decision. Then append the next as `DEC-2`, and so on.

---

## Optional: current-authority index

> Most projects leave this section empty. If the log becomes long, it may link from an older decision to the later accepted entry that supersedes or reverts it. The index is navigation only and never changes an accepted entry's bytes or authority by itself.
