# PR and worktree observation

**Purpose:** Read one explicitly identified PR and its local worktree context without treating a technical status as permission to merge.

**Inputs:** Repository and PR number, current accepted Markdown requirements, available read-only `gh` access, and any local Git checkout to inspect.

**Outputs:** A timestamped, revision-bound observation with satisfied, unmet, or unknown conditions and a manual readback path.

**Success:** Every declared condition is evaluated from complete, stable reads; unknown or missing policy stays unknown, and the human retains merge authority.

The optional [`observe_pr.py`](../../../tools/observe_pr.py) reads the identified PR. The helper is neither required for Stage 9 nor an authority source. Its JSON requirements file is an invocation transcription of accepted Markdown, not a new canonical artifact. An observation with no requirements is useful for diagnosis but exits 2, never ready. Even exit 0 means only that the declared technical conditions were observed at the recorded head/base and interval; it never authorizes a merge.

## Optional helper invocation

From a normal checkout with an already available, authenticated `gh`:

```sh
python3 project-system/tools/observe_pr.py --help
python3 project-system/tools/observe_pr.py --repo OWNER/REPO --pr 42 --requirements /path/to/requirements.json
python3 project-system/tools/observe_pr.py --repo OWNER/REPO --pr 42 --requirements /path/to/requirements.json --watch
```

The invocation file must contain **all** fields below. Copy their meaning from the accepted task/repository requirements; absent or partial policy is not an empty policy. Use `unsupported_requirements` for accepted conditions the helper cannot prove, such as code-owner or environment-specific rules. That forces an unknown result. The example values are illustrative, not a claim about any repository:

```json
{
  "required_checks": ["buildsolid-validate"],
  "required_approvals": 1,
  "merge_gate_required": true,
  "resolved_threads_required": true,
  "dependencies": [{"repo": "OWNER/REPO", "pr": 41, "head": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}],
  "unsupported_requirements": []
}
```

`required_checks: []` is valid only when the accepted policy explicitly requires no named checks. List **every material predecessor** in the flat dependency array: if C depends on A and B, include both, even if A is already merged. A dependency is satisfied only when that exact declared head remains the observed head and the PR is merged; an unreadable or changing predecessor prevents success. This is not a recursive dependency crawler. If the chain is unknown or an earlier fix's current behavior has not been established, name that gap in `unsupported_requirements` and keep the outcome unknown. The helper observes one PR at a time; it does not establish that a dependency's resulting behavior remains in the current base. Multiple same-name check runs, even from one app, and a check run plus status context with the same required name are ambiguous without an explicit replacement identity; the helper returns unknown. Duplicate identities across API pages prevent a complete read. Check runs must name the observed head SHA; REST status items must have a canonical API URL for the requested repository and head because the list response has no item-level `sha` field. For review, the supported contract is a count of approvals by distinct reviewers whose `commit_id` is the observed head, with no live requested review or changes request. Old or missing approval commit identity is unknown when it could affect the count; if the actual rule permits older approvals or imposes other constraints, name it as unsupported.

Output is one JSON observation to stdout. Exit `0` means a complete stable read satisfied the declared, supported technical conditions; `1` means a known unmet condition; `2` means incomplete, unknown, stale, error, or no evaluated requirements; `124` means the overall deadline expired. The JSON always states `merge_permission: not_evaluated`. A one-shot read is the default with a 30-second overall budget and no transient retries. `--watch` uses a 300-second total budget, 15-second interval and at most three transient retries per read by default. Flags can shorten those bounds. Cancellation stops and waits for the owned `gh` process group. No command installs, fetches, writes Git state, opens a PR or merges it.

The interval between `started_at` and `ended_at` is not an atomic GitHub transaction. The helper reads complete paginated check, status, review and thread sets twice, bracketing them with head/base and material gate reads; it rejects movement it detects. Provider races that are not visible in those reads remain a limit. A missing permission or page remains unknown.

## Manual path

Without the helper, use `gh api` or the GitHub UI to read the exact repository, number, head and base identities, current lifecycle and draft state, all required check runs and status contexts, review history and unresolved threads, merge gate, and named dependencies. For example, `gh api repos/OWNER/REPO/pulls/42` shows PR identity and gate; `gh api --paginate repos/OWNER/REPO/commits/HEAD/check-runs`, `gh api --paginate repos/OWNER/REPO/commits/HEAD/statuses`, and `gh api --paginate repos/OWNER/REPO/pulls/42/reviews` cover the corresponding paginated REST reads. Inspect all review-thread pages in the UI or GraphQL and each declared dependency; never substitute a single page or summary badge. Read the PR identity and material gate fields again after dependent pages. Record missing pages, permissions, rate limits, changing identities, and the observation interval as unknown. A local worktree is a separate fact: inspect `git rev-parse HEAD`, `git status --porcelain=v1 -z`, relevant base and diffs before reusing its result. Do not infer a clean checkout, current behavior, or merge permission from a green PR label.
