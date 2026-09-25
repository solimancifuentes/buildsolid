# Start from the outcome

Use these recipes from one normal checkout with one competent agent. Read the linked Markdown skill and apply its procedure directly; no skill installer, orchestrator session, subagent, worktree or helper executable is required. [Framework](../../framework/docs/context-package.md) owns modes, profiles, prerequisites and authority. These recipes teach entry and proof, not new gates.

Resolve the project profile and interaction mode from the current instruction, accepted project choice or unambiguous context; state an inference and ask only when competing choices materially change the work. New Product Build, Existing Project Change and Lightweight/Internal Build describe workflow depth. Guided, Founder, Expert and Build describe interaction. A preference for short answers is not a fifth mode. Existing full `spec.md` / `plan.md` / `tasks.md` projects remain valid; an adequate compact contract needs no redundant copies.

## Plan a new product

**Outcome:** A concrete problem, intended user and bounded product direction that can proceed into the applicable planning stages.

**Start with:** The idea and what is actually known about the user/problem. No prior artifact is needed for intake. Example: "Guided Mode, New Product Build. Help me plan a private booking tracker for my tutoring practice; I have three tutors and currently double-book rooms." This is an illustrative prompt, not evidence about a real customer.

Read [founder-discovery](../skills/founder-discovery/SKILL.md) directly when discovery is the next need. If the entry itself is unclear, use [buildsolid-orchestrator](../skills/buildsolid-orchestrator/SKILL.md) to route. Resolve only material unknowns and record the resulting intent in the applicable existing [templates](../templates/). Distinguish observed evidence from assumptions. Continue through scope, journeys, architecture and the applicable planning artifacts as the actual project needs them; AI depth applies only when AI is load-bearing.

**Invariant:** Planning does not silently accept guesses, authorize implementation or deploy a product. New Product Build uses the full flow by default, with reasoned exclusions where genuinely inapplicable.

**Proof and handoff:** A cold reader can identify the user, problem, intended outcome, scope/non-goals, uncertain assumptions and next genuine prerequisite. Missing intent remains a question or proposed state. Once intent/approach/tasks/acceptance/effects are accepted and actionable, Stage 9 can use [implementation-executor](../skills/implementation-executor/SKILL.md); a discovery conversation alone is insufficient.

## Fix a bounded bug in an existing project

**Outcome:** Restore accepted behavior and prove the relevant regression without adding a feature.

**Start with:** Expected behavior, symptom/input, current code/tests and accepted scope/effects. State Existing Project Change and the resolved mode. Example: "Expert Mode. Empty labels must return a validation error, but they currently save. Fix only that path and its regression test; local edits/tests are authorized. No deployment." Reuse the owning contract or task; do not create a parallel stack.

If mechanism or impact is unknown, use [project-investigator](../skills/project-investigator/SKILL.md) for a read-only explanation first. Record the compact impact outcome in the existing plan/task: direction test, entry stage, affected artifacts or stages, required downstream gates and material exclusions. Then apply [implementation-executor](../skills/implementation-executor/SKILL.md) and its [bug procedure](../skills/implementation-executor/references/task-types.md). Exercise the intended failure before the fix when reproducible, repair the responsible path, and check valid-input behavior plus affected consumers.

**Invariant:** A failing unrelated test does not reproduce this bug. Do not change accepted expectations to hide a defect or classify ordinary remediation as substantive Stage 13 learning.

**Proof and handoff:** Record actual revision/dirty inputs, command/input, before/after result and limits in the task. If reproduction is unavailable, explain the limit and alternative proof. Hand implemented scope and honest coverage to [qa-reviewer](../skills/qa-reviewer/SKILL.md); a green command alone does not accept the task.

## Complete a small internal task

**Outcome:** Make a bounded internal change with proportionate intent and proof.

**Start with:** Lightweight/Internal Build, a resolved mode, and one adequate Markdown contract. For example, an accepted task may ask to add a `--quiet` option to an existing local report, name the files/consumers, preserve default output and error exits, authorize local edits/tests, and require quiet success with unchanged failure behavior. That contract carries intent, scope/non-goals, approach/dependencies, actionable tasks/status, acceptance/review and allowed effects/stop rules. These are semantic requirements, not mandatory separate filenames.

Use [task-breakdown](../skills/task-breakdown/SKILL.md) only if actionable tasks are missing; use [spec-planner](../skills/spec-planner/SKILL.md) if material intent/approach is missing. When the contract is sufficient, directly apply [implementation-executor](../skills/implementation-executor/SKILL.md). Check the changed behavior and critical invariants using the project's existing commands or executable manual steps. No UI requirement means no invented screenshot; no performance claim means no benchmark ritual.

