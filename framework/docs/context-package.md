# BuildSolid — Context Package

> Read the sections relevant to the current task before substantive work. This is the canonical, agent-neutral BuildSolid context package; applicable project guidance may require additional task-specific sources.

---

## 1. What BuildSolid is

**BuildSolid** is a **software factory framework and intelligence layer for building real software with AI**. It gives solo founders, designers, engineers, curious builders, and AI coding agents a shared way to turn product intent into durable artifacts before and during implementation.

BuildSolid guides a user from raw idea to production-ready MVP artifacts through a structured, end-to-end workflow:

discovery → spec-driven development → minimalist UX → architecture planning → intelligence layer design → task breakdown → implementation → QA → deployment → launch prep → iteration.

BuildSolid is **not** a generic prompt pack, a chatbot wrapper, or a list of tips. It is the framework and intelligence layer for building real projects with AI agents — opinionated about phases, artifacts, handoffs, AI behavior, and decision memory, while remaining flexible about the user's experience level and pace.

The canonical identity reference lives at [`framework/docs/brand/BUILD_SOLID_CANONICAL.md`](brand/BUILD_SOLID_CANONICAL.md).

### What BuildSolid is *not* (canonical)

- Not an IDE.
- Not a CLI.
- Not a web app.
- Not a deployment platform.
- Not a no-code app builder.
- Not an npm/pip package.
- Not a generic AI wrapper.
- Not a simple prompt pack.
- Not a vibe-coding tool.
- Not an automation/orchestration runtime.
- Not a hosted service.
- Not a replacement for Cursor, Claude Code, Lovable, Base44, Bolt, Replit, GitHub, Supabase, Vercel, or comparable tools.

BuildSolid is **Markdown-first and skill-first**. We prove the workflow before we build tools around it.

---

## 2. Target users

BuildSolid must be useful for all of the following, without forcing any of them into the wrong shape:

- **Beginners / curious builders** — need explanation, scaffolding, and gentle pacing.
- **Designers** — care deeply about UX direction, flows, and minimalism.
- **Engineers** — want speed, defaults, and the ability to skip hand-holding.
- **Solo founders** — need product thinking, scope discipline, and launch readiness, not just code.

The same workflow should serve all four. The **mode** the user is in (see §5) is what changes how the agent behaves.

---

## 3. Platform strategy

- **Built for Claude Code first.** Skills, slash-style invocations, and file conventions assume the Claude Code harness as the primary surface.
- **Used inside Conductor.** BuildSolid is designed to feel native when run as one or more parallel Conductor agents inside a workspace.
- **Portable beyond Claude Code.** BuildSolid artifacts must remain portable to Codex, GitHub Copilot, Spec Kit, and other AI coding agents. Keep this portability in mind: avoid Claude-Code-only assumptions in the markdown templates and skill *contents* (the harness wiring can be Claude-specific, the artifacts should not be).

---

## 4. Core principles

These are non-negotiable. When in doubt, fall back to them.

1. **Founder intent comes before code.** Understand *why* the project exists and *who it's for* before writing or generating anything.
2. **Specs come before implementation.** No code without a spec. No spec without scoped intent.
3. **Minimalist MVPs come before full SaaS platforms.** The first build should be the smallest thing that proves the thesis. Cut, then cut again.
4. **AI is an intelligence layer, not just a feature.** Treat AI capabilities as a designed system layer with its own architecture, prompts, evals, fallbacks, and cost model — not as a sprinkle of "AI features."
5. **Multiple modes, one workflow.** The phases don't change; the agent's behavior does (see §5).
6. **Useful for beginners, designers, engineers, and solo founders.** No phase should be exclusionary.
7. **Ask when needed; move fast when not.** Experts should not be slowed down by mandatory questionnaires.
8. **Prove the workflow before tooling it.** BuildSolid is Markdown + skills. Do not build a CLI, package, web app, or automation layer.

---

## 5. Supported modes

Every BuildSolid interaction runs in exactly one mode. The mode shapes question density, assumption-making, explanation depth, challenge level, execution bias, and stop/escalation behavior. It does **not** change the underlying phases, project profile, artifact vocabulary, authority model, or quality bar.

The four supported interaction modes are:

1. **Guided Mode** — Walks the user through each phase step by step. Explains tradeoffs in plain language. Default for beginners.
2. **Founder Mode** — Challenges the idea like a sharp startup office-hours session. Pushes on problem clarity, audience, willingness to pay, and differentiation before any building.
3. **Expert Mode** — Makes reasonable defaults and assumptions, moves quickly, surfaces only the decisions that materially change outcomes. Default for experienced engineers/designers.
4. **Build Mode** — Executes against existing specs (`spec.md`, `plan.md`, `tasks.md`). Only stops to ask the user when genuinely blocked.

Resolve the active mode from explicit current instruction, an accepted current project choice, or unambiguous context. State a safe inference and ask only when competing modes would materially change behavior, risk, scope, acceptance, or output. Persist the mode only when it is a durable cross-session project choice; ordinary session posture does not require an artifact update.

### Central mode policy

The central mode policy below applies to every BuildSolid skill unless a skill's §5 states a narrower, skill-specific delta that remains consistent with the shared behavior.

| Mode | Question density | Assumption-making | Explanation depth | Challenge level | Execution bias | Stop/escalation behavior |
|---|---|---|---|---|---|---|
| **Guided Mode** | Higher density, asked in small batches. Ask freely when the answer teaches the user or materially shapes the artifact. | Make few silent assumptions. Offer a clear default when useful, but confirm important choices. | Explain the purpose of each phase, artifact, and tradeoff in plain language. | Supportive but honest; challenge gently and explain why the challenge matters. | Teach while progressing. Slow enough for comprehension, but still produce or update artifacts. | Stop for unclear intent, missing user preference, contested decisions, or any irreversible/high-impact action. |
| **Founder Mode** | Medium to high density, focused on sharp leverage questions rather than questionnaires. | Assume less about market, audience, willingness to pay, differentiation, and scope. Force weak claims into explicit assumptions. | Explain only enough to make the pressure test actionable. | Highest challenge level. Push on problem severity, audience specificity, wedge, non-goals, and false certainty. | Pressure-test before producing downstream artifacts. Cut scope aggressively when the thesis does not justify it. | Stop when founder intent, audience, problem, willingness to pay, or differentiation is too weak to support the next phase. Escalate consequential product-direction decisions to `decisions.md`. |
| **Expert Mode** | Low density. Ask only when the decision materially changes outcome, risk, scope, architecture, acceptance, or review. | Make reasonable defaults from accepted artifacts and current context. Surface assumptions that carry meaningful risk. | Concise. Explain decisions and tradeoffs only where they affect the work. | Direct and selective. Challenge contradictions, weak evidence, or over-scoped choices without re-running beginner discovery. | Move quickly from accepted inputs to artifact updates, reviews, or routing decisions. | Stop for material ambiguity, authority conflicts, missing accepted inputs, founder-gated choices, or high-impact actions. Do not stop for questions already answered on disk. |
| **Build Mode** | Minimal density. Ask only when blocked. | Use `spec.md`, `plan.md`, `tasks.md`, accepted decisions, and required artifacts as the source of truth. Do not invent missing acceptance criteria. | Minimal and operational. State blocker, assumption, change, or verdict. | Narrow challenge level. Challenge only when implementation would violate the spec, tasks, constitution, accepted decisions, or safety/security expectations. | Execute against existing specs and tasks. Avoid rediscovery, redesign, or scope expansion. | Stop when required build inputs are missing or conflicting, when work would drift from accepted artifacts, when a founder gate is triggered, or before destructive/high-impact actions. |

Profiles are separate from modes. A **New Product Build**, **Existing Project Change**, or **Lightweight/Internal Build** can run in any appropriate mode. Profiles select workflow depth and artifact expectations; modes select how the agent behaves with the human.

### Shared policy vs per-skill deltas

The central mode policy owns behavior that should not be redefined differently by each skill:

- the four mode names and their meanings;
- baseline question density;
- assumption-making posture;
- explanation depth;
- challenge level;
- execution bias;
- stop and escalation behavior;
- the separation between modes and project profiles.

