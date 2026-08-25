---
name: security-reviewer
description: Review an implemented project change against its accepted criteria for common security issues, secret handling, dependency posture, and relevant AI-layer risks such as prompt injection, tool-based secret exfiltration, and hallucination boundaries. Use this read-only skill in Stage 10 when the implementation and genuine acceptance inputs exist.
---

# security-reviewer

> A BuildSolid skill. Drives Phase 10 (QA and Review — security pass) of the BuildSolid workflow defined in `framework/docs/context-package.md` §6. Authored against the Skill Quality Standard in `framework/docs/constitution.md` §11.

This file is plain markdown. Use Claude's `skill-creator` to author or amend it where available; follow the same conventions by hand otherwise.

---

## 1. Single purpose

Review project changes — both code and configuration — for security issues across three areas: classic application security (secret handling, input validation, auth, dependency posture, logging hygiene), the project's threat model (the harms the project must not enable), and AI-layer-specific risks (prompt injection, data exfiltration via model tools, hallucination boundaries, model-output trust assumptions).

The skill does **not** perform functional QA (that is `qa-reviewer`), implement code, or run penetration tests. It produces a verdict and a punch list of findings with severity.

## 2. Trigger conditions

Invoke this skill when:

- A user or direct caller requests a security review and the implementation plus its accepted scope and acceptance criteria are available.
- The orchestrator routes an applicable project to the Phase 10 security pass with its genuine dependencies satisfied.
- A change touches secrets, authentication, the AI layer, external dependencies, or user data.
- The launch checklist (`launch-checklist.md` §4) requires a security pass before launch.
- A vulnerability or incident is discovered post-launch and a re-review is required.
- An accepted change materially affects the threat model or the AI layer.

Direct invocation is valid when security review is the focused purpose, the implementation and accepted acceptance inputs are current, profile and mode are resolved and stated, and no unresolved cross-stage dependency, routing ambiguity, or founder gate exists. Do **not** invoke when there is no implementation to review. Require `intelligence-layer.md` only when AI is load-bearing or affected; otherwise review the applicable non-AI security surface.

## 3. Inputs

Required artifacts:

- The implementation under review (code, configuration, infrastructure references).
- The accepted scope and acceptance criteria for that implementation — normally the applicable `spec.md`, `plan.md`, and `tasks.md` content.
- `intelligence-layer.md` when AI is load-bearing or affected, for the capabilities, prompts / policies, safety boundaries, and data-flow rules in §4 / §7.

Optional context:

- `architecture.md` §5 (external dependencies) and §8 (intelligence-layer boundary).
- `deployment.md` §2 (secrets) and §9 (compliance).
- `decisions.md` — for accepted security tradeoffs.
- `known-issues.md` — for previously-accepted security debt.
- The `qa-reviewer`'s current result and task, review, pull-request, or accepted-decision provenance when functional QA is relevant.
- A project-specific threat model if one exists.
- Resolved profile and mode from explicit current instruction, an accepted durable project choice, unambiguous current context, or the caller / orchestrator. State any inference and ask only when ambiguity would materially change the work.

User context the skill expects:

- Confirmation of the review scope (code paths, environments, capabilities).
- Disclosure of any external constraints (e.g., "this project handles PHI" or "this is a marketing site with no user data").

## 4. Outputs

Outputs this skill returns or may update:

- A **security verdict** returned to the caller: scope of the review, findings grouped by severity (Critical / High / Medium / Low / Informational), and a per-finding recommendation. For ordinary same-scope review and remediation, record the verdict in the active task, review, or pull-request provenance; do not force a `decisions.md` entry.
- `decisions.md` only when the human accepts a security exception, resolves a meaningful security tradeoff, or makes another consequential durable choice.
- `known-issues.md` only for accepted security debt that must persist across sessions, with severity and mitigation.
- For findings that require remediation, a scoped entry for the current task or review, or a draft handed to `task-breakdown` when new task decomposition is genuinely needed. The caller or orchestrator owns any cross-stage route.

The skill does **not** modify implementation code. It does not commit fixes; it reports them.

Shape rules:

