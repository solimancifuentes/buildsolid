# AGENTS.md — Photographer SaaS

This file is the agent-neutral self-rules document for BuildSolid's photographer SaaS reference example: a minimalist SaaS for freelance photographers (gallery delivery, client selections, AI image suggestions). Any AI coding agent operating on this example reads this file before doing substantive work. Claude-Code-specific guidance lives in the paired [`CLAUDE.md`](CLAUDE.md). The two layers must stay in sync — no duplicated rule, no contradiction.

The governing document for BuildSolid itself is the BuildSolid constitution (`framework/docs/constitution.md` in the BuildSolid repository). Where BuildSolid's principles apply to this example, this file restates them in project terms; where this file and the constitution disagree, the constitution wins for anything claiming to be a BuildSolid artifact.

This is an **entirely synthetic reference example**, not a real person, research corpus, or shipping product. Maya, the other photographers, interviews, quotations, dates, measurements, permissions, source galleries, and observed-results language are illustrative scenario material. The example walks the BuildSolid workflow with worked artifacts; it does not produce code. See [`README.md`](README.md) §1 for the explicit stop-point.

---

## 1. Read first, in order

Before doing substantive work on this example, read its artifacts in this order:

1. [`README.md`](README.md) — the example's entry point and stop-point statement.
2. [`founder-intent.md`](founder-intent.md) — the synthetic Maya Chen persona, intended audience, and prospective success targets.
3. [`product-thesis.md`](product-thesis.md) — the compressed one-paragraph thesis.
4. [`mvp-scope.md`](mvp-scope.md) and [`non-goals.md`](non-goals.md) — what's in scope and what's explicitly not.
5. [`spec.md`](spec.md) — the spec the example's implementation would be checked against.
6. [`plan.md`](plan.md) — the implementation plan for the spec.
7. [`tasks.md`](tasks.md) — the would-build backlog (Stage 8 stops here for the reference example; later stages are artifact-level only).
8. [`decisions.md`](decisions.md) — running log of decisions made about this example.

If a referenced file does not yet exist for some reason, do only the current step and do not invent later artifacts. BuildSolid's workflow phases are listed in §3 below; agents should respect that order.

## 2. Markdown-first project artifacts

This example, like every BuildSolid project, keeps its **durable workflow artifacts** in markdown:

- Specs, plans, tasks, decisions, design notes, architecture, intelligence-layer notes, deployment notes, and launch checklists are markdown files in this directory.
- Diagrams are embedded as text (e.g., Mermaid) inside markdown when possible — see [`architecture.md`](architecture.md) §2.
- Non-markdown formats may be referenced from markdown but are not the primary carrier of any artifact in this example.

This rule covers the example's *workflow artifacts*. The example does not include product source code; if it ever did, the source language and format would be free, but the durable BuildSolid artifacts in §1 would still be markdown.

## 3. Spec before implementation

No code is written for a feature without a spec it can be checked against. This is BuildSolid's spec-before-implementation rule applied to this example.

- Authority for downstream behavior is the Framework constitution, the Framework context contract, accepted project decisions, the accepted spec, the plan, and then tasks, in that order. A lower source cannot override a higher one.
- [`tasks.md`](tasks.md) is the execution surface for an authorized downstream Build Mode run. Build Mode is not entered for this shipped example because it stops at the artifact level; the existence of a backlog does not grant implementation authority.
- If a real downstream implementation drifted from accepted artifacts, update the owning artifact first, append a decision only when the correction resolves a meaningful judgment or tradeoff, and then resume implementation.
- BuildSolid's workflow phases (Intake → Founder Discovery → Idea Compression → MVP Scope → UX Direction → Intelligence Layer → Technical Architecture → Spec Creation → Task Breakdown → Implementation → QA and Review → Deployment → Launch Prep → Iteration) are revisitable. Update existing artifacts in place; do not create parallel or versioned copies. Same-scope correction remains ordinary Existing Project Change unless accepted-state learning crosses the substantive Stage 13 threshold.

## 4. Edit existing artifacts; do not fragment

The example's artifact set is its canonical surface area.

- Prefer editing the existing files in this directory over creating new ones.
- If a needed concept has no existing artifact, propose adding one in [`decisions.md`](decisions.md) before inventing a new file.
- When iterating, update artifacts in place. A `spec-v2.md` next to `spec.md` is almost always wrong.

The example's artifact list is the one shown in [`README.md`](README.md) §2: founder-intent, discovery, product-thesis, problem-statement, mvp-scope, non-goals, user-journeys, design, intelligence-layer, architecture, spec, plan, tasks, deployment, launch-checklist, decisions, changelog, known-issues, plus this file and [`CLAUDE.md`](CLAUDE.md).

## 5. Two-layer separation: AGENTS.md vs CLAUDE.md

This example keeps two paired files at the project root:

- `AGENTS.md` (this file) — agent-neutral self-rules for any AI coding agent.
- [`CLAUDE.md`](CLAUDE.md) — Claude-Code-specific guidance and conventions.

