# BuildSolid — Constitution

> The non-negotiable rules that govern every BuildSolid spec, plan, skill, template, example, and future implementation. If a proposal conflicts with this document, the proposal loses. Amend the constitution explicitly — do not work around it.

This constitution sits alongside `framework/docs/context-package.md`. The context package describes *what BuildSolid is*; this constitution defines *what BuildSolid must and must not do*.

---

## 1. Product Identity

BuildSolid is a **free, open-source Markdown framework for spec-driven software development with AI**. It is not a prompt pack, a chatbot, a template repository, a SaaS product, or a replacement for an AI coding environment.

BuildSolid serves solo founders, designers, engineers, curious builders, and AI coding agents through a single shared workflow expressed as **markdown artifacts** and **agent skills**. The distributed framework consists of the workflow, Markdown artifacts, and agent guidance.

Canonical naming and positioning are defined in [`framework/docs/brand/BUILD_SOLID_CANONICAL.md`](brand/BUILD_SOLID_CANONICAL.md). If another document needs a short description, use: "BuildSolid is a free, open-source Markdown framework for spec-driven software development with AI."

Anything labeled "BuildSolid" must:

- Fit inside the phases defined in `framework/docs/context-package.md` §6.
- Produce or update one of the canonical artifacts (`framework/docs/context-package.md` §8).
- Be invocable or readable by an AI coding agent without requiring custom runtime infrastructure.

BuildSolid is a personal learning project shared freely for others to use and adapt. The creator intends to keep it free and open source, with no paid offerings or current plans to commercialize it. The creator intends to make occasional documentation and security corrections, with no planned feature development. Hypothetical future permissions elsewhere in this constitution are safeguards for evaluating a separately proposed change, not an active roadmap or a commitment to further development.

### Framework identity and Project System packaging

Venture stewards product strategy and proposals concerning BuildSolid identity and positioning. Framework governs the normative BuildSolid identity and positioning exposed by an accepted release, within the permanent constitutional principles and the canonical brand constraints. Venture may propose a Framework identity or positioning change, but no Venture decision changes a released Framework contract by implication. Project System depends on that Framework identity and may explain or demonstrate it without redefining it.

---

## 2. Constitutional Layers and Current Governing Scope

This constitution has five layers:

1. **Permanent principles.** The identity, authority, portability, human-control, minimalism, markdown-first, skill-first, artifact-driven, and decision-recording rules that govern every BuildSolid version unless explicitly amended.
2. **Current-version constraints.** The currently governing boundary for the latest finalized implementation scope and any maintenance before a successor scope is accepted. BuildSolid remains manual, Markdown-first, skill-first, Git/Markdown-authoritative, human-reviewed, agent-neutral, portable, and free of required runtime tooling or product infrastructure. BuildSolid's development repository may use optional development-only validators and CI that check—but never define or generate—the accepted Markdown contract. Separately gated repository, licensing, publication, and release actions receive only the authority granted by their exact accepted founder decision.
3. **BuildSolid Development contracts.** The current software-building application of BuildSolid: lifecycle stages, artifacts, skills, profiles, readiness gates, routing workflows, implementation guidance, and validation expectations. Development contracts may evolve through specs, plans, tasks, and decisions, but they do not automatically become universal BuildSolid Core primitives.
4. **Host and provider conventions.** Optional ergonomics for Claude Code, Codex, Conductor, MCP-capable environments, external memory systems, or future harnesses. These conventions must never become the only way to use BuildSolid.
5. **Future architectural permissions.** Safeguards for evaluating a hypothetical change involving coded systems, provider integrations, memory infrastructure, platform capabilities, or domain expansion. These permissions are neither an active roadmap nor current authorization.

This tree represents an exact Framework state. An untagged commit is a candidate only; released authority belongs only to the exact commit selected by the matching annotated version tag. Historical records may explain earlier states, but they do not override that selected release.

