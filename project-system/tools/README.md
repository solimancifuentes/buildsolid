# Optional local execution helpers

These standalone Python 3.10+ standard-library helpers support ordinary Markdown and Git work. They are not a product CLI, service, authority store or required setup. Use an already available Python/Git installation; the PR observer optionally calls existing authenticated `gh`. No helper installs, fetches, changes Git state, posts, merges or decides cleanup. Help is offline. JSON output is an observation for the owning task, not acceptance, merge permission or proof that a test ran.

## Check task structure and receipt identity

```sh
python3 project-system/tools/validate_execution.py path/to/contract.md
python3 project-system/tools/validate_execution.py path/to/tasks.md --full
```

The compact machine-readable subset is an ID heading (for example `### A1 — Clarify output`) plus `Status`, `Acceptance` and `Dependencies` fields. IDs include a letter and a digit, with optional letters, digits, hyphens or underscores. Full mode also checks `Description`, `Files`, `Inputs`, `Parallelizable` and `Review`, matching the existing full template. This opt-in subset is not a universal prose format: an adequate contract outside it remains usable through manual review.

Field labels can be bold or plain, with normal continuation lines. `Done condition`/`Acceptance criteria`, `Depends on`, `Command` and `Tested revision` are recognized aliases. Status remains one of Not started, In progress, Blocked or Done, allowing case and terminal punctuation differences. Dependencies can be comma/semicolon/and-separated IDs, Markdown ID links, or an explicit None/no dependencies/independent. Ambiguous repeated fields, duplicate/missing IDs, unsupported status, unknown dependencies and cycles are reported. Dependency prose outside the subset is unknown rather than guessed. Fenced examples, HTML comments and blockquoted template guidance do not count as tasks; an unclosed fence/comment makes parsing uncertain.

```md
### A1 — Clarify the existing diagnostic
**Status:** In progress
**Done condition:** Invalid input names the missing field.
  Valid input still produces the existing output.
**Depends on:** no dependencies
```

This structurally valid snippet does not establish accepted intent, adequate scope/effects, implementation or review. The helper always reports `semantic_acceptance: not_evaluated` and `test_execution: not_asserted`. A Done task depending on an unfinished task returns unknown; even all-Done labels are not behavioral evidence.

Material receipts are checked only when a task has a `Receipt` field or the caller explicitly selects `--material-task A1` (repeatable). Ordinary tasks need no screenshots, benchmark, receipt file or invented proof ritual. Put the following subset in the existing task/QA section when machine checking is useful; a compact prose receipt can instead be reviewed manually:

```md
**Receipt:** material
**Repository:** /absolute/path/to/the/tested/repository
**Revision:** <full immutable commit ID>
**Base:** <full relevant base commit ID, or Not applicable>
**Environment:** <material runtime and dependency identity>
**Procedure:** <exact command or manual steps>
**Expected:** <accepted expected condition>
**Outcome:** passed
**Evidence:** [output](<evidence/result.txt>) sha256:<64 hexadecimal digits>
**Verifier:** <identity and method>
**Snapshot:** clean
```

Provide `--repo /path/to/checkout` for read-only Git identity checks and `--base current-local-ref` when a relevant base is named. No remote is fetched. Repository identity must match the supplied checkout's absolute path or configured origin URL. The helper checks commit existence, current HEAD, current dirty state and supplied base identity. A valid-looking nonexistent commit is unknown; an old real commit or changed base is stale. With no `--repo`, receipt revision verification remains unknown. An unrelated documentation edit may allow scoped reuse after manual analysis; this conservative checker cannot prove that independence and does not silently rewrite the receipt.

Evidence rows contain a local path and SHA-256, one per continued line. Paths are relative to `--root` (default the contract's directory), must stay inside it after symlink resolution, and must be regular files up to 32 MiB. Missing/unreadable evidence is unknown; changed bytes are stale. A dirty receipt also needs `Source files` rows in the same path/digest format identifying the observed material inputs. Matching listed files does not prove that the chosen input set is sufficient, that a retained patch was applied, or that evidence came from the claimed test. Review those bindings manually. The helper does not fetch external links or read artifact paths outside the explicit root; it creates no evidence database.

Exit **0** means only the supported structure and any supplied identities passed these mechanical checks. Exit **1** reports invalid structure/receipt fields. Exit **2** reports unsupported/incomplete parsing, unavailable identity, stale evidence, deadline or cancellation. `--timeout` bounds Git/identity reads (default 30 seconds, maximum 300); Git calls are individually capped at five seconds and remaining time. Contract input is limited to 4 MiB. A failed or unverified material outcome cannot become a mechanical pass by its label.

Manual fallback: read current accepted intent and task fields, check unique IDs/status/dependency graph, then compare each material observation with actual repository/commit, dirty inputs, relevant base/environment, expected/observed result and evidence. A digest establishes bytes, not provenance or acceptance. Recheck only materially invalidated evidence and preserve honest uncertainty.

## Inventory worktrees without cleanup

```sh
python3 project-system/tools/inventory_worktrees.py --root /path/to/checkout
python3 project-system/tools/inventory_worktrees.py --root /path/to/checkout --base local-ref
```

The inventory uses local NUL-delimited worktree/status records, including spaces and newlines. It reports tracked changes, untracked and ignored paths, detached/branch identity, local base provenance and commits outside base/upstream where available. Base selection is local remote-HEAD/config information or explicit `--base`; absent information remains unknown. Remote information is not refreshed, and PR status is unknown. An ancestor relation, closed PR or squash merge cannot establish that useful work is disposable. No size traversal or deletion is performed.

Manual fallback: inspect `git worktree list --porcelain -z`, each worktree's `git status --porcelain=v1 -z --ignored=matching`, locally available base/upstream refs and relevant `git rev-list --count` results. Preserve tracked, untracked, ignored and unpublished work; separately inspect current PR/content state when relevant. Cleanup is a distinct human-authorized action, never an inventory result.

## Observe one PR conservatively

The observer's exact invocation and requirements are described in the executor's [read-only observation procedure](../skills/implementation-executor/references/observation.md). Start with an on-demand read; without an evaluated requirement contract it reports observations and unknown acceptance. Treat incomplete policy, pages, permissions, dependencies or moving revisions as unknown. Every result names the observed repository/PR/head/base and retains the distinction between technical check state and applicable human authority.
