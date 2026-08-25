# CLAUDE.md — Project template

> **This is a BuildSolid project-level template.** Copy it into a downstream project built with BuildSolid and fill it in. It contains Claude-Code-specific downstream guidance paired with the project's [`AGENTS.md`](AGENTS.md); BuildSolid's agent-neutral rules remain in the public Framework and Project System.
>
> **Purpose.** This artifact records Claude-Code-specific project affordances and fallbacks while leaving agent-neutral project rules in [`AGENTS.md`](AGENTS.md).
>
> Once filled in, this file describes Claude-Code-specific affordances that materially improve the experience of working on **your project** in the Claude Code harness. The agent-neutral self-rules live in the paired [`AGENTS.md`](AGENTS.md). This file is **additive**: every Claude-Code-specific behavior described here has an agent-neutral fallback in `AGENTS.md`. The two files must stay in sync — no rule duplicated, none contradictory.
>
> **How to use this template.**
> - Replace `<project-name>` and any `<…>` placeholder with your project's value.
> - Keep the section headings stable; downstream skills rely on them.
> - Keep blockquoted guidance (lines starting with `>`) only while drafting — remove or replace it before considering the file filled.
> - If your project does not use Claude Code, delete this file. `AGENTS.md` is sufficient on its own.
> - **Profile applicability.** This artifact is **Need-triggered** for New Product Build and Existing Project Change when Claude-Code-specific project guidance is used or changed, and **Optional** for Lightweight/Internal Build.
> - **Section depth.** Numbered sections are required when this artifact is Required, Profile-triggered, or Need-triggered for the selected profile; optional sections stay optional unless project facts make them need-triggered.
> - **Semantic readiness.** This file is ready only when it contains Claude-Code-specific additions, links back to `AGENTS.md`, and documents agent-neutral fallbacks for every Claude affordance. Placeholder cleanup alone is not enough.
> - **Reference example fill:** `project-system/examples/photographer-saas/CLAUDE.md` in the BuildSolid repository shows a worked example of this template filled in for a freelance-photographer SaaS.

If this file ever conflicts with `AGENTS.md` or with the BuildSolid constitution (`framework/docs/constitution.md` in the BuildSolid repository), those win. The constitution and `AGENTS.md` are the authoritative layers; this file is the Claude-Code-specific layer on top.

---

## 1. Scope of this file

This file covers Claude-Code-specific affordances that materially improve the experience of working on **<project-name>** in the Claude Code harness.

Every Claude-Code-specific behavior described below has an agent-neutral fallback documented in [`AGENTS.md`](AGENTS.md) — none of these affordances are required to use this project on another agent.

For project self-rules that apply regardless of harness (read-first order, markdown-first artifacts, spec-before-implementation, edit-existing-artifacts, two-layer separation, decisions log, mode-shaped question density, agent-neutrality), read [`AGENTS.md`](AGENTS.md) first.

## 2. Authoring skills with `skill-creator` *(when applicable)*

> Most downstream BuildSolid projects do not author their own skills — they consume the skills shipped with BuildSolid. Keep this section only if your project authors its own custom skills.

When authoring or amending a project-specific skill, prefer Claude's `skill-creator` skill if it is available in the current harness.

- Use `skill-creator` to scaffold new `skills/<name>/SKILL.md` files in the `SKILL.md`-inside-a-folder shape.
- The resulting `SKILL.md` must remain plain markdown that conforms to the BuildSolid Skill Quality Standard and is readable on agents that lack `skill-creator`.
- **Agent-neutral fallback:** if `skill-creator` is unavailable, author the skill by hand following its conventions and the Skill Quality Standard sections.

## 3. Human-in-the-loop with `AskUserQuestion`

When a human preference, intent, authority, safety context, or another genuine prerequisite is missing and materially required for the requested outcome, use `AskUserQuestion` if it is available in the harness.

- Do not invoke `AskUserQuestion` merely because a session began or because the orchestrator is available. The orchestrator is on demand, not a mandatory profile/mode confirmation step; see `AGENTS.md` §6 for the agent-neutral routing, profile, and mode policy.
- Do not ask when the answer can be inferred safely from existing artifacts (`spec.md`, `plan.md`, `decisions.md`) or recent context.
- **Agent-neutral fallback:** plain inline questioning, as defined in [`AGENTS.md`](AGENTS.md) §6.

