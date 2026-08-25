# AGENTS.md — Project template

> **This is a BuildSolid project-level template.** Copy it into a downstream project that has been built with BuildSolid and fill it in. It is **not** BuildSolid's own self-rules — those live at the root of the BuildSolid repository (`AGENTS.md`).
>
> **Purpose.** This artifact gives any AI coding agent the project-specific read-first order, operating rules, profile/mode expectations, and guardrails for working in this repository.
>
> Once filled in, this file is the agent-neutral self-rules document for **your project**. Any AI coding agent operating on the project repository should read it before doing substantive work. Claude-Code-specific guidance lives in the project's paired [`CLAUDE.md`](CLAUDE.md). The two layers must stay in sync — no duplicated rule, no contradiction.
>
> **How to use this template.**
> - Replace `<project-name>` and any `<…>` placeholder with your project's value.
> - Keep the section headings stable; downstream skills rely on them.
> - Keep blockquoted guidance (lines starting with `>`) only while drafting — remove or replace it before considering the file filled.
> - Do not add or retain content solely to prove that something is inapplicable. Inside an applicable artifact, `N/A - reason: <reason>` remains valid when omitting a material field or section would otherwise be surprising, ambiguous, or consequential.
> - **Profile applicability.** This artifact is **Need-triggered** for New Product Build, Existing Project Change, and Lightweight/Internal Build when project agent rules are missing, stale, or changed.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This file is ready only when it gives agent-neutral read-first order, project rules, profile/mode expectations, decision-recording rules, and project-specific guardrails without embedding one-harness-only assumptions. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/AGENTS.md` in the BuildSolid repository shows a worked example of this template filled in for a freelance-photographer SaaS.

The governing document for BuildSolid itself is the BuildSolid constitution (`framework/docs/constitution.md` in the BuildSolid repository). Where BuildSolid's principles apply to your project, this file restates them in project terms; where this file and the constitution disagree, the constitution wins for anything claiming to be a BuildSolid artifact.

---

## 1. Read first, in order

Before doing substantive work on this repository, an AI coding agent should identify the current applicable lifecycle slice and read the applicable artifacts that are already present, in this order. Replace each filename with the path used in your repository if it differs.

1. `README.md` — the project entry point.
2. `founder-intent.md` — why this project exists, for whom, what success looks like.
3. `product-thesis.md` — the compressed one-paragraph thesis.
4. `mvp-scope.md` and `non-goals.md` — what's in scope and what's explicitly not.
5. `spec.md` — the spec the implementation works against.
6. `plan.md` — the implementation plan for the spec.
7. `tasks.md` — the buildable backlog.
8. `decisions.md` — running log of project decisions and their rationale.

> Skip a file that is absent or outside the applicable slice; do not create an artifact or N/A placeholder merely to complete this list. If an absent file is a genuine prerequisite for the requested work, stop or route to produce it before continuing. BuildSolid's workflow phases are listed in §3 below; agents should respect that order.

## 2. Markdown-first project artifacts

BuildSolid projects keep their **durable workflow artifacts** in markdown:

- Specs, plans, tasks, decisions, design notes, architecture, intelligence-layer notes, deployment notes, and launch checklists are markdown files in this repository.
- Diagrams are embedded as text (e.g., Mermaid) inside markdown when possible.
- Non-markdown formats may be referenced from markdown but should not be the primary carrier of any project artifact.

> This rule covers your project's *workflow artifacts*, not its product code. Your application's source code can be in any language and any format that fits the project. The artifacts in §1 are the durable memory of the project; treat them that way.

## 3. Spec before implementation

No code is written for a feature without a spec the implementation can be checked against. This is BuildSolid's spec-before-implementation rule applied to your project.

- `spec.md` and `plan.md` must exist and be current before substantive implementation begins.
- `tasks.md` must exist before any agent claims to be in **Build Mode** (see §6).
- If implementation drifts from the spec, update the spec **first**, log the rationale in `decisions.md`, then continue. "It was easier to just code it" is not a valid reason to skip a spec.
- BuildSolid's workflow phases (Intake → Founder Discovery → Idea Compression → MVP Scope → UX Direction → Intelligence Layer → Technical Architecture → Spec Creation → Task Breakdown → Implementation → QA and Review → Deployment → Launch Prep → Iteration) are revisitable. When you revisit a phase, **update the existing artifact in place** — do not create parallel or versioned copies.

## 4. Edit existing artifacts; do not fragment

The project's artifact set is its canonical surface area.

- Prefer editing existing artifacts over creating new ones.
- If a needed concept has no existing artifact, propose adding one in `decisions.md` before inventing a new file.
- When iterating, update artifacts in place. A second `spec-v2.md` is almost always wrong.

> The list of artifacts your project may produce is the list referenced in §1 plus the design/architecture/intelligence-layer set (`design.md`, `architecture.md`, `intelligence-layer.md`), the deployment/launch set (`deployment.md`, `launch-checklist.md`), and the living-state pair (`changelog.md`, `known-issues.md`). The BuildSolid context package documents the full canonical list.

## 5. Two-layer separation: AGENTS.md vs CLAUDE.md

This project keeps two paired files at the project root:

- `AGENTS.md` (this file) — agent-neutral self-rules for any AI coding agent.
- `CLAUDE.md` — Claude-Code-specific guidance and conventions.

The two must stay in sync but never duplicate each other or contradict each other. When you edit one, check the corresponding pair. Anything that is *not* Claude-Code-specific belongs here, not in `CLAUDE.md`.

> If your project does not use Claude Code, you may delete `CLAUDE.md`. Keep any other harness-specific guidance in its own clearly named host file (for example, `CODEX.md`) with an agent-neutral fallback here. Do not absorb harness-specific instructions into this agent-neutral file.

## 6. Human-in-the-loop, profile, and mode

AI coding agents working on this project are collaborators, not autopilots.

- **Resolve and state the active project profile.** Use the explicit current instruction, then an accepted durable project choice, then unambiguous current context. BuildSolid Development supports exactly three profiles:
  - **New Product Build** — starting a new product, MVP, or major product direction.
  - **Existing Project Change** — changing an existing project, feature, workflow, codebase, or accepted artifact set.
  - **Lightweight/Internal Build** — building a small internal tool, library, experiment, one-off utility, non-public workflow, or low-ceremony build.
- State a safe profile inference and its reason. Ask only when competing profiles would materially change workflow depth, behavior, risk, scope, acceptance, or output.
- AI-native work is not a standalone profile. If AI is load-bearing in any profile, the Intelligence Layer work applies inside the selected profile.
- A focused BuildSolid skill may be invoked directly when its purpose matches, its genuine accepted inputs are current, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. Use the orchestrator on demand for routing or status, ambiguous entry, cross-stage coordination, missing cross-stage dependencies, continuity, a material profile change, or substantive iteration diagnosis; it is not a mandatory session preamble.
- **Resolve and state the active mode** from the explicit current instruction, an accepted durable project choice, or unambiguous current context. Profiles describe the shape of the work; modes describe how the agent behaves with the human. Every profile can run in any appropriate mode. BuildSolid supports four modes; one is always active:
  - **Guided** — ask freely; explain tradeoffs.
  - **Founder** — ask sharply; pressure-test the idea.
  - **Expert** — ask only when a decision materially changes the outcome.
  - **Build** — ask only when blocked.
- Persist a profile or mode only when the human deliberately makes it a durable cross-session project choice. Ordinary session posture is stated in the interaction and is not silently written into project artifacts; record a meaningful durable choice or override in `founder-intent.md` §6 and, when consequential, `decisions.md`.
- When the human's preference, intent, authority, safety context, or another genuine prerequisite is missing and the gap could materially change the outcome, **ask** rather than guess. The agent-neutral fallback is plain inline questioning. Harness-specific clarification tooling (e.g., a structured question API) is described in `CLAUDE.md` for Claude Code; other harnesses use whatever clarification tooling they provide.
- When the answer can be safely inferred from existing artifacts or recent context, **do not ask**. Do not interrupt experts with questions whose answers are already on disk.
- **Unresolved founder choices and irreversible or high-impact actions** — including deletions, deployments, public posts, destructive git operations, sending external messages, changes to billing or authentication — require explicit human confirmation regardless of mode. Do not infer authority from an accepted artifact, prior task, review, or completed prerequisite.
- Every meaningful human decision is recorded in `decisions.md`.

## 7. Stay agent-neutral by default

The artifacts in this repository must be readable and actionable by any competent AI coding agent.

- Do not embed Claude-Code-only assumptions into the project artifacts (specs, plans, tasks, design, architecture, etc.). Claude-specific behavior, when used, must be **additive**: the artifact must still be usable on a different agent, possibly with reduced ergonomics.
- Claude-Code-only conventions belong in `CLAUDE.md`, with a documented agent-neutral fallback.
- The same rule applies to any other harness — no harness-only assumptions in artifact contents.

## 8. Decisions go in `decisions.md`

Every decision of consequence about this project — scope changes, architecture choices, intelligence-layer tradeoffs, deployment choices, accepted/rejected proposals — is recorded in `decisions.md`.

- Append new entries at the bottom; do not rewrite accepted decisions in place.
- Supersede a decision with a new entry that links back.
- Conversations are not the system of record; artifacts are. Information that lives only in chat is information that will be lost.

## 9. When in doubt

- Read the project's `spec.md`, `plan.md`, and `decisions.md`.
- If those are silent, read the corresponding BuildSolid governing documents in the BuildSolid repository (`framework/docs/context-package.md`, `framework/docs/constitution.md`).
- If both are silent and missing preference, intent, authority, safety context, or another genuine prerequisite could materially change the outcome, **ask** using whatever clarification tooling your harness provides, with plain inline questioning as the agent-neutral fallback. Otherwise state the safest reasonable inference and continue.
- Do not invent intent. Do not skip specs to ship implementation. Do not bury human-relevant decisions in chat.

---

## Optional sections

The sections below are **optional**. Include them when your project genuinely needs them; remove them otherwise. Their headings remain stable so other BuildSolid skills and templates can rely on them when present.

### A. Project-specific commands and workflows *(optional)*

> Add only commands and workflows that are uncommon enough that an agent would not infer them. Examples: a non-standard test invocation, a project-specific pre-commit step, a domain-specific lint. Do not list generic commands.

### B. External systems and references *(optional)*

> If this project depends on external systems (a hosted database, a vector store, a third-party API, a managed AI provider), point at them here with one-line descriptions and where credentials live. Do not put credentials themselves in this file or anywhere in the repository.

### C. Project-specific guardrails *(optional)*

> Risks unique to this project — domains where mistakes are expensive (regulated industries, payment flows, data privacy boundaries, content moderation). State the rule and why; let the agent apply judgment from there.