- Severities are explicit. Critical and High findings block launch unless logged as accepted exceptions in `decisions.md`.
- Findings cite the file or artifact and the rule violated, not just "looks bad."
- When AI is load-bearing or affected, AI-layer findings reference `intelligence-layer.md` §7 (safety boundaries) and §4 (data flow) explicitly.
- Edited in place; no parallel versions.
- Cross-references resolve.

## 5. Mode behavior

This skill follows the central mode policy in `framework/docs/context-package.md` §5; the bullets below define only this skill's deltas.

- **Guided Mode.** Review classic appsec, the project threat model, and applicable AI-layer risks with severity rationale for each finding.
- **Founder Mode.** Pressure-test security and privacy commitments against real data paths, model boundaries, and user harm.
- **Expert Mode.** Run the review directly; surface Critical / High findings plus Informational items the project is likely not tracking.
- **Build Mode.** Review the implemented task against its accepted criteria, or resolve a specific security blocker, without expanding the agreed scope.

In every mode, the skill remains read-only over implementation and returns a severity-ranked verdict. Ordinary results use task, review, or pull-request provenance; durable decisions and persistent debt are recorded only when their actual thresholds are met.

## 6. Question policy

What the skill **must resolve**, asking only when the answer is not safely inferable and would materially change the review or its disposition:

- Confirmation of the review scope if not already declared.
- Disclosure of any compliance regime (GDPR, HIPAA, SOC 2, etc.) the project is committed to, when not already in `spec.md` / `architecture.md` / `intelligence-layer.md`.
- For each Critical / High finding that will not be fixed before the relevant gate, whether the human explicitly accepts the exception and mitigation; that consequential choice goes into `decisions.md`, with persistent debt also captured in `known-issues.md` when needed.
- Human authority before treating a `launch-checklist.md` §4 security item as passed.

What the skill **may assume**:

- Anything the implementation does is in scope for review.
- Secrets in the repository (committed `.env` files, hardcoded keys, embedded tokens) are Critical findings unless the project has a logged exception.
- When AI is load-bearing or affected, the AI layer's stated safety boundaries (`intelligence-layer.md` §7) are the contract; deviations are findings.
- Logs that contain secrets, credentials, or sensitive user data are findings (per `project-system/templates/launch-checklist.md` §4).
- The resolved profile and mode when they can be inferred unambiguously from current instruction, accepted durable state, or caller context; state the inference rather than asking again.

How the skill **confirms before destructive actions**:

- The skill does not modify implementation. Acceptance of debt is a logged decision.
- Marking a `launch-checklist.md` §4 checkbox passed when a Critical / High finding is open is forbidden without a logged exception.

Asking mechanism: prefer `AskUserQuestion`; plain inline questioning otherwise.

### Categories of risks the skill covers

**Classic application security**

- Secret handling: hardcoded secrets, secrets in logs, secrets in error messages.
- Input validation: untrusted input reaching shell / SQL / file-system / model boundaries.
- Auth model: missing authn/authz, broken access control, session handling.
- Dependency posture: outdated dependencies with known CVEs, unmaintained libraries.
- Logging hygiene: PII / credentials / tokens in logs; log retention vs commitments.

**Project threat model**

- Implementations that drift into a non-goal in `non-goals.md` (e.g., adding a payment endpoint when payments are non-goal).
- Implementations that violate a `spec.md` commitment (e.g., shipping multi-tenant data without tenant isolation when spec promises isolation).
- Compliance commitments in `spec.md` / `architecture.md` / `intelligence-layer.md` not actually met.

**AI-layer-specific risks**

- **Prompt injection** — untrusted user input rendered into a model prompt without isolation; tool-using models that can be coerced into unintended actions.
- **Data exfiltration via tools** — a tool-using model that can read or transmit data outside the project's boundary (e.g., a model with shell access in production).
- **Secret exfiltration via prompts** — secrets / credentials rendered into prompts and then potentially echoed back in outputs or stored by the provider.
- **Data flow drift** — data sent to providers that `intelligence-layer.md` §4 says is "never sent to providers."
- **Hallucination boundary failures** — outputs presented to the user as authoritative when `intelligence-layer.md` §7 requires a "labeled as suggestion" presentation.
- **Eval gaps** — capabilities shipped without the eval set required by `intelligence-layer.md` §5.