Record meaningful human decisions in `decisions.md` regardless of how the question was asked.

## 4. Subagents

Subagents (`Agent` / `Task`) are useful when:

- A research task spans many files and would otherwise burn the main context window (e.g., "find every place feature X is referenced across the project").
- Independent work can run in parallel (e.g., reviewing two unrelated subsystems against the project's spec).

Treat subagent results as untrusted summaries. Verify changes the subagent claims to have made by reading the files. Subagents are an ergonomic aid — they do not change what the artifacts must contain.

**Agent-neutral fallback:** do the work in the main agent's context. Subagent use is never required by this project.

## 5. MCP tools, slash commands, and hooks

Claude-Code affordances — MCP tools, slash commands, hooks — are permitted and may improve the experience of working on this project. Guardrails:

- Never let an MCP tool, slash command, or hook become the **only** path to use a project capability. Anything an agent must do should also be doable by reading the project artifacts and following them.
- The project's markdown artifacts must remain useful even when none of these are available.
- Do not embed MCP / slash / hook references into agent-neutral artifacts (`spec.md`, `plan.md`, `tasks.md`, `decisions.md`, design and architecture documents, etc.). They belong in this file and, when needed, in clearly-marked Claude-Code-specific sections of skill files.
- **Agent-neutral fallback:** the underlying capability is described in plain markdown in the relevant artifact, executable by any competent agent.

> If this project does configure project-scoped Claude Code settings (e.g., a `.claude/settings.json` with allowed tools or hooks), document them here in one short paragraph so a new collaborator understands what is configured and why. Do not duplicate the settings file content into this file.

## 6. Conductor workspaces *(optional)*

> Keep this section only if your team uses Conductor; delete it otherwise.

If this project is worked on inside Conductor, treat Conductor as **ergonomic**, not required.

- The project must work for a single agent in a single workspace and for multiple agents collaborating across Conductor workspaces.
- The `.context/` directory in each workspace is for inter-agent coordination notes — handoffs, scratch, who-owns-what. Durable project artifacts (the files in §1 of `AGENTS.md`) **must not** live in `.context/`; they are the system of record and belong in tracked project files.
- When two workspaces produce changes that touch the same artifact, merge them in the main repo before continuing — no cross-workspace artifact merging in `.context/`.
- Do not embed Conductor-only assumptions into the markdown artifacts. A reader on another machine without Conductor must see the same repo state.

**Agent-neutral fallback:** a single working tree on a developer's machine. No project capability requires Conductor.

## 7. Cross-references to AGENTS.md

To avoid duplication, this file points at [`AGENTS.md`](AGENTS.md) for everything else:

- Read-first order, markdown-first artifacts, spec-before-implementation, edit-existing-artifacts, decisions log: see `AGENTS.md` §1–§4, §8.
- Two-layer separation between this file and `AGENTS.md`: see `AGENTS.md` §5.
- Mode-shaped question density rules: see `AGENTS.md` §6.
- Agent-neutrality of artifact contents: see `AGENTS.md` §7.
- When-in-doubt fallback: see `AGENTS.md` §9.

If you find yourself wanting to restate one of those rules here, stop — it belongs in `AGENTS.md`, not in this file.

---

## Optional sections

The sections below are **optional**. Include them when your project genuinely needs them; remove them otherwise. Their headings remain stable so other BuildSolid skills can rely on them when present.

### A. Project-specific Claude commands *(optional)*

> Add custom slash commands the project relies on, with a one-line description of each and an agent-neutral fallback (what to do if the command is unavailable).

### B. Project-specific subagent patterns *(optional)*

> If the project benefits from a recurring subagent pattern (e.g., "spawn a reviewer for every PR touching the AI layer"), document the pattern here. Keep it short and point at the relevant `AGENTS.md` section for the agent-neutral path.

### C. MCP servers used by this project *(optional)*

> If the project relies on specific MCP servers (e.g., a project-managed knowledge base or a managed model provider), name them and their purpose here. Do not store credentials.