A skill's §5 owns only the **delta** needed for that skill's job. Good per-skill deltas state:

- what this skill does differently in each mode;
- which artifact or decision the mode behavior affects;
- which questions are unique to this phase or artifact;
- which material ambiguities or genuine prerequisites justify a question in this phase;
- what the skill must refuse, defer, or escalate in that mode.

Per-skill deltas must not rename, merge, remove, or add modes; redefine project profiles; weaken the central stop/escalation behavior; silently promote proposed knowledge to accepted state; or duplicate this policy at length.

### Skill §5 authoring and maintenance pattern

When an accepted scoped change updates a skill's §5, use this pattern:

1. Keep the existing `## 5. Mode behavior` heading required by the Skill Quality Standard.
2. Add a short lead sentence: "This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas."
3. Preserve all four mode bullets, in any order that makes the skill's primary mode clear.
4. Replace generic restatements of Guided / Founder / Expert / Build behavior with phase-specific deltas.
5. Keep concrete artifact outputs, refusal rules, material question triggers, and escalation triggers that are meaningful for the skill. Do not set numeric question quotas.
6. If a skill has no meaningful delta for a mode, state the minimal delta rather than deleting the mode.
7. Do not perform a suite-wide skill migration without an accepted scoped task authorizing that exact treatment.

## 5A. Development project profiles

BuildSolid Development uses one of three project profiles to choose the right workflow depth. Profiles describe the shape of the project work. They are separate from the interaction modes in §5, which describe how the agent behaves with the human.

| Profile | Use when | Workflow effect |
|---|---|---|
| **New Product Build** | The user is starting a new product, MVP, major product direction, or similarly scoped new release. | Uses the full Development lifecycle by default. Record an actual conditional-stage decision or material deviation when it matters; an empty fourteen-row ledger is not required. |
| **Existing Project Change** | The user is changing an existing project, feature, workflow, codebase, or accepted artifact set. | Starts from existing accepted artifacts and code. Avoids full rediscovery unless the change alters intent, audience, or product direction. Requires impact analysis before tasks. |
| **Lightweight/Internal Build** | The work is a small internal tool, library, experiment, one-off utility, non-public workflow, or low-ceremony build. | Uses the smallest proportionate lifecycle slice, smaller task decomposition, and no empty artifact solely to record inapplicability. |

Resolve the profile from explicit current instruction, an accepted current project choice, or unambiguous context. State the profile and a brief reason. Ask the human only when competing profiles materially change workflow depth, risk, scope, acceptance, or output. Record only a durable cross-session profile choice or a material override in `decisions.md`; ordinary session posture is not silently persisted.

Every profile can run in any appropriate mode: Guided, Founder, Expert, or Build. Do not rename, merge, or replace the four interaction modes when selecting a profile.

AI-native work is not a standalone profile. If AI is load-bearing in any profile, the Intelligence Layer stage and AI-specific validation depth apply inside the selected profile.

---

## 5B. Lifecycle contracts by profile

The three project profiles are defined in §5A. This section does **not** redefine them; it defines only the **lifecycle behavior each profile selects**. The §6 stage list, order, and stage names are identical for every profile. A run uses the **applicable lifecycle slice**: the smallest ordered set of stages, artifacts, genuine prerequisites, validations, and gates needed to reach the requested outcome from accepted current state. Profiles change depth and applicability, never stage order or names, and introduce no numeric risk tiers or scores.

### Stage applicability by profile

The table gives the **default** applicability of each §6 stage per profile. It is a compatibility and routing map, not a required per-run ledger. States are qualitative:

- **Required** — normally produced or updated for this profile.
- **Conditional** — applicability depends on the specific work and is decided when the stage or a downstream dependency matters.
- **Commonly N/A - reason** — usually not applicable for this profile; record a reason only when omission would otherwise be surprising, ambiguous, or consequential.

| Stage | New Product Build | Existing Project Change | Lightweight/Internal Build |
|---|---|---|---|
| 0 Intake | Required | Required | Required |
| 1 Founder Discovery | Required | Conditional | Conditional |
| 2 Idea Compression | Required | Conditional | Conditional |
| 3 MVP Scope | Required | Conditional | Conditional |
| 4 UX Direction | Required | Conditional | Commonly N/A - reason |
| 5 Intelligence Layer | Conditional | Conditional | Conditional |
| 6 Technical Architecture | Required | Conditional | Conditional |
| 7 Spec Creation | Required | Required (after impact analysis) | Required |
| 8 Task Breakdown | Required | Required (after impact analysis) | Required |
| 9 Implementation | Required | Required | Required |
| 10 QA and Review | Required | Required | Conditional |
| 11 Deployment | Required | Conditional | Commonly N/A - reason |
| 12 Launch Prep | Required | Conditional | Commonly N/A - reason |
| 13 Iteration | Conditional | Conditional | Conditional |

Stage 5 (Intelligence Layer) is Required in any profile where AI is load-bearing. When it is not load-bearing, no intelligence-layer artifact is created solely to record N/A; use `N/A - reason` only when the omission needs durable explanation. The defaults above are starting points, not gates. Profile selection follows §5A.

**Conditional does not mean silently skipped.** Where a Conditional stage applies, it runs at a depth proportionate to the selected profile. For Lightweight/Internal Build, QA and Review remain Conditional, but a proportionate review — including security where relevant — is still expected whenever the work creates that risk. Record an omission when it is material; do not create an empty placeholder to prove it.

### The `N/A - reason` compatibility rule

When a stage- or artifact-specific omission needs durable explanation, record:

`N/A - reason: <specific one-line reason>`

(ASCII hyphen; this remains the canonical compatibility token.) The reason must let a fresh agent understand why the item is inapplicable. A recorded `N/A - reason` remains a **satisfied** state for progression. Existing verbose matrices remain valid, but new work does not need a row or artifact for every omission. A compact **material exclusions** list is also valid. Record a `decisions.md` entry only when the exclusion itself is a meaningful accepted choice or materially changes workflow depth.

### Direct focused-skill entry

A focused skill may be invoked directly when its purpose matches the requested outcome, its genuine accepted prerequisites are current, profile and mode are safely resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. Otherwise use **Block** or **Route** under §8D, including route to the orchestrator when coordination is needed. Existing orchestrator-first use remains valid; direct invocation is additive and requires no migration.

### Brownfield entry and re-entry (Existing Project Change)

The Existing Project Change profile does not restart at fresh discovery. Its path is:

1. **Existing-state read** — read the already-accepted artifacts (§8) and code rather than rediscovering them.
2. **Impact analysis before tasks** — identify the direction-test result, entry stage, affected artifacts or stages, required downstream gates, and material exclusions. This is a **gate before Stage 8 (Task Breakdown)**: tasks are not produced until the impact is clear in current accepted artifacts.
3. **Enter at the appropriate stage** for the change's blast radius (for example, a spec-only change re-enters at Stage 7; a UX change at Stage 4). Do not create rows for unaffected upstream stages unless a material exclusion needs explanation.
4. **Update accepted artifacts in place** — no parallel copies.
5. **Full rediscovery (Stages 1–2) applies only** when the change alters intent, audience, or product direction.

This same path is the destination of the Stage 13 re-entry loop. The impact-analysis procedure that makes this path actionable is defined in §8E.

### Stage 9 — Implementation support

Stage 9 (Implementation) is markdown-only support. BuildSolid does **not** generate code, scaffold projects, or add scripts at this stage (`framework/docs/constitution.md` §15). The lifecycle contract for Stage 9 is:

- BuildSolid provides markdown guidance for execution context, handoffs, drift detection between code and the accepted `spec.md` / `plan.md` / `tasks.md`, recovery, and completion expectations.
- A direct caller or the orchestrator hands control to **Build mode** for the build itself. Routing or orchestration re-engages at **Stage 10 (QA and Review)** only when needed.

The detailed implementation-support procedure is defined in §8E.

### Stage 13 — Iteration loop

Stage 13 (Iteration) is a complete feedback and re-entry loop for substantive post-acceptance learning that changes intent, scope, architecture, acceptance, launch treatment, or cross-stage direction. Its steps are:

observe → record evidence → evaluate → diagnose → propose → test → human review → accept or reject → update artifacts in place → validate.

