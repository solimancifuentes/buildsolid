---
name: workflow-improver
description: Diagnose an evidenced workflow failure and propose proportionate reusable guidance, or design a bounded behavioral comparison of workflow guidance. Use after a real execution, review, or evaluation exposes a workflow question; not for ordinary product bug fixing.
---

# workflow-improver

> A BuildSolid skill following the Skill Quality Standard in `framework/docs/constitution.md` §11 and the applicable profile and mode contracts in `framework/docs/context-package.md`.

**Purpose:** Explain an observed workflow failure and recommend the smallest evidence-backed reusable correction, or evaluate whether a proposed correction helps.
**Inputs:** The observed request and outcome, applicable accepted guidance, relevant task or review evidence, and the proposed change if one exists.
**Outputs:** A diagnosis with uncertainty and a routed recommendation; when comparison is warranted, a predeclared evaluation method and honest result.
**Success:** A fresh agent can distinguish a recurring guidance defect from a one-off error, inspect the evidence, and act through the proper artifact owner without inventing authority or a new record.

---

## 1. Single purpose

Improve the workflow from observed behavior. Diagnose whether the guidance is absent, was not triggered, was available but not followed, or whether a single execution failed despite adequate guidance. Propose a reusable change only when the evidence supports one. Product implementation, report triage, and acceptance of changed project intent remain with their owning workflows.

## 2. Trigger conditions

Use when a user asks to reflect on a workflow failure, a review finds a repeatable process gap, or Stage 13 routes evidenced workflow learning here. Direct entry is valid with a bounded question and actual case evidence; an orchestrator pass is not required. A single bad output can justify investigation but does not establish recurrence. For an incoming product report, use the orchestrator's [manual report intake](../buildsolid-orchestrator/references/report-intake.md) first if its route is unclear.

## 3. Inputs

Identify the concrete request, active project profile and interaction mode, accepted task contract, guidance available at the time, actual output or action, and observed consequence. Record source, revision or date where material, and what was or was not available to the actor. Compare the applicable trigger and instruction with the failure path; do not infer noncompliance from a missing transcript or infer missing guidance from one surprising result. Prior cases may establish recurrence only when they are independently evidenced and comparable. Read [reflection](references/reflection.md) for classification; read [evaluation](references/evaluation.md) only when a proposed guidance change needs a behavioral test.

## 4. Outputs

Return a short diagnosis in the current task, review, or change record: observed facts with pointers, classification and alternative explanations, recurrence evidence or its absence, affected instruction/trigger, smallest proposed correction, owner, expected behavior, and a way to check it. Mark inference and unknowns. Keep proposed guidance proposed until accepted through its normal artifact owner and authority path. Persistent issues go in `known-issues.md` only when they must survive sessions; meaningful accepted choices go in `decisions.md`. No new reflection file, score, preference store, or evaluation dossier is required.

## 5. Mode behavior

Apply the central interaction policy in `framework/docs/context-package.md` §5:

- **Guided Mode.** Explain the observed failure and candidate cause.
- **Founder Mode.** Test whether the correction changes a material goal or authority boundary.
- **Expert Mode.** Lead with evidence and actionable scope.
- **Build Mode.** Diagnose the obstacle to the accepted task and return to execution without expanding it.

A user's writing or tooling preference is a preference, not a fifth mode or a durable mode change.

## 6. Question policy

Ask only for missing evidence or a material choice that cannot be resolved from accepted context and would change the diagnosis, scope, or authorization. State a bounded assumption when safe. Do not ask the user to reconfirm an already accepted in-scope correction. A proposed change to accepted intent, behavior, or a consequential effect goes through its actual human gate; a workflow diagnosis itself grants no implementation or external-write authority.

## 7. Done criteria

The result identifies the actual case and applicable guidance, separates observation from inference, makes one of the four classifications or remains explicitly inconclusive, and recommends no broader change than the evidence warrants. If evaluated, the comparison uses criteria fixed before trial, a current baseline and candidate, isolated outputs, appropriate controls, and a conclusion limited to observed cases. The owning skill or artifact receives the actionable change; ordinary same-scope correction can remain in task/review provenance.

## 8. Failure modes

- **No inspectable case:** request the smallest missing output or source, or report that the cause is unknown; do not fabricate recurrence.
- **Guidance existed but was missed:** inspect discovery and trigger separately from instruction content; do not rewrite sound guidance solely because it was not loaded.
- **A one-off execution error:** correct the task within its accepted scope; add a reusable instruction only if a general failure mechanism is evidenced.
- **Evaluation favors a candidate in one trial:** report the observation, not general superiority. A failed or insensitive control leaves the method inconclusive.
- **Proposed change crosses project authority:** route to the owning accepted artifact and gate before treating it as current guidance.

## 9. Portability note

One agent can apply this skill by reading Markdown, task/review outputs, and ordinary Git state in a normal checkout. Host traces, subagents, telemetry, and model-cost accounting are optional evidence sources, never prerequisites. No external message, ticket, preference update, or code mutation follows automatically from a diagnosis.

## 10. Reference example

The [reflection procedure](references/reflection.md) includes a small illustrative missed-trigger case and the counterevidence that would change its classification. The [evaluation procedure](references/evaluation.md) shows how to compare a shared workflow function with a new capability without treating a baseline's legitimate refusal as failure. These are methods, not claims of an executed project result.
