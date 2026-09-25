---
name: project-investigator
description: Investigate a project's code paths, data transformations, history, and accepted rationale without changing production state. Use for a bounded read-only technical question or before implementation when mechanism or blast radius is unclear.
---

# project-investigator

> A BuildSolid skill for bounded read-only investigation. It follows the Skill Quality Standard in `framework/docs/constitution.md` §11 and the applicable lifecycle contract in `framework/docs/context-package.md`.

**Purpose:** Answer a named technical question from inspectable project evidence without implementing a change.
**Inputs:** The question and scope, current checkout/revision, relevant code and tests, accepted project contract and decisions, and any authorized external sources.
**Outputs:** A concise finding that separates observed facts, inferences, unknowns, and contradictions, with precise evidence pointers and affected consumers.
**Success:** A fresh agent can verify the material claims, understand the uncertainty and blast radius, and decide whether an accepted implementation contract needs work before execution.

---

## 1. Single purpose

Answer a bounded question about current code behavior, data flow, blast radius, or historical rationale from evidence. This skill is read-only with respect to production code and state; `implementation-executor` owns accepted implementation work.

## 2. Trigger conditions

Use this skill when a user asks how or why a project behaves, when a bug or refactor needs mechanism discovery, or when Stage 9 routes a read-only question here. Direct entry is valid when the question and read scope are clear. A broad request to fix, build, or change production behavior routes to the executor after adequate accepted intent, approach and tasks exist (`framework/docs/context-package.md` §8B).

## 3. Inputs

- A named question, affected behavior or system surface, and the current repository/revision. Establish whether the checkout is dirty before attributing behavior to a commit.
- Relevant source, tests, configuration, call sites and consumers; inspect only what the question needs. Use focused text search and follow the actual call/data path.
- Accepted project decisions and implementation contract when the question concerns intended behavior or rationale. Git history can explain how code changed; it does not establish present intent by itself.
- External documentation or research only when the question needs it and access is available. Record source and retrieval context; distinguish it from local observations.

## 4. Outputs

Return a compact investigation result in the current task or review record; create or update a durable owning Markdown artifact only when the finding changes accepted project knowledge under its normal authority rules. Include:

1. **Question and snapshot:** scope, repository, revision, dirty-state qualifier and any relevant environment.
2. **Observed:** concrete code paths, symbols, data transformations, tests, commands or Git facts, each with a precise file/line, symbol, commit or output pointer.
3. **Inferred:** explanations supported by the observations, explicitly labeled as inference.
4. **Unknown or contradictory:** gaps, conflicting sources and the cheapest discriminating check.
5. **Impact and next step:** direct and indirect consumers, invariants at risk, and whether to stop, investigate further, or route to the accepted contract owner/executor.

Trace inputs through transformations to outputs. Inspect callers and consumers before claiming a blast radius. Prefer a small exact citation over an uncited narrative. A read-only test, diagnostic command or disposable inspection fixture may inform the answer when it stays within authorized effects; report what was actually run, and do not claim unrun behavior as observed.

## 5. Mode behavior

Follow the central mode policy in `framework/docs/context-package.md` §5. These are only investigation-specific deltas:

- **Guided Mode.** Explain the path and evidence in plain language, one meaningful step at a time.
- **Founder Mode.** Identify where a mechanism claim depends on an untested product assumption before treating it as a reason to build.
- **Expert Mode.** Lead with the finding, exact citations, uncertainty and affected consumers.
- **Build Mode.** Answer only the question blocking the accepted task, then hand control back without widening implementation scope.

## 6. Question policy

Ask only when the target question, repository, authority to inspect sensitive data, or a material intended-behavior choice cannot be resolved from current instruction and accepted artifacts. State safe scope inferences. Do not ask for permission merely to read ordinary project files or run authorized read-only checks.

This skill performs no destructive or high-impact action. If the investigation would require such an action, stop at that boundary and obtain the applicable human authorization through the owning workflow. Do not infer implementation authority from a diagnosis.

## 7. Done criteria

The result answers the named question to the extent evidence permits; material code/history claims have checkable pointers; observation, inference and unknowns are distinct; indirect consumers and critical invariants are considered; and any remaining uncertainty has a specific next check or blocker. If no reliable answer exists, a well-evidenced inconclusive result is complete as an investigation, not as implementation acceptance.

## 8. Failure modes

- **History conflicts with current code or accepted decisions:** report the contradiction and use current accepted state for intent; do not present an old commit message as current rationale.
- **Dirty or moving checkout:** identify the actual inspected state and recheck claims affected by concurrent changes before relying on them.
- **Missing evidence:** mark the claim unknown or inferred; do not fabricate a call path, runtime result or external citation.
- **Question expands into a fix or experiment:** preserve findings and route to an adequate accepted implementation contract or bounded experiment brief before effects occur.
- **External source unavailable or outside scope:** continue from local evidence where useful and state the limit.

## 9. Portability note

The procedure works for one agent in a normal Git checkout using Markdown, native search, source inspection and ordinary Git commands. Browser, search connectors or subagents are optional aids; their absence does not change the evidence standard. Any host-specific result needs a plain citation or reproducible observation that another agent can inspect.

## 10. Reference example

See [the illustrative investigation](references/investigation-example.md). It demonstrates the report shape on a tiny hypothetical code path; its snippets and findings are examples, not executed project evidence. Replace every example pointer with actual source and revision evidence during a real investigation.