The five constitutional layers above remain the constitutional organization of BuildSolid. Venture, Framework, and Project System are architecture domains. Internal Development and Publication are operational zones. Domains and zones are not constitutional layers and do not rename, replace, merge, reorder, or add a layer.

Framework owns the normative BuildSolid contracts within the permanent principles and current-version constraints. Project System packages, instantiates, and demonstrates compatible Framework contracts without redefining them. Venture stewards strategy and proposals; Internal Development and Publication describe bounded operational work and receive no normative authority merely by being named.

The constitution and BuildSolid Development contracts in this tree state the contract for this exact tree. Their presence does not grant repository, licensing, publication, release, platform, product automation, implementation, or Build Mode authority by implication.

---

## 3. Core Principles

These principles are binding. They override convenience, novelty, and personal taste.

1. **Founder intent before code.** No skill, template, or example may begin with implementation details before intent is captured.
2. **Specs before implementation.** No code without a spec. No spec without scoped intent.
3. **Minimalism by default.** When two options work, the smaller one wins.
4. **AI is an intelligence layer.** Treat AI capabilities as a designed layer with prompts, evals, fallbacks, costs, and safety — not as decoration.
5. **One workflow, multiple modes.** Phases never change. Behavior changes by mode (Guided, Founder, Expert, Build).
6. **Inclusive by design.** Every phase must be usable by a beginner, a designer, an engineer, and a solo founder.
7. **Ask when needed; assume when safe.** Do not waste expert time, and do not invent intent.
8. **Prove manually before tooling.** BuildSolid capabilities must work as readable Markdown artifacts and skills. Any separately proposed automation, packaging, integration, or runtime tooling would first require evidence that the manual workflow works; this principle neither claims that such evidence already exists nor commits the project to future tooling. Development-only maintenance checks may automate verification of an already-readable contract; they do not become BuildSolid capabilities or replace the manual path.
9. **Iteration is a phase.** Revisiting earlier phases (per `framework/docs/context-package.md` §6, Phase 13) is legal and expected. When a phase is revisited, the corresponding existing artifact is **updated in place** — do not create parallel or versioned copies.

---

## 4. Markdown-First Rule

All durable BuildSolid outputs are markdown files.

- Specs, plans, tasks, decisions, design notes, architecture, intelligence-layer designs, deployment notes, and launch checklists are markdown.
- Skills are defined in markdown.
- Templates are markdown.
- Diagrams are embedded as text (e.g., Mermaid) inside markdown when possible.

Git plus human-readable Markdown are the authority for accepted BuildSolid knowledge. Conversations, `.context/`, `.handoffs/`, generated summaries, external memory, derived views, and provider state are not accepted canonical truth unless promoted through reviewed Markdown artifacts and decisions. The operational Development authority states and conflict-precedence chain are defined in `framework/docs/context-package.md` §8C.

Non-Markdown formats may be referenced from Markdown but must not be the primary carrier of a BuildSolid Framework or Project System artifact. Exact non-Markdown license or legal text separately accepted for an exact publication is a legal distribution file, not a replacement source of truth for BuildSolid contracts. No JSON-as-source-of-truth, YAML config schema, proprietary artifact format, or external system may replace accepted Git-tracked human-readable Markdown.

Private repository-maintenance scripts, tests, and workflow configuration are implementation details, not canonical Framework or Project System artifacts. They may validate accepted Markdown and Git invariants but may not generate, promote, or silently redefine accepted meaning.

### Authority precedence across contexts

Git plus human-readable Markdown remain authoritative for accepted BuildSolid knowledge. Human review remains required to promote authority-sensitive Proposed knowledge. Private unreleased work, public proposals, chat, `.context/`, `.handoffs/`, generated summaries, external memory, provider state, and derived views cannot override the accepted source for their context.