## 7. Done criteria

- Every in-scope code path / configuration has been reviewed against the applicable areas; AI-layer risks apply when AI is load-bearing or affected.
- Each finding has severity, citation, and recommendation.
- The security verdict is returned and recorded in the active task, review, pull request, or durable artifact appropriate to its actual significance.
- Consequential accepted exceptions or tradeoffs are recorded in `decisions.md`; only persistent accepted debt is appended to `known-issues.md`.
- Applicable `launch-checklist.md` §4 items are evaluated; failures named.
- Return the Phase 10 security result, unresolved gates, and readiness state to the caller. Return to the orchestrator only when cross-stage routing or continuity is needed.

The user's signal that the skill is done is being able to point at the verdict and say "no Critical or High open at launch — or, the open ones are explicitly accepted with mitigations."

## 8. Failure modes

- **Genuine inputs missing.** Stop and name the missing implementation or acceptance input. Route to its owning stage or to the orchestrator only when cross-stage coordination is needed.
- **No threat model.** Use BuildSolid's defaults plus the applicable accepted `spec.md` and, when AI is load-bearing or affected, `intelligence-layer.md` commitments. Surface "the project lacks an explicit threat model" as an Informational finding.
- **Critical finding the user wants to ignore.** Refuse without a logged exception in `decisions.md` and a mitigation. The skill does not silently downgrade severity.
- **AI-layer commitments not met.** Refuse to pass the AI-layer section. Route remediation to Build Mode against `intelligence-layer.md`.
- **Substantive Stage 13 proposal reaches Stage 10 without acceptance.** When the work actually meets the material-change threshold in `framework/docs/context-package.md` §8E, block until the proposed change is accepted or rejected. Same-scope bugs, review remediation, maintenance, routine retry, and in-progress work remain ordinary Existing Project Change and do not require Stage 13 or a universal `decisions.md` entry.
- **Out-of-scope request.** If the user asks the skill to also do functional QA, redirect to `qa-reviewer`. If they ask this read-only skill to fix bugs, return the findings to Build Mode against the current scoped task or review; route to `task-breakdown` only when genuinely new task decomposition is needed.
- **Implementation drifts from `spec.md` commitments.** Per `framework/docs/constitution.md` §6, the spec is updated *first* (with logged decision); only then is the implementation accepted.

## 9. Portability note

The skill is plain markdown and contains no Claude-Code-only behavior.

Claude-Code-specific affordances and their agent-neutral fallbacks:

- **Question mechanism.** Prefer `AskUserQuestion`; plain inline questioning otherwise.
- **Subagents.** A reviewer subagent may be used to scan dependencies for known CVEs in parallel with the main review. Fallback: scan inline.
- **Skill authoring.** Prefer `skill-creator`; otherwise edit by hand.
- **MCP / tool risk note.** The skill itself runs read-only over the project files; it does not require harness-side tool integrations to function. When reviewing MCP-using or tool-using models, the AI-layer-risk checklist applies regardless of which harness the project runs in.

No Conductor- or Spec-Kit-only assumptions. The artifacts live in tracked project files, never in `.context/`.

## 10. Reference example

See the synthetic freelance-photographer reference project's artifact-level Stage 10 boundary (`project-system/examples/photographer-saas/README.md` §1):

- `project-system/examples/photographer-saas/launch-checklist.md` §4 — unchecked would-launch requirements for the security review, photographer authentication, delivery-link scoping, issue severity, logging hygiene, dependency posture, and AI-boundary tests.
- `project-system/examples/photographer-saas/decisions.md` DEC-4, DEC-5, DEC-11, and DEC-12 — provider criteria with the specific provider still unresolved, plus active-data and restore-safe retention treatment. These are planned boundaries, not a completed security-review verdict.

The example is referenced, not embedded (`framework/docs/constitution.md` §11 item 10).