Feedback re-enters the relevant earlier stage through the brownfield re-entry path above; artifacts are updated in place, and a decision is recorded when acceptance, rejection, or a material tradeoff requires durable rationale. Same-scope bugs, review remediation, maintenance, and routine retry are **not** Stage 13; they remain ordinary Existing Project Change work against unchanged acceptance criteria. The detailed iteration procedure is defined in §8E.

### Deferred to later tasks

This section defines stage-level lifecycle contracts only. The required, optional, profile-triggered, and need-triggered **artifact matrix** and the per-artifact **semantic readiness criteria** are defined in §8A and §8B. The **authority and memory states** and conflict-precedence chain are defined in §8C. The Existing Project Change impact-analysis procedure, Stage 13 iteration procedure, and Stage 9 implementation-support procedure are defined in §8E.

---

## 6. Core flow

BuildSolid keeps these phases in exact order as its stable lifecycle map. New Product Build uses the full flow by default. Existing Project Change and Lightweight/Internal Build may enter at the earliest affected stage and execute only the applicable slice established under §5B; this is routing from accepted state, not a reorder of the lifecycle.

0. **Intake** — capture the raw idea and the user's mode/context.
1. **Founder Discovery** — who, why, what's the wedge.
2. **Idea Compression** — reduce to a one-paragraph product thesis.
3. **MVP Scope** — what's in, what's explicitly out.
4. **UX Direction** — minimalist flows, key screens, tone.
5. **Intelligence Layer** — where AI lives, what it does, what it must not do.
6. **Technical Architecture** — stack, services, data, boundaries.
7. **Spec Creation** — `spec.md` + `plan.md` ready to hand to a builder.
8. **Task Breakdown** — `tasks.md` of small, verifiable units.
9. **Implementation** — code against the specs and tasks.
10. **QA and Review** — functional, design, and security review.
11. **Deployment** — environments, secrets, rollout.
12. **Launch Prep** — positioning, page, first users, metrics.
13. **Iteration** — feedback loop into earlier phases.

Each applicable phase produces or updates durable state when the outcome requires it. Do not create an empty artifact solely to prove that a phase was omitted.

---

## 7. Skill system

The BuildSolid skill system. Each skill is a Markdown-defined capability that an agent can invoke. Focused skills may be invoked directly when their genuine prerequisites exist; the orchestrator composes routing when entry or cross-stage coordination is ambiguous.

| Skill | Purpose |
|---|---|
| `buildsolid-orchestrator` | On-demand router. Resolves mode/profile, identifies the current phase when routing is needed, delegates, and maintains cross-stage continuity. |
| `founder-discovery` | Powers Founder Mode. Pressure-tests the idea, audience, problem, and differentiation. |
| `idea-compressor` | Reduces a sprawling idea into a tight product thesis and problem statement. |
| `mvp-scope` | Defines the smallest valuable build. Forces explicit non-goals. |
| `ux-minimalist` | Drives UX direction toward fewer screens, fewer states, clearer flows. |
| `intelligence-layer-architect` | Designs the AI layer: capabilities, prompts, models, evals, fallbacks, costs, safety. |
| `technical-planner` | Picks stack and produces `architecture.md`. |
| `spec-planner` | Produces and maintains `spec.md` and `plan.md` in a Spec Kit-compatible shape. |
| `starter-stack-advisor` | Opinionated minimal default stack for solo builders (used when the user wants a default, not a debate). |
| `task-breakdown` | Turns specs/plans into a concrete, verifiable `tasks.md`. |
| `qa-reviewer` | Reviews implementation against specs and acceptance criteria. |
| `security-reviewer` | Reviews changes for common security issues, secrets, and AI-layer risks. |
| `deployment-manager` | Plans and executes environment setup, secrets, and rollout. |
| `launch-prep` | Drives positioning, landing page, first-user plan, and key metrics. |

Skills remain **Markdown-first**. Host-provided wiring is optional and no runtime wiring is required.

### 7A. Skills, roles, agents, agent instances, workflows, and policies

BuildSolid uses a small, deliberately flat vocabulary to describe **how the workflow is executed**. These terms name execution concepts; they are **not** new canonical lifecycle units, artifacts, or runtime components. They do not change the §6 stages, the §8 artifacts, the §5 modes, the §5A/§5B profiles, the §8D gating policy, or the §8E routing workflow. The model exists so a fresh agent reads one definition of these words instead of inferring a heavier, persona-driven or service-driven shape.

#### Definitions

| Term | What it means in BuildSolid | Example |
|---|---|---|
| **Skill** | A reusable Markdown instruction module — a procedure or capability an agent reads and applies. A skill is instructions, not an actor; it does not run on its own. | the 14 skills in §7, e.g. `mvp-scope`, `qa-reviewer` |
| **Role** | A responsibility, perspective, review lens, or authority boundary — **not necessarily a separate agent**. | "the security-review lens"; "the founder's authority over product direction" |
| **Agent** | A model plus tools that executes instructions: the worker that reads skills, runs workflows, and produces or updates artifacts, working within a context, objective, outputs, and escalation rules. | one competent AI coding agent running BuildSolid |
| **Agent instance** | A concrete execution of an agent in a specific harness, session, workspace, or working tree. Agent instances are working-context (§8C) and non-canonical. | one Claude Code session in one Conductor workspace |
| **Workflow** | An ordered procedure — sequencing, branching, human gates, validation, synthesis, handoff. | the §8E routing workflow; the §5B Stage 13 iteration loop |
| **Policy** | A reusable behavioral rule that governs how skills and workflows behave. | the §5 mode policy; the §8C authority/memory model; the §8D readiness/gating policy; the §8E routing workflow as a routing policy |

#### How they relate