| Context | Exact proposed precedence |
|---|---|
| Private unreleased development | Applicable repository-wide governance and accepted private decisions control repository operations, confidentiality, and release preparation. The accepted Framework constitution controls normative Framework meaning. Accepted version-scoped plans and Project System source operate within both and cannot override either. |
| Released public BuildSolid use | The selected public release commit and tag, containing the accepted Framework contract and its compatible Project System package, govern that released version. Private unreleased changes have no public authority. |
| Downstream project work | The selected public release's Framework contract governs normative BuildSolid meaning; its compatible Project System package supplies conforming procedures and artifacts; then the downstream project's accepted decisions and artifacts govern project-specific facts. |
| Public contribution proposal | The currently selected released public contract remains controlling until private acceptance, reconciliation, validation, and a later accepted public release include the proposal. |

---

## 5. Skill-First Rule

All BuildSolid capabilities are exposed as **skills** before they are exposed as anything else.

- Every workflow capability listed in `framework/docs/context-package.md` §7 must exist as a markdown skill before any non-markdown form (script, package, service, etc.) is considered in any future version.
- Skills must be self-contained: a competent agent should be able to execute the skill given only the skill file and the project's existing artifacts.
- Skills must compose. Focused skills may be invoked directly when their purpose matches, genuine accepted prerequisites are current, profile and mode are safely resolved and stated, and no cross-stage ambiguity or founder gate exists. The orchestrator routes on demand for ambiguous intake, cross-stage coordination, missing cross-stage dependencies, continuity, or substantive iteration diagnosis. A skill that tries to do everything is wrong.
- New capability ideas enter the system as skill drafts, not as scripts, services, or packages.
- Any future non-markdown exposure of a BuildSolid capability requires a later accepted decision and, where this constitution requires it, a constitutional amendment. Skill-first is not bypassed by calling a future tool "experimental."
- A private repository-maintenance validator is not a BuildSolid capability merely because it checks BuildSolid source. It remains development infrastructure and must not become required for downstream use.

When building BuildSolid skills, **prefer using Claude's `skill-creator` skill** if available. If `skill-creator` is unavailable in the current harness, follow its conventions by hand. Either way, the resulting skill file must remain plain markdown that conforms to the Skill Quality Standard (§11) and is usable on agents that do not have `skill-creator`.

---

## 6. Spec-Before-Implementation Rule

No implementation work happens without a spec the implementation can be checked against.

- `spec.md` and `plan.md` must exist (and be current) before Phase 9 (Implementation) begins.
- `tasks.md` must exist before any agent claims to be in Build Mode.
- An implementation that drifts from the spec must update the spec **first**, with rationale logged in `decisions.md`, before continuing.
- "It was easier to just code it" is not a valid reason to skip a spec.

This rule applies to BuildSolid itself: new skills and templates require a short spec section (purpose, inputs, outputs, success criteria) before their content is fleshed out. For a skill, that spec section **is** the skill file's own header per the Skill Quality Standard (§11) — no separate `spec.md` is required to author a skill.

An exact accepted repository task contract or founder decision may supply the requirements, scope, validation, and stop conditions for routine maintenance and development-only validation. Such maintenance does not require a separate `spec.md` / `plan.md` / `tasks.md` stack solely because it uses code to verify the repository. Product capabilities, released behavior, and Build Mode implementation remain subject to the full rule above.

### Non-executable planning and independent execution gates

A Proposed spec, plan, task, contract, constitutional amendment, decision treatment, migration row, review result, or completed preparation task grants no implementation, Build Mode, activation, external-operation, licensing, publication, release, platform, automation, or merge authority.

A separately accepted repository-scoped founder decision may authorize one bounded envelope for reversible, non-canonical internal preparation or implementation when it names the exact eligible activities, accepted inputs, baseline requirement, integration ownership, exclusions, expiration, validation, and withdrawal rules. That envelope does not activate target authority, select or execute a founder-reserved external action, accept a license, publish, accept a release, or authorize merge. Build Mode applies only when the exact grant names it and only within that envelope. Every action beyond the envelope may begin only when its exact accepted inputs exist and the founder decision and confirmation required by its gate separately authorize that exact scope.