**Invariant:** Small scope does not remove acceptance or effects authority. A disposable experiment additionally needs its question, boundary, observable result, resource/time bound and disposal/promotion rule. Its result cannot silently become production code.

**Proof and handoff:** The current task records what actually changed, what ran, the observed result and what remains unverified. The [optional task checker](../tools/README.md#check-task-structure-and-receipt-identity) can check a supported Markdown subset; a competent reader can perform the same mechanical review without Python. Neither route establishes semantic acceptance by structure alone.

## Review a change against its acceptance

**Outcome:** A criterion-linked review that distinguishes pass, failure, missing coverage and uncertainty.

**Start with:** Accepted contract/criteria, actual changed code or artifacts, current revision/dirty state, relevant base and evidence. State the project's existing profile/mode; review does not redefine them. A partial implementation may be reviewed honestly without being accepted as complete.

Apply [qa-reviewer](../skills/qa-reviewer/SKILL.md) directly. Reuse the project's verification instructions; if they are missing or stale, [project-verifier](../skills/project-verifier/SKILL.md) can build or maintain a proportionate procedure. Separate command drift, a missing harness capability and a product bug. Inspect actual observable output/state, not only the implementer's summary. Use [adversarial review](../skills/qa-reviewer/references/adversarial-review.md) when useful: reproduce reachable claims and keep a valid singleton even when others disagree. Apply [security-reviewer](../skills/security-reviewer/SKILL.md) to the relevant security surface.

**Invariant:** Unexecuted features remain unverified; inconclusive measurements stay inconclusive. An accepted exception is not a passing criterion. A screenshot or passing endpoint cannot prove every intermediate dependency, interaction or environment.

**Proof and handoff:** Map each criterion to tested revision, procedure, observed result and evidence. Material findings route to their owning implementation, harness or instructions; recheck affected results after repair. The [runnable pilot](../examples/execution-pilot/README.md) teaches this process with deliberately planted controls. It is synthetic. The [photographer example](../examples/photographer-saas/README.md) demonstrates a full planning stack, not executed application behavior. Human acceptance, deployment and merge follow their own applicable gates.

## Resume work without trusting stale context

**Outcome:** Reconstruct the first genuinely unfinished task and resume only after ownership and evidence are current.

**Start with:** Current accepted artifacts, actual Git head/status/diff, relevant base/dependencies/environment and any authorized live review state. A handoff or chat is a hint, not accepted state. State the current profile/mode without silently persisting a temporary preference.

Read [resume, ownership and revision evidence](../skills/implementation-executor/references/recovery.md). Use [buildsolid-orchestrator](../skills/buildsolid-orchestrator/SKILL.md) when cross-stage reconstruction is needed; direct executor pickup is valid when entry and prerequisites are already clear. Reconcile merged versus proposed versus reverted behavior and tracked/untracked work. Check every material predecessor, including unfinished middle tasks. Invalidate only evidence affected by relevant change; scope any claimed reuse explicitly.

If a previous worker failed, stop it and establish that potentially writing child processes are quiescent before transferring its files. An interruption notification is insufficient. A user hold stops affected work; a late revoked patch cannot overwrite the new owner. If ownership is ambiguous, preserve those files and work only on independent authorized items.

**Invariant:** Ancestor reachability or an old green check does not prove current behavior. [Optional PR/worktree observation](../skills/implementation-executor/references/observation.md) is factual and read-only; missing pages/policy remain unknown, and no inventory grants deletion or merge authority.

**Proof and handoff:** The owning task records reconciled revision/dirty state, verified or stale evidence, actual remaining condition, current owner and next authorized action. A fresh reader can continue without the old conversation. Do not mark Done to clear a blocker.

## Learn from reports without creating a new system

For an incoming report, use [manual intake](../skills/buildsolid-orchestrator/references/report-intake.md): preserve source/readability, expected/observed behavior, uncertainty, owner and existing work before choosing bug, duplicate, possible duplicate, feature, question or uncertain route. Reading a report does not authorize a ticket, message or fix.

For an evidenced workflow problem, use [workflow-improver](../skills/workflow-improver/SKILL.md). Distinguish a missing instruction, missed trigger, noncompliance and a one-off error before proposing a reusable change. Apply its [evaluation method](../skills/workflow-improver/references/evaluation.md) when a behavioral comparison would decide the change; measure the actual outcome and retain uncertainty. A routine correction need not invent recurring failure or a new global rule.
