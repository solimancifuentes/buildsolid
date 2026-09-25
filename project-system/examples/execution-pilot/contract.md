# Local execution pilot contract

This compact contract covers a synthetic verifier exercise. A reader can use the fixture and its observations to distinguish a clean Git index, a deliberately broken index, and a root/runtime error. No product or customer behavior is inferred from those cases.

## Intent and outcome

The [CLI checker](cli/validate_fixture.py) reads only the staged `README.md` and `skills/example/SKILL.md` in a tiny repository. A clean fixture has a local guide link whose target is indexed and a nonempty skill description. Its output is a diagnosis of this example, not a general Markdown or skill validator.

## Scope and non-goals

Use Python 3.10 or newer, Git, and a fresh disposable repository. The negative case adds a missing link, a link to a real but untracked file, and a blank skill description. It stages only the README and skill edit. No private repository validator, archive, remote, install, source-checkout write, production data, publication or deployment belongs in this pilot. The [browser fixture](browser/README.md) has separate expectations.

## Approach and dependencies

Follow the [verification procedure](verification/SKILL.md) from a normal checkout. It creates the tiny repository, commits a clean baseline, plants the three violations and inspects both checker output and Git's index. The checker uses bounded, read-only Git subprocesses. If Python, Git or a disposable directory is unavailable, report the affected criterion unverified rather than substituting a claim.

## Tasks

1. Run the clean committed fixture and record its exit and output.
2. Plant all three violations, stage the two edited inputs, leave the linked target untracked, and inspect the staged blobs and index independently.
3. Invoke the checker on a sibling directory with no repository and on a nested directory in the fixture repository.
4. Record criterion-level results and limits in the current task or QA result. Remove only the task-owned temporary directory after its evidence has been retained.

## Acceptance and verification

- **CLI-1:** clean fixture returns exit 0 with `fixture-validation: passed`; its index and worktree are clean.
- **CLI-2:** planted fixture returns exit 1 with separate `missing link target`, `untracked link target`, and `missing skill description` messages. The untracked target exists on disk and is absent from `git ls-files`; only the README and skill edit are staged, with no unstaged tracked edit.
- **CLI-3:** an existing non-repository root returns exit 2 with a root/runtime error. A directory nested under a repository is also rejected as a root, so it cannot be mistaken for an independent fixture.
- **BROWSER-1/2:** rendered and interaction criteria require observations under the [browser instructions](browser/README.md). CLI output cannot satisfy them.

The [checker tests](cli/test_validate_fixture.py) exercise these states in real temporary Git repositories, including offline help and a bounded hanging Git read. A seeded failure proves detection of the planted violation; it does not make the broken fixture healthy.

## Allowed effects and stop rules

The checker reads the given repository and writes nothing. The recipe may create and remove only its marked temporary fixture. Stop and report an incomplete result if the staged and worktree states become mixed, the root is ambiguous, the Git read fails or times out, or a command would affect another checkout. Do not change the expected result to match an unexpected checker output. No production promotion or external action follows from this example.