Dependencies establish order, not authority. No dependency satisfaction, recommendation, review result, commit, PR, merge, synchronization event, completed earlier task, or evidence row opens a later task, gate, or action automatically.

A no-agent-merge rule may be imposed by separately accepted repository-wide governance for a named private migration. It is not a permanent Framework principle, not a rule for downstream projects, and not authority to begin or merge a migration.

---

## 7. Minimalism Rule

When in doubt, cut.

- MVPs proposed by BuildSolid must be the smallest thing that proves the product thesis. Cut, then cut again.
- Skills must do one job well. Split before bloating.
- Templates must include only fields that are useful in the majority of projects. Optional fields belong in examples, not in the template itself.
- Decisions that add scope must be logged in `decisions.md` with explicit justification.

A "nice to have" is a non-goal until proven otherwise.

---

## 8. Agent-Agnostic Rule

BuildSolid may be used in Claude Code, Codex, Conductor, MCP-capable environments, external-memory-capable environments, GitHub Copilot, Spec Kit-shaped workflows, and future harnesses, but it must remain **portable** to a competent agent working from a normal Git checkout and human-readable Markdown. This describes host compatibility only; it does not authorize an MCP server, external integration, or external memory infrastructure for BuildSolid.

- Markdown artifacts (§8 of the context package) must be readable and actionable by any competent coding agent. No host-only or provider-only assumptions in artifact *contents*.
- Skill *contents* should describe behavior in agent-neutral language. Host wiring may be provider-specific, but the skill must still be usable by reading the `SKILL.md` file.
- When a host-specific feature is used (subagents, slash commands, hooks, browser state, temporary provider context, Conductor workspaces, or provider-native skills), it must be additive: the artifact or skill must still be usable on a different agent, possibly with reduced ergonomics.
- Claude-Code-only conventions live in `CLAUDE.md`. Generic conventions live in `AGENTS.md`. Equivalent host-specific conventions for other tools must stay in host-specific guidance, not in agent-neutral artifacts.

Portability is a requirement, not an aspiration.

### Public self-sufficiency

Every accepted public release must be understandable, usable, and reviewable from its public Git tree alone by a competent agent using a normal checkout and human-readable Markdown. A public user must not need the private upstream, private decisions or planning, private chat, hidden memory, provider state, unpublished source, or a particular host to understand the released Framework contract or apply its compatible Project System package.

Conductor, Claude Code, Codex, MCP-capable environments, external-memory systems, multi-agent execution, and other host capabilities remain optional ergonomics. Every released capability retains a single-agent path and an agent-neutral fallback. Public completeness cannot be satisfied by a private or host-only dependency.

Private CI and repository-maintenance validators are also optional ergonomics. A competent agent using a normal checkout must retain documented native or manual checks for the material invariant; absence of the private workflow must not make a released BuildSolid capability unusable or unintelligible.

---

## 9. Human-in-the-Loop Rule

BuildSolid agents are collaborators, not autopilots.

- Resolve and state profile and mode from explicit current instruction, an accepted durable project choice, or unambiguous current context. Ask only when competing choices materially change workflow depth, behavior, risk, scope, acceptance, or output. Persist only a durable cross-session project choice; ordinary session posture is not silently promoted into project state.
- When the agent lacks the human's preference, intent, authority, safety context, or another genuine prerequisite and the gap materially affects the outcome, it **must** ask — using `AskUserQuestion` (or equivalent clarification tooling) when available. Plain inline questioning is the agent-neutral fallback; this rule must never lock BuildSolid to one harness.
- When the answer can be inferred safely from accepted artifacts or current context, the agent **must not** ask. State the inference and do not interrupt users with questions already answered on disk.
- Mode shapes question density (`framework/docs/context-package.md` §5):
  - **Guided Mode** — ask freely; explain tradeoffs.
  - **Founder Mode** — ask sharply; pressure-test.
  - **Expert Mode** — ask only when a decision materially changes the outcome.
  - **Build Mode** — ask only when blocked.
