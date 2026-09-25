# Resume, ownership and revision evidence

Use on pickup, a failed worker, an interrupted command, or when evidence may describe an older state. This is a readable procedure; no coordination service or helper is required.

## Reconstruct the current task

Read the accepted contract and applicable task outcomes first. Confirm repository identity, branch, current commit and dirty state with native Git (`rev-parse --show-toplevel`, `rev-parse HEAD`, `status --porcelain=v1 -z`). Read current diffs and relevant history; do not reset, stash, fetch, switch branches or overwrite unfamiliar work merely to make pickup easier. Inspect available PR state for the exact repository and number when it affects the task. An unavailable remote leaves that fact unknown.

Compare the handoff with evidence, rather than choosing whichever account sounds newer:

| Observation | Consequence |
|---|---|
| A commit is an ancestor of the actual integration base | The commit is integrated there; inspect relevant current content/tests before concluding its behavior still exists. |
| A later revert or edit removes the fix | Integrated history does not prove the fix remains effective. Reopen the affected task/verification against current accepted intent. |
| A diff or untracked file exists only in the checkout | Preserve it and identify ownership. It is neither a clean-commit result nor evidence of merge. |
| Only a proposal, plan, branch name or “done” message exists | Do not infer implementation, review, merge or acceptance. |
| A squash merge has no source-commit ancestry | Use actual PR merge identity plus resulting content and tests; absent ancestry alone proves neither loss nor integration. |

Select the first genuinely unfinished task with satisfied dependencies. Report material uncertainty and the next observable condition. A missing required dependency blocks its dependents even if an endpoint task has a green receipt. Same-scope repair stays in the accepted envelope; new intent or effects return to the owning contract. A user hold stops execution and ownership reassignment until the user resumes it.

## Transfer writing ownership safely

Before delegation, identify the files, worker, allowed commands/effects, acceptance, deadline and stop condition. One integration owner controls shared task/Git state. Readers may run independently; writers on the same file may not.

After failure or interruption:

1. Tell the old worker to stop and revoke its assignment. Interrupt/cancel it if supported. Record any command or process identifiers that can still write.
2. Establish that all potentially writing commands and children have finished: wait for terminal/subprocess completion and inspect the relevant process group or host job state. Stopping the model does not stop an already launched shell. A late message, quiet output or a stable file hash over a short interval is not proof of quiescence.
3. Inspect the final diff and reconcile partial writes against accepted scope. Preserve unfamiliar/user work. After a failed external mutation, obtain authoritative readback before deciding whether the original grant permits an idempotent continuation; ambiguous/partial state blocks retry.
4. Only then assign a new writer and provide the actual current snapshot. Reject a delayed patch/result from the revoked worker; inspect it as evidence only and never apply it automatically.

If a potentially writing process cannot be accounted for, block its files and continue useful disjoint work. Do not kill unrelated processes, delete locks or override permissions. The sequential fallback is to run one task at a time and wait for its commands before proceeding; do not claim independent review merely because the same agent reread its work.

## Compact receipt in the owning task or QA result

Record enough identity to reproduce a material result; omit irrelevant ceremony:

- repository identity and actual observed commit;
- dirty state: when dirty, identify the tested tracked diff and relevant untracked inputs by retained patch/content digests, not just `HEAD`; a clean receipt requires a clean tested snapshot;
- relevant integration base, upstream/task dependencies and their verification status;
- material runtime, dependency and environment identity (for visual evidence include viewport/fonts/state);
- exact command or manual procedure, expected condition, actual outcome (`passed`, `failed`, `unverified`, `inconclusive`) and evidence location;
- verifier identity/method and material limitations.

A short prose receipt is sufficient. An optional checker may require an explicit machine-readable subset when invoked, but its schema is not a new authority system. A timestamp, branch name, screenshot filename or claim of success without the tested identity cannot establish freshness.

At reuse, compare the receipt to current head, relevant base/dependencies/environment and actual evidence. Invalidate only affected results: an unrelated documentation edit can preserve a result when its independence is demonstrated; a changed implementation, relevant dependency, render environment or pending required gate prevents reuse of the affected success. Do not mechanically rerun every unchanged check. Do not rewrite old evidence to pretend it tested the new state; append the new result in ordinary provenance.

## Illustrative pickup

A task says “fix merged,” and its receipt names commit A. Git shows A in the integration history, followed by revert B; the current regression test fails. The correct pickup is a reverted fix requiring current repair/verification, not Done because A is reachable. If another writer still has a child process editing the affected file, preserve the state and block ownership transfer until that process is accounted for. This example illustrates the decision; it is not an executed test report.