- **Skills are instructions an agent reads; they are not live processes.** "Invoke a sub-skill" means "read and apply that skill's Markdown," which a single agent does inline. A skill never needs to be a separate running agent.
- **An agent reads skills and executes workflows.** One agent can read many skills and adopt many roles in sequence within a single run.
- **Roles are lenses, not agents.** A role is a responsibility or review perspective (a QA lens, a security lens, the founder's authority). The same agent can adopt multiple roles; a role requires no separate agent, process, or persona.
- **Agent instances are where execution happens, not where truth lives.** Conductor workspaces, sessions, and working trees are agent instances; their coordination notes are working-context (§8C) and never canonical.
- **Workflows sequence skills; policies constrain them.** §8E routes between stage skills; the §5, §8C, and §8D policies govern behavior at each step. **Policies govern skills and workflows; they do not replace artifacts or decisions.** Accepted knowledge still lives only in tracked Markdown artifacts (§8) and `decisions.md` (§8C) — a policy never becomes the system of record.

#### Single-agent baseline (normative)

One competent agent reading the tracked Markdown — the governing docs, this context package, the skills, and the project artifacts — must be able to execute **every** BuildSolid workflow end to end. No workflow, stage, skill, role, or policy may require multiple agents, a runtime, a service, a queue, a daemon, an MCP server, or any agent-as-process model to be usable (`framework/docs/constitution.md` §13, §15). Sub-skills are invoked **by stage/workflow need** (§8E), not because each skill must be a separate live agent.

#### Multi-agent and Conductor are optional

Running BuildSolid as multiple parallel agents — for example across Conductor workspaces — is an **execution convenience, never a requirement and never canonical state** (`framework/docs/constitution.md` §13). Multi-agent coordination lives in `.context/` and `.handoffs/` as working-context (§8C) and must never stand in for an accepted artifact. Anything multiple agents produce becomes canonical only by promotion into reviewed Markdown artifacts and decisions (§8C).

#### No persona-heavy design

BuildSolid must **not** depend on named character personas, fictional team members, or artificial "agent teams" to function. Role labels (for example "reviewer", "planner", "founder") are shorthand for responsibilities, review lenses, or handoff framing — they are not characters and not new canonical lifecycle units. A role label may frame a review or a handoff, but it does not add a stage, skill, artifact, mode, or authority that is not already accepted in the governing docs. Introducing a new canonical role, skill, stage, mode, or authority — or renaming, removing, merging, or reclassifying an existing one — remains founder-gated under `framework/docs/constitution.md` §16.

#### Scope boundary

§7A defines the execution vocabulary and model only. It does not rename or reclassify a skill, alter the §8E Existing Project Change, Stage 13, or Stage 9 procedures, or propagate a new rule into `templates/*.md`. The §7 skill set and the §8E stage-to-skill routing reference remain unchanged.

---

## 8. Project templates (artifacts)

Every BuildSolid project should be capable of producing these files. They are the durable memory of the project — what survives across sessions and across agents.

**Meta / agent-facing:**

- `AGENTS.md` — generic guidance for any AI coding agent operating on the repo.
- `CLAUDE.md` — Claude-Code-specific guidance and conventions.

**Product & intent:**

- `founder-intent.md` — why this exists, for whom, what success looks like.
- `discovery.md` — discovery notes, raw and structured.
- `product-thesis.md` — the compressed, one-paragraph thesis.
- `problem-statement.md` — the problem, its sufferers, current alternatives.
- `mvp-scope.md` — what's in for v1.
- `non-goals.md` — what's explicitly out (and why).
- `user-journeys.md` — the few flows that actually matter.

**Design & architecture:**

- `design.md` — UX direction, principles, references.
- `architecture.md` — system architecture and stack.
- `intelligence-layer.md` — AI capabilities, prompts, evals, fallbacks, costs.
- `decisions.md` — running log of decisions and their rationale.

**Build & ship:**

- `spec.md` — the spec the builder works against.
- `plan.md` — the implementation plan for the spec.
- `tasks.md` — concrete, verifiable tasks.
- `deployment.md` — how this ships and runs.
- `launch-checklist.md` — what must be true before launching.

**Living state:**

- `changelog.md` — what changed and when.
- `known-issues.md` — current bugs, gaps, and intentional debt.

Not every project needs every file on day one — but the system must know how to produce each when the relevant phase calls for it.

### 8A. Artifact requirements by profile

This matrix defines BuildSolid Development artifact requirements for the three project profiles in §5A. It retains the current artifact vocabulary above. It does **not** merge, remove, rename, or create any canonical artifact; authority and memory states are defined separately in §8C.

Requirement states are qualitative:

- **Required** — normally exists or is updated for the selected profile.
- **Optional** — useful when present, but not required for the profile or stage to proceed.
- **Profile-triggered** — required because the selected profile normally needs it.
- **Need-triggered** — required only when the project's facts make it applicable.
- **N/A - reason** — intentionally not applicable and durably explained when omission is material, using the compatibility token from §5B.

For **Existing Project Change**, "required" usually means "read the accepted artifact and update it only if the impact analysis shows it is affected." The run records affected surfaces, downstream gates, and material exclusions; it does not need one row for every unaffected upstream artifact.

| Artifact | Stage | New Product Build | Existing Project Change | Lightweight/Internal Build | Trigger conditions |
|---|---:|---|---|---|---|
| `AGENTS.md` | 0 | Need-triggered | Need-triggered | Need-triggered | Required when project agent rules are missing, stale, or changed. |
| `CLAUDE.md` | 0 | Need-triggered | Need-triggered | Optional | Required when Claude-Code-specific project guidance is used or changed. |
| `founder-intent.md` | 0-1 | Required | Required read; update if intent, audience, constraints, or a durable project profile/mode changed | Required at lightweight depth | Records durable project choices at initialization; transient session posture is not persisted. |
| `discovery.md` | 1 | Required | Conditional | Optional | Required when user/audience/problem evidence is being collected or materially revised. |
| `product-thesis.md` | 2 | Required | Conditional | Optional | Required when the product thesis is new or changed. |
| `problem-statement.md` | 2 | Required | Conditional | Optional | Required when the problem, sufferers, severity, or alternatives are new or changed. |
| `mvp-scope.md` | 3 | Required | Conditional | Required at lightweight depth | Required when scope, cuts, success, or failure criteria are new or changed. |
| `non-goals.md` | 3 | Required | Conditional | Required at lightweight depth | Required when explicit exclusions or deferred scope need to constrain work. |
| `user-journeys.md` | 4 | Required | Conditional | Optional | Required when user flows, journeys, or acceptance paths matter to the build. |
| `design.md` | 4 | Required | Conditional | Need-triggered | Required when UX direction, screen behavior, tone, or accessibility materially affect the work. |
| `architecture.md` | 6 | Required | Conditional | Need-triggered | Required when system shape, stack, data, dependencies, or technical boundaries are new or changed. |
| `intelligence-layer.md` | 5 | Need-triggered | Need-triggered | Need-triggered | Required when AI is load-bearing; do not create the file solely to record that AI is not load-bearing. |
| `decisions.md` | 0-13 | Required | Required | Required | Required for meaningful project decisions, overrides, deferrals, and rationale. |
| `spec.md` | 7 | Required | Required after impact analysis | Required | Required before implementation work can be planned or checked. |
| `plan.md` | 7 | Required | Required after impact analysis | Required | Required before task breakdown; records the applicable slice, downstream gates, and material exclusions when they matter. |
| `tasks.md` | 8 | Required | Required after impact analysis | Required | Required before Build Mode or implementation begins. |
| `deployment.md` | 11 | Required | Conditional | Need-triggered | Required when the work ships to an environment, changes operations, or affects rollout/recovery. |
| `launch-checklist.md` | 12 | Required | Conditional | Need-triggered | Required when the work has a user-facing launch, communication, metrics, or readiness event. |
| `changelog.md` | 13 | Need-triggered | Need-triggered | Optional | Required when the project uses a durable change log or a release/update is recorded. |
| `known-issues.md` | 10, 13 | Need-triggered | Need-triggered | Optional | Required when bugs, gaps, accepted limitations, or intentional debt must persist across sessions. |

For Stage 9 (Implementation), BuildSolid remains markdown-only. Implementation support follows the §8E procedure and lives in the accepted `spec.md`, `plan.md`, `tasks.md`, `decisions.md`, and any affected project artifacts; it does not require or authorize a new implementation-context artifact, scaffold, script, or project generator.

For substantive Stage 13 (Iteration), feedback re-enters the relevant earlier stage through the brownfield path in §5B, using the detailed procedure in §8E. Update existing artifacts in place: use `known-issues.md` for persistent issues, `decisions.md` for meaningful acceptance, rejection, or tradeoffs, and the affected stage artifact for changed accepted state. Ordinary correction uses normal task, review, or change provenance. No separate evidence or feedback artifact is created.

### 8B. Semantic readiness criteria

An artifact is semantically ready when a fresh competent agent can use it to continue the project without private chat context. Readiness is stronger than removing template residue. Every ready artifact must:

- keep the stable headings expected by an artifact that exists; explain a material intentional omission in the compact applicability record rather than creating an empty artifact;
- replace placeholders and blockquoted drafting guidance with project-specific content, except where a clearly marked draft section is still intentional;
- align with upstream artifacts and name any conflict rather than silently resolving it;
- record meaningful decisions in `decisions.md` when the artifact resolves scope, architecture, implementation, launch, or substantive iteration questions;
- name open questions, blockers, and material exclusions explicitly; existing or locally useful `N/A - reason` states remain valid;
- include enough acceptance, review, or validation detail for the artifact's lifecycle stage and selected profile.

Per-artifact readiness criteria:

| Artifact | Semantically ready when... |
|---|---|
| `AGENTS.md` | It gives agent-neutral read-first order, project rules, profile/mode expectations, decision-recording rules, and project-specific guardrails without embedding one-harness-only assumptions. |
| `CLAUDE.md` | It contains only Claude-Code-specific additions, links back to `AGENTS.md`, and documents agent-neutral fallbacks for any Claude affordance. |
| `founder-intent.md` | It states the founder, audience, reason for existence, success definition, constraints, and any durable project profile or mode choice clearly enough to anchor later artifacts. Transient session posture need not appear. |
| `discovery.md` | It distinguishes raw observations from structured findings, names current alternatives, and identifies hypotheses or open questions still needing evidence. |
| `product-thesis.md` | It gives a concise thesis, wedge, audience, and timing rationale that later scope and spec artifacts can quote or test. |
| `problem-statement.md` | It identifies who has the problem, what hurts, why it persists, current alternatives, and severity/frequency in concrete terms. |
| `mvp-scope.md` | It states the thesis to prove, must-haves, explicit cuts, success/failure criteria, and time/effort budget proportionate to the selected profile. |
| `non-goals.md` | It names excluded product, user, business, technical, AI, and process scope with enough rationale to prevent relitigation during implementation. |
| `user-journeys.md` | It describes the primary flows, actor intent, trigger, steps, success state, failure/edge cases, and cross-journey patterns needed by design, spec, and QA. |
| `design.md` | It defines UX principles, tone, key screens, cross-screen patterns, and out-of-scope design boundaries at the depth required by the selected profile. |
| `architecture.md` | It explains the system shape, components, data model, dependencies, decisions, constraints, and boundaries with the intelligence layer. |
| `intelligence-layer.md` | When AI is load-bearing, it defines AI role, capabilities, model/data flow, eval strategy, cost model, safety boundaries, and iteration loop. No file is required solely to record that AI is not load-bearing. |
| `decisions.md` | It preserves decisions in append-only form with context, decision, rationale, consequences, and references sufficient to reconstruct why the project changed. |
| `spec.md` | It states target users, problems, goals, non-goals, journeys, required capabilities, architecture/intelligence summaries, acceptance criteria, risks, and open questions. |
| `plan.md` | It identifies authoritative inputs, resolved planning decisions, structure, build phases, dependencies, sequencing, review checkpoints, validation, merge criteria, risks, and the applicable lifecycle slice, including material exclusions. |
| `tasks.md` | It decomposes the plan into small verifiable tasks with files, inputs, acceptance, status, dependencies, parallelization, and review gates, at the depth selected by the profile. |
| `deployment.md` | Where deployment applies, it covers environments, secrets, rollout, rollback, observability, incident response, recovery, cost/capacity, and compliance. No file is required solely to record inapplicability. |
| `launch-checklist.md` | Where launch applies, it states readiness for product, intelligence layer, infrastructure, security, privacy, communication, metrics, operations, and unresolved decisions. No file is required solely to record inapplicability. |
| `changelog.md` | It records released or unreleased changes in stable categories, preserves historical accuracy, and points to decisions or migration notes when changes matter. |
| `known-issues.md` | It records current bugs, gaps, intentional debt, status, impact, owner or next review point, and resolution history when persistent issues exist. |

The readiness and gating policy in §8D defines how a direct caller or orchestrator advances, defers, blocks, or routes based on these criteria. This section defines the artifact contract only.

### 8C. Authority and memory states

BuildSolid Development treats durable project memory as tracked, human-readable Markdown. Authority states describe how information should be interpreted when a fresh agent reconstructs project state from the repository.

Git plus human-readable Markdown are authoritative for **accepted** knowledge. Chat, `.context/`, `.handoffs/`, generated summaries, external memory, provider state, and derived views are not canonical unless their content is promoted through reviewed Markdown artifacts and decisions.

Authority-sensitive information uses these states:

- **Proposed** - A suggested change, interpretation, decision, issue, artifact edit, or plan that has not yet been accepted. Proposed knowledge may appear in draft sections, proposed decision entries, review notes, or working context, but it must be labeled clearly and cannot override accepted artifacts. Promotion requires human review when the change affects scope, architecture, lifecycle applicability, implementation direction, launch, iteration, authority, or governance.
- **Accepted** - Current canonical knowledge recorded in tracked human-readable Markdown after the required review. Accepted knowledge lives in the relevant artifact from §8 and, when consequential, in `decisions.md`. A decision with `Status: Accepted` is accepted only for the scope named in that entry; it does not silently approve deferred work.
- **Superseded** - Formerly accepted knowledge that has been replaced by a later accepted artifact update or decision. Superseded entries remain in place for history and rationale, but they do not control current work when they conflict with the later accepted source that superseded them.
- **Derived** - A summary, view, synthesis, checklist, model output, report, or memory projection created from other sources. Derived knowledge must point back to its inputs when used for review. It is useful for navigation and analysis, but it is non-canonical until promoted into accepted artifacts or decisions.
- **Ephemeral** - Temporary conversation, scratch notes, unstaged reasoning, local reminders, or transient coordination that is expected to expire. Ephemeral knowledge may guide the current exchange, but a future agent must not need it to reconstruct accepted state.
- **Evidence/event** - A dated observation, user report, validation result, review finding, production incident, research note, benchmark, or test outcome. Evidence/event knowledge records what happened or what was observed; it can support proposals and decisions, but it does not by itself change accepted project direction.
- **Working-context** - Coordination state for active work, including `.context/`, `.handoffs/`, branch handoffs, role notes, generated summaries, and workspace ownership notes. Working-context may help agents collaborate, but it is non-canonical and must yield to accepted tracked artifacts when conflicts appear.

Conflict precedence for BuildSolid Development:

1. `framework/docs/constitution.md` governs everything.
2. `framework/docs/brand/BUILD_SOLID_CANONICAL.md` governs naming and positioning within constitutional limits.
3. `framework/docs/context-package.md` governs the current workflow, modes, profiles, stages, artifact vocabulary, artifact requirements, readiness criteria, and this authority model within constitutional limits.
4. Accepted BuildSolid decision entries included in this exact tree govern consequential choices for their named scope within the documents above. A later accepted decision supersedes an earlier conflicting decision only when it says so or clearly covers the same question.
5. Accepted scoped specs, plans, and tasks included in this exact tree govern implementation within the higher sources and decisions. The narrowest accepted task boundary controls execution detail but never supersedes an accepted decision by implication.
6. Accepted skills and templates govern execution details for their own scope, subject to the documents above.
7. Examples, `.handoffs/`, `.context/`, chat, generated summaries, external memory, provider state, and other derived or working-context sources are useful inputs only when they do not conflict with the accepted sources above.

Unpublished decisions, specs, plans, tasks, or other contracts outside the exact tagged tree have no authority over a selected public release.

Inside a downstream BuildSolid project, the same pattern applies at project level: the project's `decisions.md` and accepted artifacts are the project authority, subject to BuildSolid's governing docs and templates. Project working-context and chat remain non-canonical unless promoted into reviewed project artifacts.

Human review promotes authority-sensitive changes by accepting a Markdown artifact edit, accepting a decision entry, or explicitly approving a proposed artifact state. Agents may draft proposals, collect evidence, and apply approved edits, but they must not silently promote contested, missing, high-impact, or governance-sensitive information into accepted state.

This section defines the authority and memory contract only. It does not implement validation runs or any new canonical artifact.

### 8D. Readiness and gating policy

This section defines how a direct skill caller or the BuildSolid orchestrator decides whether work may progress and where it goes next, using artifact requirements (§8A), semantic readiness criteria (§8B), authority and memory states (§8C), lifecycle contracts (§5B), and interaction modes (§5). It does **not** rename or reorder any stage, mode, profile, artifact, or skill; create a canonical artifact; or introduce numeric risk tiers or scores. Every judgment is qualitative.

A **gate** is an actual prerequisite, acceptance, routing, authority, security, deployment, launch, or consequential decision point. A direct caller or orchestrator uses exactly one of four outcomes when such a boundary is reached; no ceremonial gate is required at every stage transition.

#### The four gating outcomes

- **Advance** — move the run from the current stage to the next applicable stage.
- **Defer** — progress past a known, unready gap because a human has explicitly accepted the gap for now.
- **Block** — stop; do not progress until the gate is satisfied, deferred, or escalated.
- **Route** — hand control to a specific stage or sub-skill instead of progressing linearly.

Advance, defer, and block answer "may the run progress past this stage?" Route answers "where does work go next?" A single gate may combine block with route (block here; route to the upstream skill that can unblock).

#### When each outcome applies

**Advance** applies when, for the current stage and the selected profile:

- every artifact the stage is **required** to produce or update (§8A) exists, is **accepted** (§8C), and is **semantically ready** (§8B) at the depth the profile expects; and
- every applicable material dependency is satisfied and any material exclusion is explicit (§5B); and
- no unresolved conflict, stale input, or authority violation affects the stage; and
- any founder gate for the stage has been cleared.

**Defer** applies when a required artifact or stage is not yet ready but a human has explicitly chosen to accept the gap and continue. Only a human authorizes a deferral; an agent never defers on its own. The deferral is recorded in the applicable project's `decisions.md` (see "Human deferral" below) and the gap is carried forward so downstream skills see it.

**Block** applies when progression would cross an unsatisfied gate without an authorized deferral. Specifically:

- a genuine required input is missing, draft, or marked blocking, and no deferral applies;
- two accepted inputs conflict, or an artifact conflicts with an upstream artifact (§8B requires naming, not silently resolving, the conflict);
- a stale input no longer reflects an accepted upstream change;
- a proposed, derived, ephemeral, evidence/event, or working-context input would have to override an accepted artifact for the run to proceed (§8C);
- a founder gate is triggered (stage/mode/profile/artifact/skill rename, removal, merge, or addition; an authority change; a new canonical artifact; or any constitution-level stop condition); or
- a destructive or otherwise high-impact action is pending.

A block ends only by resolving the input, establishing a valid material exclusion, recording a human deferral, or escalating the founder gate.

**Route** applies when the next action is not "advance to stage N+1" but "go to a specific stage or skill":

- a missing dependency belongs to an earlier stage → route to the skill that owns it;
- a sub-skill returns a missing-dependency or wrong-phase handoff → route to the producing skill;
- Existing Project Change impact analysis directs entry at the stage matching the change's blast radius (§5B) → route there and carry its affected surfaces, downstream gates, and material exclusions;
- Stage 13 iteration re-entry sends accepted feedback back to the relevant earlier stage using the §8E iteration procedure (§5B) → route there and update artifacts in place.

Route never promotes non-canonical input to accepted; it only changes which stage or skill works next.

#### Applicability and `N/A - reason` as a satisfied state

A stage or artifact recorded with `N/A - reason: <reason>` (§5B) is treated by every gate as **satisfied**, not as missing work. A compact material exclusion is also satisfied when it is specific and reconstructable from tracked Markdown. No marker is required for an omission that is neither material nor surprising. When the token is used, two conditions apply:

- the reason must be specific and reconstructable from tracked Markdown (§5B); a bare `N/A` with no reason is treated as a draft/missing input and blocks; and
- the marker lives in the owning artifact or compact applicability record, and a `decisions.md` entry is added only when the exclusion is itself a meaningful accepted choice (§5B).

#### How input state affects gating

Gating reads the authority state of each input (§8C). Only **accepted** knowledge in tracked Markdown can satisfy a readiness gate. Therefore:

- **Missing / draft / blocking** genuine required input → block (or defer if a human accepts the gap; or establish a material exclusion if it does not apply).
- **Conflicting** inputs → block and route to the skill that owns the conflicting artifact; name the conflict (§8B), do not silently resolve it.
- **Stale** input (for example a `founder-intent.md` §6 durable profile or mode choice that has been superseded by an accepted project change) → not ready for the affected scope; block or route to refresh it before relying on it. A temporary session posture that differs from a durable project choice does not by itself make the artifact stale.
- **Proposed** input → cannot satisfy a gate; it must be promoted to accepted through human review (§8C) before it counts.
- **Superseded** input → does not satisfy the gate when it conflicts with the accepted source that superseded it.
- **Derived, ephemeral, evidence/event, working-context** inputs → non-canonical; they may inform a proposal or a route decision but can neither satisfy a readiness gate nor override an accepted artifact. Evidence/event can support a deferral or a proposal; it does not by itself advance a gate. `.context/` and `.handoffs/` working-context can never stand in for an accepted artifact.

This preserves the §8C rule that agents must not silently promote contested, missing, high-impact, or governance-sensitive information into accepted state.

#### How gating varies by profile

Profiles change *which artifacts gate a stage* and *the readiness depth expected*, never the four outcomes and never through numeric tiers (§5A, §5B):

- **New Product Build** — gates on the full required artifact set for each stage (§8A); conditional stages are decided when they matter, and material deviations are recorded.
- **Existing Project Change** — gates only on genuine prerequisites and artifacts the impact analysis shows are affected. Impact analysis is itself a gate before Stage 8 (§5B), so Task Breakdown blocks until the compact outcome is clear in accepted artifacts. The caller reads accepted artifacts first rather than rediscovering them.
- **Lightweight/Internal Build** — gates on the smaller applicable set with proportionately lighter readiness depth. A proportionate review, including security where relevant, is still expected when the work creates that risk; no empty N/A-only artifact is required.

All three use qualitative applicability only.

#### How gating respects mode behavior

Gating logic is identical in every mode. The four interaction modes (§5) change only *how* the direct caller or orchestrator handles a gate — question density, explanation depth, and stop/escalation posture — not what counts as ready, satisfied, or blocking. No mode name or meaning changes here.

- **Guided Mode** — explains the gate and the gap in plain language; asks before deferring; surfaces what a block needs.
- **Founder Mode** — pressure-tests whether a gap actually matters before allowing a deferral; escalates product-direction gaps to `decisions.md`.
- **Expert Mode** — states the gate decision concisely; defers only material gaps; does not re-ask questions already answered on disk.
- **Build Mode** — advances against accepted `spec.md` / `plan.md` / `tasks.md`; blocks only when required build inputs are missing or conflicting or when work would drift from accepted artifacts; asks only when blocked.

No mode may lower a gate so that proposed or non-canonical input silently becomes accepted, and no mode may skip a founder gate or a destructive-action confirmation (§5, §8C).

#### Human deferral

A deferral is the only way to progress past a genuinely required but unready artifact. An inapplicable item is instead a material exclusion under §5B. Deferral is a human decision, not an agent one, and is recorded in the applicable project's `decisions.md` with:

- the deferred artifact or stage;
- the reason for deferring;
- the stage the run is advancing into; and
- the scope of the deferral (it is accepted only for that scope and does not silently approve other deferred work, per §8C).

The direct caller or orchestrator carries the deferred-gap note forward so downstream skills see it when reconstructing state.

#### Policy boundary

§8D defines readiness and gating only. The routing workflow that consumes its four outcomes, the Existing Project Change impact procedure, substantive Stage 13 iteration, and Stage 9 implementation support are in §8E. Neither section renames, adds, removes, merges, or moves a skill, stage, profile, mode, or artifact.

### 8E. Routing workflow

This section defines the **routing workflow** for BuildSolid Development: the ordered procedure that takes a run from intake to a delegated sub-skill, using only the contracts already in place — the lifecycle stages (§6), the project profiles and their lifecycle contracts (§5A, §5B), the interaction modes (§5), the artifact requirements (§8A), the semantic readiness criteria (§8B), the authority and memory states (§8C), and the readiness/gating policy and its four outcomes (§8D). It does **not** change any of those contracts; it does not rename, merge, remove, reorder, or add any stage, mode, profile, artifact, or skill; it introduces **no numeric risk tiers or scores**; and it implies **no runtime orchestration, service, queue, daemon, MCP server, or agent-as-process**. The workflow is a Markdown decision procedure that one agent reading tracked Markdown can execute end to end. Multi-agent and Conductor patterns remain an optional convenience layered on the same procedure (§3; `framework/docs/constitution.md` §13).

This is the canonical routing workflow. `project-system/skills/buildsolid-orchestrator/SKILL.md` **consumes** this section rather than restating it; the orchestrator owns only coordination, routing, continuity, and escalation. A focused skill may be invoked directly under §5B when its purpose and genuine prerequisites are clear.

#### The routing loop

Run this ordered loop when the human requests routing or status, entry is ambiguous, work crosses stages, cross-stage dependencies are missing, the profile may materially change, continuity must be reconstructed, or substantive Stage 13 diagnosis is needed. It is not a mandatory session preamble or stage-boundary ceremony. A compact loop — not a stage×profile×mode matrix — gives every combination a clear path when routing is needed.

1. **Intake.** Capture the user's stated intent and session context (Stage 0). One sentence is enough to start.
2. **Resolve mode and profile.** Apply the order in §5 and §5A: explicit current instruction, accepted durable project choice, unambiguous context, then a focused question only for material ambiguity. State an inference and persist only a durable change. Modes and profiles are orthogonal: profile selects workflow depth (§5B); mode selects human interaction (§5).
3. **Read canonical state.** List the artifacts on disk and read the **accepted** ones (§8C). For each artifact a stage is required to produce, determine its authority state (§8C) and whether it is semantically ready at the profile's expected depth (§8A, §8B). Non-canonical inputs — `.context/`, `.handoffs/`, chat, generated summaries, derived views — may inform routing but can never satisfy a gate or stand in for an accepted artifact (§8C, §8D).
4. **Identify the current stage.** For New Product Build, the current stage is the first applicable §6 stage whose required artifact is missing, draft, or not semantically ready, unless the human states otherwise. Lightweight/Internal uses the smallest applicable slice. Existing Project Change takes its entry stage from impact analysis, not a fresh Stage 0 walk. A recorded N/A or material exclusion is satisfied and skipped.
5. **Apply an actual gate.** At a genuine prerequisite, acceptance, routing, authority, security, deployment, launch, or consequential boundary, evaluate the four §8D outcomes against required inputs, authority states, and any founder gate.
6. **Choose the path** (exactly one §8D outcome):
   - **Advance** → proceed to the next applicable stage and its primary skill (routing reference below).
   - **Defer** → only on explicit human acceptance; record the deferral in `decisions.md` (deferred item, reason, destination stage, scope), carry the gap forward, and proceed.
   - **Block** → stop; state what the gate needs (resolve the input, establish a material exclusion, record a human deferral, or escalate a founder gate). Do not advance.
   - **Route** → hand control to the specific stage or sub-skill that owns the dependency (an upstream producer, a sub-skill's missing-dependency handoff, the Existing Project Change impact-analysis entry point, or the Stage 13 iteration re-entry target) instead of advancing linearly. Route never promotes non-canonical input to accepted.
7. **Delegate.** Invoke the chosen stage's primary sub-skill with the resolved profile, stated mode, stage context, and any carried-forward deferred gaps. The sub-skill's own §5 delta applies inside the central mode policy (§5).
8. **Preserve material continuity.** Record only what a fresh agent needs: an owning-artifact note for affected state, a `decisions.md` entry for consequential judgment such as a durable profile/mode change, material deferral, or conflict resolution, and a `founder-intent.md` §6 update only for a durable project choice. `.context/`/`.handoffs/` notes remain working-context scratch (§8C).
9. **Escalate founder gates.** When a gate would require a stage/mode/profile/artifact/skill rename, removal, merge, or addition; an authority change; a new canonical artifact; another `framework/docs/constitution.md` §16 stop condition; or a destructive/high-impact action — stop and escalate to the human, and record the escalation in `decisions.md`. The orchestrator never clears a founder gate on its own (§8C, §8D).

#### Entry points by profile

The loop is the same for all three profiles; only the **entry point** and the **gating depth** differ (§5B, §8D). This is the compact decision workflow that gives every stage/profile combination a clear starting path:

- **New Product Build** — enter at Stage 0 (Intake) and walk the full lifecycle in order by default. Each required stage gates on its full §8A artifact set; decide Conditional stages when they matter and record material deviations.
- **Existing Project Change** — do not restart at fresh discovery. Enter through the brownfield path (§5B), run the compact impact analysis below, and route to the earliest affected stage. Full rediscovery applies only when intent, audience, or product direction changes.
- **Lightweight/Internal Build** — enter with the smallest applicable slice and lighter readiness depth (§5B, §8D). Proportionate review, including security where relevant, still applies when the work creates that risk; no empty N/A-only record is needed.

Stage 13 (Iteration) re-entry uses the same Existing Project Change brownfield path: accepted feedback routes back to the relevant earlier stage and artifacts are updated in place (§5B).

#### Impact analysis procedure (Existing Project Change)

Impact analysis is a Markdown-only routing procedure for Existing Project Change work. It creates no new artifact, stage, skill, score, runtime, or automation. It records the change's effect in existing accepted artifacts so later skills can continue from the right lifecycle point without rediscovering the whole project.

Run this procedure before identifying the current stage for an Existing Project Change:

1. **Read existing state.** Read accepted project artifacts (§8) and the relevant code or implementation surface. Use non-canonical context such as chat, `.context/`, `.handoffs/`, or generated summaries only as clues; they cannot satisfy the gate or override accepted artifacts (§8C).
2. **Frame the change in plain language.** State what is changing, why now, which user/workflow/system surface it affects, and which accepted artifacts or code areas appear touched.
3. **Run the direction test.** Determine from accepted state and current instruction whether the change alters product intent, target audience, or product direction; ask only if that answer is materially ambiguous. If **yes**, route to full rediscovery at Stage 1 (Founder Discovery) and update accepted artifacts in place from there. If **no**, continue the Existing Project Change path.
4. **Classify blast radius by earliest affected stage.** Identify the earliest §6 lifecycle stage whose accepted artifact, decision, or code contract must change. That earliest affected stage is the entry stage. Examples: a UX-only change enters at Stage 4; an architecture decision enters at Stage 6; a spec-only correction enters at Stage 7.
5. **Record the compact outcome in existing artifacts.** Ensure current accepted `spec.md`, `plan.md`, `tasks.md`, or another owning artifact makes the direction-test answer, entry stage, affected artifacts or stages, required downstream gates, and material exclusions clear. Add a separate compact note only when those artifacts do not make the impact reconstructable. Add a `decisions.md` entry only for a meaningful accepted choice or tradeoff; do not create a full upstream N/A ledger.
6. **Gate Stage 8.** Stage 8 (Task Breakdown) remains blocked until the compact impact outcome is clear in accepted artifacts. `task-breakdown` may not draft or update `tasks.md` from an unresolved impact analysis.
7. **Route to the entry stage.** Use the existing stage-to-skill routing reference below to invoke the entry stage's primary sub-skill with the impact-analysis outcome carried forward.
8. **Resume ordinary progression.** From the entry stage forward, use the normal §8D advance / defer / block / route logic. Update affected accepted artifacts in place; do not create parallel versions.

#### Iteration procedure (Stage 13)

Iteration is a Markdown-only feedback and re-entry procedure for Stage 13. It creates no new artifact, stage, skill, authority state, score, runtime, or automation. It turns feedback about already accepted project state into an accepted or rejected change path that a fresh agent can reconstruct from tracked Markdown.

Run this procedure only when feedback, review, validation, production use, or user observation arrives after **Accepted** state and would materially change intent, scope, architecture, acceptance, launch treatment, or cross-stage direction:

1. **Observe the feedback.** Capture the source, affected accepted state, impact, and current status in the affected artifact or `known-issues.md` when the issue must persist across sessions. Non-canonical inputs may identify feedback but do not override accepted state (§8C).
2. **Run the material-change test.** Stage 13 applies only when accepted state exists and the feedback would change intent, scope, architecture, acceptance, launch treatment, or cross-stage direction. Same-scope bugs, review remediation, maintenance, routine retry, and in-progress or pre-sign-off work remain ordinary Existing Project Change.
3. **Diagnose the route.** Reuse the impact-analysis procedure above, including its direction test and blast-radius classification by earliest affected §6 stage, rather than restating a separate diagnostic model.
4. **Propose and test the change.** Draft the smallest proposed artifact updates that address the evidence, then test the proposal against the affected artifacts' §8B semantic readiness criteria before asking for acceptance.
5. **Human review.** Present the evidence, diagnosis, proposed updates, readiness check, and recommended re-entry stage for human review. Proposed knowledge remains non-canonical until accepted under §8C.
6. **Accept or reject.**
   - **Accepted change** → record a `decisions.md` entry when acceptance resolves a meaningful judgment or tradeoff, then route from the accepted compact impact outcome.
   - **Rejected proposal** → preserve a persistent `known-issues.md` entry only when the issue remains relevant, and record the rejecting decision when it carries lasting rationale.
7. **Update artifacts and route.** For an accepted change, update affected accepted artifacts in place and route to the relevant earlier stage. Do not create unaffected-stage rows solely to show omission.
8. **Validate proportionately.** Validate the updated artifact set at the depth required by the profile and affected stage. Record the result where it has durable value; ordinary task, review, or pull-request provenance is sufficient for same-scope correction.

#### Implementation-support procedure (Stage 9)

Stage 9 is Markdown-only support for project-side implementation. It creates no new artifact, stage, skill, authority state, score, runtime, scaffold, script, CLI, MCP server, automation, telemetry, integration, or product infrastructure. Builders execute the project work outside BuildSolid's artifact system; BuildSolid keeps the accepted implementation context reconstructable from tracked Markdown.

Run this procedure when Stage 8 has produced an accepted `tasks.md` and the run enters Stage 9:

1. **Confirm entry inputs.** Enter Stage 9 only when `spec.md`, `plan.md`, and `tasks.md` are accepted (§8C), semantically ready (§8B), and current for the selected profile. If any required input is missing, draft, stale, or conflicting, use the §8D block/route behavior before implementation begins.
2. **Track task context in `tasks.md`.** Each implementation task preserves its working context in the existing task fields: `Files`, `Inputs`, `Acceptance`, `Parallelizable`, `Review`, `Dependencies`, plus `Status`. The only valid `Status` values are `Not started`, `In progress`, `Blocked`, and `Done`. Non-canonical notes in chat, `.context/`, `.handoffs/`, or generated summaries may help the current builder, but a fresh agent must be able to reconstruct task state from tracked Markdown.
3. **Advance task status deliberately.** Mark a task `In progress` when project-side implementation begins, `Blocked` when the task cannot continue without resolving a documented blocker, and `Done` only when the task's own acceptance criterion has been satisfied. A dependency is available to downstream tasks only when it is accepted or its task status and review gate make the dependency state explicit.
4. **Detect drift continuously.** During implementation, compare the project-side work against the accepted `spec.md`, `plan.md`, and each task's `Acceptance`, `Files`, `Inputs`, `Review`, and `Dependencies`. Drift includes implementation that exceeds non-goals, changes planned sequencing or architecture, touches files outside the task contract, weakens acceptance criteria, or discovers that the task no longer matches the accepted spec/plan.
5. **Recover from divergence before continuing.** If implementation diverges from `spec.md`, `plan.md`, or `tasks.md`, update the accepted artifact first per `framework/docs/constitution.md` §6, with rationale recorded in `decisions.md`, then resume Stage 9 from the updated task context. Do not accept implementation merely because it was easier than the spec.
6. **Recover from stalls through existing gates.** If a task stalls, record blocker evidence in `known-issues.md` when the blocker must persist across sessions, set the task `Status` to `Blocked`, and then use the existing §8D **Block** outcome or explicit human **Defer** behavior. A blocked task is not complete just because implementation stopped.
7. **Recover from missing requirements by routing.** If implementation reveals a missing requirement, reuse the §8E impact-analysis direction test. Small in-scope gaps that do not change product intent, target audience, or product direction route to `task-breakdown` for task adjustment after any needed spec/plan update. Direction-changing gaps leave Stage 9 and route outside implementation through the relevant earlier stage.
8. **Prepare the Stage 10 handoff.** Before handing off to Stage 10, every in-scope task has `Status: Done` or an explicit `Status: Blocked` with blocker evidence and a recorded human deferral/decision; any accepted divergence has already updated `spec.md`, `plan.md`, and/or `tasks.md`; open issues are in `known-issues.md`; and the implementation is ready for `qa-reviewer` to compare against the accepted task acceptance criteria.

#### How modes shape routing

The lifecycle order is **identical in every mode**. The mode (§5) changes only the question density, explanation depth, and stop/escalation posture a direct caller or orchestrator uses — never stage order or skill ownership (§8D). At each actual gate:

- **Guided Mode** — explain the gate and the gap in plain language; ask before deferring; surface what a block needs.
- **Founder Mode** — pressure-test whether a gap actually matters before allowing a deferral; escalate product-direction gaps to `decisions.md`.
- **Expert Mode** — state the gate decision concisely; defer only material gaps; do not re-ask questions already answered on disk.
- **Build Mode** — advance against accepted `spec.md` / `plan.md` / `tasks.md`; block only when required build inputs are missing or conflicting or when work would drift from accepted artifacts; ask only when blocked.

No mode may lower a gate so that proposed or non-canonical input silently becomes accepted, and no mode may skip a founder gate or a destructive-action confirmation (§5, §8C, §8D).

#### Stage-to-skill routing reference

This table is the canonical mapping from each §6 stage to the sub-skill that owns it. Which stages actually run follows the applicable lifecycle slice (§5B); a recorded N/A or material exclusion is satisfied and does not block routing. The stage list, order, and names are unchanged from §6.

| Stage | Stage name | Primary sub-skill | Optional helper(s) |
|---|---|---|---|
| 0 | Intake | orchestrator itself (resolve profile + mode; capture the raw idea) | — |
| 1 | Founder Discovery | `founder-discovery` | — |
| 2 | Idea Compression | `idea-compressor` | — |
| 3 | MVP Scope | `mvp-scope` | — |
| 4 | UX Direction | `ux-minimalist` | — |
| 5 | Intelligence Layer | `intelligence-layer-architect` | — |
| 6 | Technical Architecture | `technical-planner` | `starter-stack-advisor` (helper) |
| 7 | Spec Creation | `spec-planner` | — |
| 8 | Task Breakdown | `task-breakdown` | — |
| 9 | Implementation | project-side build against `tasks.md`; no BuildSolid skill (markdown-only support, §5B and §8E implementation-support procedure) | — |
| 10 | QA and Review | `qa-reviewer` then `security-reviewer` | — |
| 11 | Deployment | `deployment-manager` | — |
| 12 | Launch Prep | `launch-prep` | — |
| 13 | Iteration | back to the relevant earlier stage's primary skill, updating artifacts in place (§5B iteration loop, §8E iteration procedure, and brownfield re-entry) | — |

Stage 9 (Implementation) is intentionally skill-less: the project's own builders execute `tasks.md` using the implementation-support procedure above. A direct caller or the orchestrator hands control to **Build Mode** for the build; routing re-engages at **Stage 10 (QA and Review)** only when needed (§5B Stage 9 support; `framework/docs/constitution.md` §15 — no project-generation logic). `starter-stack-advisor` remains a standalone optional helper. Any future proposal to merge or remove it still requires new validation evidence and a separate founder decision.

#### Routing scope boundary

§8E defines routing, compact Existing Project Change impact analysis, substantive Stage 13 iteration, Stage 9 implementation support, and the canonical stage-to-skill reference. It changes no inventory, skill identity, standalone-helper decision, runtime, or authority boundary.

---

## 9. First example project

The first concrete project BuildSolid should be able to walk a user through end-to-end:

> **A minimalist SaaS for freelance photographers** that helps them:
> 1. Create client galleries.
> 2. Send delivery links to clients.
> 3. Collect client selections (favorites / final picks).
> 4. Use AI to suggest the best images for delivery (e.g., sharpness, expression, composition, duplicate culling).

The scenario, founder persona, complete research corpus, participants, quotations, observations, measurements, dates, permissions, and galleries are synthetic rather than conducted research or real-world evidence. Its product, implementation, evaluation, security, deployment, legal-review, and launch material illustrates artifact relationships; it does not claim completed activity. Use it as a compatibility fixture for skills and templates; Framework remains the governing authority.

---

## 10. Working agreements for agents

When you (an AI coding agent) operate on this repo:

1. **Read the relevant parts of this file first.** Then read the applicable artifacts in §8 that already exist before proposing changes.
2. **Resolve and state profile/mode** (§5, §5A). Infer safely from current instruction or accepted state; ask only when ambiguity materially changes the work; persist only durable project choices.
3. **Respect the phase order and applicable slice** (§5B, §6). For an Existing Change or Lightweight/Internal run, state the entry stage, affected surfaces, downstream gates, and material exclusions when they matter.
4. **Do not introduce tooling that BuildSolid disallows.** No CLI, web app, package, or automation layer. If you feel you need one, record it as a proposal in the applicable project's `decisions.md` instead.
5. **Prefer editing existing artifacts** over creating new ones. The artifact list in §8 is the canonical surface area.
6. **Stay portable in artifact contents.** Skill internals can lean on Claude Code; the markdown artifacts should make sense to any competent agent.
7. **Treat the photographer SaaS** (§9) as a synthetic compatibility fixture when designing or testing skills and templates. It demonstrates Framework; it does not redefine it.