- Irreversible or high-impact actions (deletions, deployments, public posts, destructive git operations) require explicit human confirmation regardless of mode.
- Every meaningful human decision is recorded in `decisions.md`.

If uncertainty about intent, authority, safety, or another genuine prerequisite could materially change the outcome, stop and ask. Otherwise state a safe inference and continue.

---

## 10. Artifact-Driven Workflow Rule

The artifacts in `framework/docs/context-package.md` §8 are the **system of record**. Conversations are not.

- Each **applicable** phase produces or updates durable state when the outcome requires it. Do not create an empty artifact or exhaustive applicability ledger solely to prove that a phase or artifact was omitted.
- An agent picking up a project mid-flight must be able to reconstruct state from the artifacts alone.
- New information with durable project value is captured in the appropriate artifact, not left only in chat history. Transient session posture and routine correction provenance need not become canonical project state.
- Edits to existing artifacts are preferred over creating new files. Do not fragment the canonical surface area.
- If a needed concept has no artifact, propose adding one in `decisions.md` before inventing a new file.
- Authority-sensitive knowledge moves through the proposed, accepted, superseded, derived, ephemeral, evidence/event, and working-context states defined in `framework/docs/context-package.md` §8C.
- Human review promotes authority-sensitive proposed knowledge into accepted canonical state. Agents may propose, draft, and execute approved edits, but they must not silently promote contested, missing, or high-impact decisions.

Artifacts are the durable memory. Treat them that way.

### Repository governance, Framework, Project System, and Publication

Repository governance controls branch and merge policy, confidentiality, migration, repository settings, release preparation, publication controls, and provenance. The Framework constitution controls normative BuildSolid meaning. Repository governance may impose stricter operational controls but may not redefine, weaken, or publish a different Framework contract.

Project System packages, instantiates, and demonstrates the applicable Framework contract through conforming skills, templates, examples, and guidance. It may specialize presentation but may not redefine, weaken, contradict, or bypass Framework. A Project System need that conflicts with Framework must return as a Framework change proposal.

Publication selects and assembles only an exact, separately accepted public package. It may transform wrappers, navigation, and paths only when the transformation is recorded and semantically equivalent to the accepted source. Publication owns no normative meaning and cannot promote non-public, Proposed, or transformed content by implication.

Publication is default-deny. A path is authorized only when it is listed individually in a release-specific file-by-file allowlist recorded in tracked Markdown and accepted for the exact publication. The allowlist may list Markdown source files and the exact non-Markdown license or legal file separately accepted at the first-publication gate; listing such a file does not select or accept its contents. Globs, directory inclusion, frontmatter, visibility metadata, omission from a denylist, or file location never authorize publication.

---

## 11. Skill Quality Standard

Every BuildSolid skill must satisfy the following before it is considered done:

1. **Single purpose.** A one-sentence description of what the skill does and does not do.
2. **Trigger conditions.** When the orchestrator (or a user) should invoke this skill.
3. **Inputs.** Which artifacts and which user context the skill expects.
4. **Outputs.** Which artifacts the skill produces or updates, and in what shape.
5. **Mode behavior.** How the skill behaves in Guided, Founder, Expert, and Build modes.
6. **Question policy.** What the skill must ask, what it may assume, and how it confirms before destructive actions.
7. **Done criteria.** How the agent (and the user) know the skill has finished its job.
8. **Failure modes.** What the skill should do when inputs are missing, conflicting, or out of scope.
9. **Portability note.** Any Claude-Code-specific behavior, and the agent-neutral fallback.
10. **Reference example.** A *pointer* to the relevant section of the freelance-photographer reference project showing how the skill behaves. Do not embed or duplicate the reference project inside the skill file.

A skill missing any of these is a draft, not a skill.

---

## 12. Template Quality Standard

Every BuildSolid template (the artifacts in `framework/docs/context-package.md` §8) must satisfy:

