---
name: verification
description: Check the execution pilot's tiny Git fixture and record criterion-linked results; use the browser fixture separately.
---

# Execution pilot verification

This project-local procedure applies the [pilot contract](../contract.md). It is a recipe, not an executed verdict. Run it from a normal checkout of this example. Only a newly allocated temporary repository is changed.

## 1. Single purpose

Exercise the example-only checker on a clean index, three planted violations and an invalid root. Record what happened for CLI-1/2/3. Browser and performance checks have their own procedures.

## 2. Trigger conditions

Use this procedure for a fresh CLI observation or when a prior result may be stale. The compact contract and permission for task-owned temporary files are enough. If only visual or interactive behavior matters, follow the [browser instructions](../browser/README.md).

## 3. Inputs

- The [pilot contract](../contract.md), Python 3.10 or newer, Git and a shell.
- The [checker](../cli/validate_fixture.py) and its offline `--help`. It accepts `--root ROOT` and reads that repository's index.
- A new temporary directory and time to inspect its contents before removing it. Record Python, Git, platform and source-checkout identity when reporting a run.

## 4. Outputs

### Launch and doctor

Start in `project-system/examples/execution-pilot` in the checkout you intend to use. Check the tools before creating the fixture. The help command needs no Git repository or network.

```sh
pilot_setup_failed() { printf 'Pilot setup stopped: %s\n' "$1" >&2; exit 2; }
python3 --version || pilot_setup_failed 'Python unavailable'
git --version || pilot_setup_failed 'Git unavailable'
python3 -c 'import platform; print(platform.platform())' || pilot_setup_failed 'platform read failed'
python3 cli/validate_fixture.py --help || pilot_setup_failed 'checker help failed'
PILOT_SOURCE=$(pwd) || pilot_setup_failed 'source path unavailable'
git rev-parse HEAD || pilot_setup_failed 'source revision unavailable'
git status --porcelain=v1 -- . || pilot_setup_failed 'source status unavailable'
PILOT_DIR=$(mktemp -d) || pilot_setup_failed 'temporary directory allocation failed'
case "$PILOT_DIR" in /*) [ -d "$PILOT_DIR" ] && [ ! -L "$PILOT_DIR" ] || pilot_setup_failed 'temporary directory invalid' ;; *) pilot_setup_failed 'temporary directory invalid' ;; esac
printf 'buildsolid-cli-pilot\n' > "$PILOT_DIR/.buildsolid-cli-owned" || pilot_setup_failed 'fixture marker write failed'
mkdir "$PILOT_DIR/repo" "$PILOT_DIR/not-a-repo" || pilot_setup_failed 'fixture directory creation failed'
cd "$PILOT_DIR/repo" || pilot_setup_failed 'fixture directory change failed'
git init -q || pilot_setup_failed 'fixture Git init failed'
mkdir -p docs skills/example || pilot_setup_failed 'fixture input directory creation failed'
printf '# Fixture\n[Guide](docs/guide.md)\n' > README.md || pilot_setup_failed 'fixture README write failed'
printf '# Guide\n' > docs/guide.md || pilot_setup_failed 'fixture guide write failed'
printf '%s\n' '---' 'name: example' 'description: Check one small fixture.' '---' '# Example' > skills/example/SKILL.md || pilot_setup_failed 'fixture skill write failed'
git add README.md docs/guide.md skills/example/SKILL.md || pilot_setup_failed 'fixture staging failed'
git -c user.name='Pilot Fixture' -c user.email='pilot@example.invalid' commit -qm baseline || pilot_setup_failed 'fixture baseline commit failed'
BASE=$(git rev-parse HEAD) || pilot_setup_failed 'fixture baseline identity unavailable'
PILOT_STATUS=$(git status --porcelain=v1) || pilot_setup_failed 'fixture baseline status unavailable'
[ -z "$PILOT_STATUS" ] || pilot_setup_failed 'fixture baseline is not clean'
```

The baseline status check must be empty. `BASE` is the disposable fixture commit; keep it separate from the source checkout's identity. Any setup failure stops before the next command; mark the affected row unverified and preserve the marked directory for inspection if one was created.

### Drive and independently observe

Run the clean case, then plant the three violations. The checker reads the staged blobs, so stage the README and skill edit and leave the linked target untracked. Do not stage an unrelated file or leave a tracked input partly unstaged.

