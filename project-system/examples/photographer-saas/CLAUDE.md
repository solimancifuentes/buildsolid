# CLAUDE.md — Photographer SaaS

This file describes Claude-Code-specific affordances that materially improve the experience of working on BuildSolid's photographer SaaS reference example in the Claude Code harness. The agent-neutral self-rules live in the paired [`AGENTS.md`](AGENTS.md). This file is **additive**: every Claude-Code-specific behavior described here has an agent-neutral fallback in `AGENTS.md`. The two files must stay in sync — no rule duplicated, none contradictory.

If this file ever conflicts with [`AGENTS.md`](AGENTS.md) or with the BuildSolid constitution (`framework/docs/constitution.md` in the BuildSolid repository), those win.

This is a **reference example**, not a real shipping product. See [`README.md`](README.md) §1 for the explicit stop-point.

---

## 1. Scope of this file

This file covers Claude-Code-specific affordances that materially improve the experience of working on the photographer SaaS example in the Claude Code harness.

Every Claude-Code-specific behavior described below has an agent-neutral fallback documented in [`AGENTS.md`](AGENTS.md) — none of these affordances are required to use this example on another agent.

For project self-rules that apply regardless of harness (read-first order, markdown-first artifacts, spec-before-implementation, edit-existing-artifacts, two-layer separation, decisions log, mode-shaped question density, agent-neutrality), read [`AGENTS.md`](AGENTS.md) first.

## 2. Authoring skills with `skill-creator`

Not applicable. This example **consumes** the BuildSolid skills — it does not author its own. The shipped skills (`project-system/skills/<name>/SKILL.md`) cover every phase the example walks. If a future revision of this example needed a custom project-specific skill, this section is the place to describe how Claude's `skill-creator` would be used; the agent-neutral fallback (authoring the `SKILL.md` by hand) is documented in `framework/docs/constitution.md` §5.

## 3. Human-in-the-loop with `AskUserQuestion`

When a human preference, intent, or decision is genuinely required while working on this example, use `AskUserQuestion` if it is available in the harness.

- Resolve and state profile and mode from the current instruction, the durable intake choice in [`founder-intent.md`](founder-intent.md) §6, or unambiguous accepted context. Use `AskUserQuestion` only when competing choices materially change the work. A resumed session may use a temporary posture without rewriting the durable intake choice.
- Follow the agent-neutral direct-skill and on-demand-orchestrator rule in [`AGENTS.md`](AGENTS.md) §6. This Claude-specific file adds no separate routing or session-preamble requirement.
- Do not ask when the answer can be inferred safely from existing artifacts ([`spec.md`](spec.md), [`plan.md`](plan.md), [`decisions.md`](decisions.md)) or recent context.
- **Agent-neutral fallback:** plain inline questioning, as defined in [`AGENTS.md`](AGENTS.md) §6.

Record meaningful human decisions in [`decisions.md`](decisions.md) regardless of how the question was asked.

## 4. Subagents

Subagents (`Agent` / `Task`) are useful when working on this example if:

- A research task spans many artifacts and would otherwise burn the main context window — for example, "find every place the image-suggestion capability is referenced across this directory."
- Independent reviews can run in parallel — for example, reviewing [`intelligence-layer.md`](intelligence-layer.md) and [`architecture.md`](architecture.md) against [`spec.md`](spec.md)'s acceptance criteria at the same time.

Treat subagent results as untrusted summaries. Verify changes the subagent claims to have made by reading the files. Subagents are an ergonomic aid — they do not change what the artifacts must contain.

**Agent-neutral fallback:** do the work in the main agent's context. Subagent use is never required to walk this example.

## 5. MCP tools, slash commands, and hooks

Claude-Code affordances — MCP tools, slash commands, hooks — are permitted and may improve the experience of working on this example. Guardrails:

- No MCP tool, slash command, or hook is the **only** path to use anything in this example. Every artifact in this directory is plain markdown and remains readable on any agent.
- The example's artifacts must remain useful even when none of these are available.
- Claude-Code-specific references do not appear in any agent-neutral artifact in this directory ([`spec.md`](spec.md), [`plan.md`](plan.md), [`tasks.md`](tasks.md), [`decisions.md`](decisions.md), the design / architecture / intelligence-layer files, etc.). They live here.
- **Agent-neutral fallback:** the underlying capability is described in plain markdown in the relevant artifact, executable by any competent agent.

This example requires no `.claude/settings.json` or custom Claude command. If a downstream copy introduces project-scoped Claude Code settings, document them here in one short paragraph and preserve an agent-neutral fallback.

## 6. Conductor workspaces

The example walks cleanly inside Conductor or in a single working tree. Per `framework/docs/constitution.md` §13, Conductor is **ergonomic**, not required.

- The example's artifact set must work for a single agent in a single workspace and for multiple agents collaborating across Conductor workspaces.
- An optional `.context/` directory is for inter-agent coordination notes only. Durable example artifacts (the files listed in [`README.md`](README.md) §2) **must not** live in `.context/`; they are the system of record and belong in this directory under version control.
- When two workspaces produce changes that touch the same example artifact, merge them in the main repo before continuing — no cross-workspace artifact merging in `.context/`.
- No artifact in this directory embeds a Conductor-only assumption.

**Agent-neutral fallback:** a single working tree on a developer's machine. Walking the example does not require Conductor.

## 7. Cross-references to AGENTS.md

To avoid duplication, this file points at [`AGENTS.md`](AGENTS.md) for everything else:

- Read-first order, markdown-first artifacts, spec-before-implementation, edit-existing-artifacts, decisions log: see [`AGENTS.md`](AGENTS.md) §1–§4, §8.
- Two-layer separation between this file and [`AGENTS.md`](AGENTS.md): see [`AGENTS.md`](AGENTS.md) §5.
- Mode-shaped question density rules: see [`AGENTS.md`](AGENTS.md) §6.
- Agent-neutrality of artifact contents: see [`AGENTS.md`](AGENTS.md) §7.
- When-in-doubt fallback: see [`AGENTS.md`](AGENTS.md) §9.

If you find yourself wanting to restate one of those rules here, stop — it belongs in [`AGENTS.md`](AGENTS.md), not in this file.

---

## Optional sections

### A. Project-specific Claude commands

Not applicable. The example defines no custom slash commands and depends on no parent command configuration.

### B. Project-specific subagent patterns

A useful recurring pattern when reviewing this example: spawn a subagent to walk the example end-to-end against [`spec.md`](spec.md) §10 acceptance criteria before merging a change to any single artifact. The agent-neutral path is the same review done in the main agent's context against the same checklist (see [`AGENTS.md`](AGENTS.md) §1 for the read-first order).

### C. MCP servers used by this example

Not applicable. The example does not depend on any MCP server. The *imagined* MVP that the artifacts describe would depend on an object-storage provider and a managed AI provider (see [`architecture.md`](architecture.md) §5 and [`intelligence-layer.md`](intelligence-layer.md) §2), but those are planned external dependencies of the spec, not MCP integrations. No credentials live anywhere in this directory.