1. **Purpose statement.** One sentence at the top: what this artifact is for and who reads it.
2. **Required sections.** The minimum sections any project must fill in.
3. **Optional sections.** Clearly marked, with guidance on when to include them.
4. **Inline guidance.** Short prompts inside the template explaining what to write — removable once filled.
5. **Stable headings.** Section titles that other skills can rely on (no surprise renames).
6. **Cross-references.** Links to the related artifacts and to the relevant phase.
7. **Example fill.** A *pointer* to the relevant section of the freelance-photographer reference project showing a worked example. Do not embed or duplicate the reference project inside the template.
8. **Agent-neutral content.** No instructions that only make sense in Claude Code.

Templates evolve, but their core sections are part of the contract between skills.

### Framework ownership and Project System conformance

Framework defines the normative Skill Quality Standard and Template Quality Standard. Project System packages skills and templates that conform to those standards. Packaging, public presentation, examples, wrappers, paths, or host ergonomics may not reduce, redefine, or bypass a numbered requirement. Any proposal to change a standard is a Framework change and must identify compatibility and migration impact before founder review.

---

## 13. Host and Workspace Convention Rule

BuildSolid is designed to work inside a normal single working tree and may also be used inside host environments such as **Conductor** for parallel agent work.

- BuildSolid must work for a single agent in a single workspace **and** for multiple agents collaborating across Conductor workspaces.
- The `.context` directory in each workspace is the appropriate place for inter-agent coordination notes that are not durable project artifacts. Durable project artifacts (`framework/docs/context-package.md` §8) **must not** live in `.context` — they are the system of record and belong in tracked project files.
- Conductor-specific affordances (parallel workspaces, shared context, agent handoffs) may be referenced as ergonomic improvements, but no BuildSolid capability may *require* Conductor to function.
- Host-specific affordances from any provider must remain optional. Do not embed Conductor-only, Claude-only, Codex-only, MCP-only, or external-memory-only assumptions into the markdown artifacts.

If it only works in a specific host environment, it is not BuildSolid — it is a host extension.

### Repository-scoped migration controls

A separately accepted repository-wide decision may authorize bounded non-canonical preparation before activation and may use controls such as an exact execution baseline, one frozen integration branch, one integration owner for canonical writes, read-only supporting reviewers, immutable evidence, targeted invalidation, human merge authority, or a no-agent-merge rule. Those controls govern only the exact preparation and migration named by the accepted decision. They are not permanent Framework principles, do not govern downstream projects or public users, do not make Conductor or any other host required, and do not authorize activation, external action, publication, release, or merge merely by being described or prepared.

---

## 14. Provider Tooling Rule

Provider-specific tools and skills are welcome where they materially improve the experience, subject to §8 (Agent-Agnostic).

Permitted as optional ergonomics:

- Using Claude's `skill-creator` (when available) to author BuildSolid skills.
- Using `AskUserQuestion` for human-in-the-loop clarification.
- Using subagents, slash commands, hooks, and other host-provided UI or workspace ergonomics.
- Documenting Claude-Code-specific conventions in `CLAUDE.md`.
- Documenting equivalent Codex, Conductor, or future-host conventions in clearly scoped host-specific guidance.

Required guardrails:

- Any provider-specific behavior must have a documented agent-neutral fallback.
- Provider tooling must never become the *only* path to use a BuildSolid capability.
- Skill files must remain readable and useful even if provider-specific tools are not available.
- For human-in-the-loop clarification specifically, the agent-neutral fallback to `AskUserQuestion` is plain inline questioning, as defined in §9.

Use host strengths. Do not depend on them.

---

## 15. Current Manual Constraints, Development Validation, Explicit Non-Goals, and Separate Platform Gate

BuildSolid remains a manual, Markdown-first, skill-first, Git/Markdown-authoritative, human-reviewed, agent-neutral, and portable Framework and Project System. Optional private development infrastructure does not change that product boundary. The following remain out of scope unless a later constitutional amendment, accepted implementation contract, and independent founder decision authorize an exact platform transition:

- A BuildSolid product CLI, binary entry point, shell command, coded product validator, runtime script, or project generator.
- A web app, desktop app, dashboard, hosted service, docs website, frontend, admin panel, or runtime surface.
- A package distributed through npm, pip, cargo, or another package system.
- A database, schema, database migration, authentication system, authorization system, or persistence layer.
- Product deployment automation, infrastructure-as-code, automated publication, synchronization automation, or automated release infrastructure for BuildSolid itself.
- Runtime services, daemons, queues, APIs, MCP servers, external memory infrastructure, or provider-backed runtime systems.
- Automated or programmatic project-generation logic. An agent may continue to populate artifacts manually as part of the workflow.
- Runtime or coded integrations with Spec Kit, OpenSpec, Kiro, BMAD, GStack, GBrain, Cognee, Graphiti, Mem0, Letta, MCP, Claude Code, Codex, Conductor, or another host runtime.
- Telemetry, analytics, usage tracking, billing, or commercial mechanics.
- A BuildSolid rename, a BuildSolid Development product rename, or a Core / Development product or repository split.
- Implementation of BuildSolid Design, Support, Marketing, Operations, or another horizon domain.
- Artifact, skill, mode, stage, profile, or permanent-principle removal, merge, or rename without founder approval and migration guidance.
- `starter-stack-advisor` merge or removal without new validation evidence and a separate founder decision.

### Development-only validation exception

BuildSolid's development repository may use a small repository-owned validator, tests, and CI workflow when an exact accepted repository decision or task contract authorizes them and all of the following remain true:

- they check deterministic repository invariants and do not define, generate, promote, publish, or release canonical BuildSolid meaning;
- they use no secrets, production or customer data, publication credentials, or repository write authority;
- they are dependency-light, reviewable, mechanically retryable, and accompanied by a normal-checkout native or manual fallback;
- provider-specific workflow configuration is optional and does not become a public or downstream dependency;
- a validator implementation failure is distinguished from a contract failure and may be corrected and rerun without creating a new governance event; and
- publication, release, repository settings, external synchronization, and destructive operations remain outside the exception.

This exception is BuildSolid development infrastructure, not a platform transition, BuildSolid capability, product runtime, integration, or permission for automation listed elsewhere in this section.

License selection and first publication remain prohibited unless and until the later first-publication gate selects either no publication or one unmodified standard license together with a founder rights/provenance attestation, an exact release-specific file allowlist and path map, no external contributions initially, treatment of every concrete legal red flag, and one exact candidate, version, and publication action. Counsel escalation is required when a concrete red flag exists, including another copyright holder, employer or client ownership ambiguity, copied or adapted third-party material, custom or incompatible licensing, known patent concerns, or contested branding. Absence of a license, attestation, allowlist, path map, or exact decision is never permission to publish.

Repository-topology changes, first publication, public validation, and release acceptance are independent effects. A fresh task contract and exact founder authorization must govern any consequential repository operation. The first-publication gate governs content and license publication. Read-only validation of the exact public candidate requires no separate validation-authority decision and grants no released authority. The release gate alone may accept, reject, defer, or withdraw the exact commit and version. Preparation, validation, evidence, repository creation, and publication do not open another gate automatically.

Future architectural permissions are not current authorization. A platform proposal must provide founder-reviewable evidence of all of the following before implementation can be authorized:

- a repeated user problem that the manual Framework and Project System cannot solve adequately;
- alternatives showing why documentation, skill, template, or host-native ergonomics are insufficient;
- exact proposed runtime or tooling scope and non-goals;
- a preserved public Markdown and single-agent fallback;
- security, privacy, threat, data, maintenance, cost, support, and licensing analysis;
- compatibility and migration treatment for existing public and downstream users;
- an explicit constitutional amendment proposal;
- an accepted implementation contract proportionate to the proposed product or platform scope; and
- an independent founder decision authorizing implementation.