```sh
python3 "$PILOT_SOURCE/cli/validate_fixture.py" --root "$PWD"
printf 'clean_exit=%s\n' "$?"
printf '%s\n' '[Missing](docs/absent.md)' '[Untracked](docs/untracked.md)' >> README.md
printf 'Only in the worktree.\n' > docs/untracked.md
printf '%s\n' '---' 'name: example' 'description:' '---' '# Example' > skills/example/SKILL.md
git add README.md skills/example/SKILL.md
git status --porcelain=v1
git diff --cached --name-only
git diff --name-only
git show :README.md
git show :skills/example/SKILL.md
test -f docs/untracked.md
git ls-files --cached -- docs/untracked.md
python3 "$PILOT_SOURCE/cli/validate_fixture.py" --root "$PWD"
printf 'planted_exit=%s\n' "$?"
```

Expect exit 0 and `fixture-validation: passed` for the clean case. For the planted case expect exit 1 and three separate messages: `missing link target: docs/absent.md`, `untracked link target: docs/untracked.md`, and `missing skill description: skills/example/SKILL.md`. Check that `git diff --cached --name-only` lists only README and skill, `git diff --name-only` is empty, and `git ls-files --cached -- docs/untracked.md` prints nothing while the file exists. These reads establish the fixture state independently of the checker's summary.

The sibling directory is not a repository. A nested directory is inside the fixture repository but is not its top level. Both must return exit 2 as root/runtime errors.

```sh
mkdir nested
python3 "$PILOT_SOURCE/cli/validate_fixture.py" --root "$PILOT_DIR/not-a-repo"
printf 'invalid_root_exit=%s\n' "$?"
python3 "$PILOT_SOURCE/cli/validate_fixture.py" --root "$PWD/nested"
printf 'nested_root_exit=%s\n' "$?"
```

### Evidence and feature map

Record each command, output and exit, `BASE`, the source checkout identity and dirtiness, Python/Git/platform versions, the staged and untracked readback, and the verifier in the current task or QA result. Then update the [feature map](feature-map.md) by criterion. An expected failure from a seeded violation shows that the checker detected it; the planted repository itself remains invalid.

### Cleanup

No service is started. After retaining the observations, leave the fixture and remove only the directory whose marker and repository you created. Preserve it if ownership is unclear.

```sh
cd "$PILOT_SOURCE"
if [ -n "$PILOT_DIR" ] && [ ! -L "$PILOT_DIR" ] \
  && [ -d "$PILOT_DIR/repo/.git" ] \
  && [ "$(cat "$PILOT_DIR/.buildsolid-cli-owned")" = 'buildsolid-cli-pilot' ]; then
  rm -r -- "$PILOT_DIR"
else
  printf '%s\n' 'Cleanup blocked: fixture ownership is unclear.' >&2
fi
```

## 5. Mode behavior

The mode policy in the Framework context package applies. Guided Mode explains the exit classes and independent state checks. Founder Mode tests whether the negative control targets the intended invariant. Expert Mode can report a concise receipt. Build Mode runs the accepted recipe and asks only when blocked. No mode can convert an unobserved case into a pass.

## 6. Question policy

Resolve the source checkout and allowed temporary effects from the task. Ask only if a material ownership or authority fact remains uncertain. Do not install a missing tool, edit the source checkout or clean a directory whose marker does not match.

## 7. Done criteria

CLI-1/2/3 each have an actual exit and output or a stated unverified/inconclusive reason. The planted index and untracked target have independent readback. The source checkout was not written, and cleanup applies only to the marked fixture. Browser rows remain unverified until separately exercised.

## 8. Failure modes

If a command in this recipe differs from `--help`, correct the recipe and rerun the affected observation. If the harness cannot plant a required state, record the harness gap. If a correctly planted state is misclassified, preserve the output as a checker defect. Do not change the contract to make an unexpected result pass. If the fixture has unstaged tracked edits or unexpected staged files, stop the recipe and mark the affected observation unverified: the checker still reads the index, so its exit does not prove the intended fixture state. An invalid root, Git read failure or timeout, or output beyond the checker's 64 KiB stdout and 8 KiB stderr per-call limits returns exit 2.

## 9. Portability note

The checker is a small Python 3.10+ standard-library example. It uses bounded, read-only Git calls and needs no private validator, CI, browser, service, package install or network. A competent reader may perform the same staged-blob and index checks manually when Python is unavailable, but should mark the checker execution unverified.

## 10. Reference example

The [contract](../contract.md) states the expected result, and the [feature map](feature-map.md) starts with unverified rows. The [checker tests](../cli/test_validate_fixture.py) exercise disposable real Git repositories. Their success does not replace a fresh run on the fixture whose results are being reported.