The two must stay in sync but never duplicate each other or contradict each other. When you edit one, check the corresponding pair. Anything that is *not* Claude-Code-specific belongs here, not in `CLAUDE.md`.

If a downstream copy of this example does not use Claude Code, [`CLAUDE.md`](CLAUDE.md) can be deleted — but the rules in this file must still hold for whatever harness is in use.

## 6. Human-in-the-loop and mode

AI coding agents working on this example are collaborators, not autopilots.

- **Resolve and state the active profile and mode for the current work.** The durable intake choice is New Product Build in Founder Mode ([`founder-intent.md`](founder-intent.md) §6). Reuse it when current, or infer a temporary session posture from the current instruction and accepted artifacts. Ask only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output; persist only a durable cross-session change. BuildSolid supports four modes; one is always active:
  - **Guided** — ask freely; explain tradeoffs.
  - **Founder** — ask sharply; pressure-test the idea.
  - **Expert** — ask only when a decision materially changes the outcome.
  - **Build** — ask only when blocked.
  A resumed session may use a different stated posture without rewriting the durable intake choice.
- A focused BuildSolid skill may be invoked directly when its purpose matches, its genuine accepted inputs are current, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. Use the orchestrator on demand for routing or status, ambiguous entry, cross-stage coordination, missing cross-stage dependencies, continuity reconstruction, a material profile change, or substantive Stage 13 diagnosis; it is not a mandatory session preamble.
- When the human's preference, intent, authority, safety context, or another genuine prerequisite is missing and materially affects the outcome, **ask**. The agent-neutral fallback is plain inline questioning. Harness-specific clarification tooling is described in [`CLAUDE.md`](CLAUDE.md) for Claude Code.
- When the answer can be safely inferred from existing artifacts or recent context, **do not ask**. The artifacts in §1 are the system of record; if the answer is on disk, do not interrupt the user.
- **Irreversible or high-impact actions** — deletions, deployments, public posts, destructive git operations, sending external messages, changes to billing or authentication — require explicit human confirmation regardless of mode. The example does not exercise any of these.
- Every meaningful human decision is recorded in [`decisions.md`](decisions.md).

## 7. Stay agent-neutral by default

The artifacts in this directory must be readable and actionable by any competent AI coding agent.

- No Claude-Code-only assumption is embedded in any artifact in this directory (specs, plans, tasks, design, architecture, intelligence-layer, etc.). Claude-specific behavior, when used, is described in [`CLAUDE.md`](CLAUDE.md).
- Conductor-only assumptions are also avoided: this example walks for a single agent in a single working tree. Conductor is ergonomic, not required.
- The same rule applies to any other harness — no harness-only assumptions in artifact contents.

## 8. Decisions go in `decisions.md`

Every decision of consequence about this example — scope cuts, architecture choices, intelligence-layer tradeoffs, deployment-stop-point clarifications, accepted/rejected proposals — is recorded in [`decisions.md`](decisions.md).

- Append new entries at the bottom; do not rewrite accepted decisions in place.
- Supersede a decision with a new entry that links back.
- Conversations are not the system of record; artifacts are.
- Routine test, review, load, security, recovery, launch, and incident evidence belongs in task state, review or pull-request records, operational logs, or [`known-issues.md`](known-issues.md). Append a decision only for a meaningful accepted choice, exception, deferral, or tradeoff.

## 9. When in doubt

- Read the applicable Framework contract, then accepted [`decisions.md`](decisions.md) entries, [`spec.md`](spec.md), [`plan.md`](plan.md), and [`tasks.md`](tasks.md), in that order.
- If those are silent, infer and state the safest supported posture. Ask only when unresolved ambiguity could materially change scope, behavior, risk, acceptance, authority, safety, or another genuine prerequisite.
- Do not invent intent. Do not skip specs to ship implementation. Do not bury human-relevant decisions in chat.

---

## Optional sections

### A. Project-specific commands and workflows

Not applicable, because this example produces no code. There are no project-specific build, test, or lint commands. If a future iteration produces real source, this section is the place to capture any non-obvious invocations.

### B. External systems and references

The example's artifacts name external systems the *imagined* MVP would depend on (an object-storage provider for images and an unresolved managed AI provider for the image-suggestion capability — see [`architecture.md`](architecture.md) §5 and [`intelligence-layer.md`](intelligence-layer.md) §2). These are described as **planned** dependencies of the example's spec, not as live integrations. No credentials live anywhere in this directory.

### C. Project-specific guardrails

The example handles **client photographs** as its primary data class. A future implementation may send only downscaled image bytes and an opaque frame ID through the accepted, data-minimized provider/subprocessor boundary after the specific provider and dated written commitment are accepted; it must not send photographer, client, gallery, filename, metadata, or cost-attribution identity. Photographs must not leak into shared output, training data, or third-party analytics. The intelligence-layer artifact ([`intelligence-layer.md`](intelligence-layer.md) §4, §7) defines the boundary. Any wider flow is a guardrail violation and blocks the change.