Until all platform-gate conditions are met, platform, runtime, product CLI, service, integration, product automation, infrastructure, and coded publication work remain unauthorized. The development-only validation exception above does not waive those boundaries.

If a contributor believes an otherwise prohibited capability is necessary, they must stop, record the proposal and evidence in the applicable decision system, and wait for the exact constitutional and founder approvals required by the affected layer and gate. Adding prohibited scope without those approvals violates the constitution.

---

## 16. Review and Acceptance Criteria

Every change to BuildSolid is reviewed against this constitution before it is accepted.

A change is **acceptable** if and only if:

- It is in scope for the current version (§2) or accompanied by the required accepted decision and constitutional amendment.
- It does not introduce anything prohibited by §15 outside the development-only validation exception.
- It respects the markdown-first (§4) and skill-first (§5) rules.
- It does not break the spec-before-implementation rule (§6).
- It preserves agent-agnostic portability (§8).
- It honors the human-in-the-loop rule (§9): asks when it should, assumes when it safely can.
- It preserves Git plus human-readable Markdown as the authority for accepted knowledge (§4, §10).
- It preserves human-reviewed promotion for authority-sensitive changes (§9, §10).
- New or changed skills meet the Skill Quality Standard (§11).
- New or changed templates meet the Template Quality Standard (§12).
- Decisions of consequence are logged in `decisions.md`.
- `CLAUDE.md` and `AGENTS.md` remain in sync: no convention is duplicated across the two, and none contradicts the other (per §8).
- The freelance-photographer reference project still walks cleanly through the affected phases.

A change is **rejected** if it:

- Introduces a product CLI, web app, package, runtime service, database, auth, product deployment automation, external integration, MCP server, telemetry, or project-generation logic.
- Locks the workflow to a single AI coding agent.
- Bypasses specs to ship implementation.
- Adds scope without justification.
- Buries human-relevant decisions in chat instead of in artifacts.

Implementation agents must stop for founder approval before removing, merging, or renaming a lifecycle stage, mode, canonical artifact, skill, or permanent principle; executing any skill rename; merging or removing `starter-stack-advisor`; adding a new canonical artifact; changing Git/Markdown authority; relocating, merging, deleting, or fundamentally reshaping `.handoffs/`; introducing anything in §15; renaming BuildSolid; splitting Core and Development into separate products or directories; promoting a horizon domain into active scope; or treating validation limits as stronger evidence than they are.

Amendments to this constitution are themselves changes and must be proposed, reviewed, and recorded in `decisions.md` with rationale. Any amendment that changes permanent principles, current-version constraints, future architectural permissions, or founder-gated stop conditions requires explicit founder review. The constitution is the slowest-moving document in the repo by design.

### Public completeness, provenance, and founder gates

Repository topology, content publication, public validation, release acceptance, and tag or release presentation remain independent effects. A repository operation does not publish content, select a license, accept a release, or authorize a later effect by implication. Each consequential mutation requires its exact current founder authorization and successful prerequisites.

First publication requires one later founder decision selecting one unmodified standard license or no publication, a founder rights/provenance attestation, an exact public allowlist and path map, no external contributions initially, treatment of every concrete legal red flag, and the exact candidate, version, and publication action. Counsel escalation is required only when a concrete legal red flag exists.

The exact public candidate may be inspected and validated read-only without a separate founder validation-authority decision. Validation evidence grants no released authority. A later founder decision must accept, reject, defer, or withdraw the exact commit and version. Acceptance is necessary but does not create a tag or GitHub Release; released authority attaches only when the matching annotated version tag selects the accepted commit.

Git, pull-request, review, check, and authoritative readback records are the default provenance for Routine and Guarded work. Preserve existing evidence append-only and create a new immutable evidence row only for a non-reconstructible Consequential observation with lasting decision value or when an accepted task explicitly requires one for a material boundary. Dependencies establish order only. No decision, review, task, commit, PR, merge, synchronization, validation, evidence row, confirmation, repository operation, or publication opens another gate or authorizes another candidate by implication.
