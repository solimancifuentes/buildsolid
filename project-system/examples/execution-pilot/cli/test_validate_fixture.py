"""Real disposable Git fixtures for the example-only checker."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import shlex
import signal
import subprocess
import sys
import tempfile
import time
import unittest


CHECKER = Path(__file__).with_name("validate_fixture.py")
VERIFICATION = CHECKER.parent.parent / "verification/SKILL.md"


class FixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.owned = tempfile.TemporaryDirectory(prefix="buildsolid-example-cli-")
        self.addCleanup(self.owned.cleanup)
        self.root = Path(self.owned.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.git("init", "-q")
        (self.repo / "docs").mkdir()
        (self.repo / "skills/example").mkdir(parents=True)
        (self.repo / "README.md").write_text("# Fixture\n[Guide](docs/guide.md)\n", encoding="utf-8")
        (self.repo / "docs/guide.md").write_text("# Guide\n", encoding="utf-8")
        (self.repo / "skills/example/SKILL.md").write_text(
            "---\nname: example\ndescription: Check one small fixture.\n---\n# Example\n",
            encoding="utf-8",
        )
        self.git("add", "README.md", "docs/guide.md", "skills/example/SKILL.md")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "baseline")

    def git(self, *args: str) -> str:
        result = subprocess.run(
            ["git", "-C", str(self.repo), *args],
            capture_output=True, text=True, timeout=5, check=True,
        )
        return result.stdout.strip()

    def check(self, root: Path | None = None, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--root", str(root or self.repo)],
            capture_output=True, text=True, env=env, timeout=6,
        )

    def source_copy(self) -> Path:
        source = self.root / "source-copy"
        (source / "cli").mkdir(parents=True)
        (source / "verification").mkdir()
        shutil.copy2(CHECKER, source / "cli/validate_fixture.py")
        shutil.copy2(VERIFICATION, source / "verification/SKILL.md")
        (source / "README.md").write_text("Source copy; not a fixture.\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(source), "init", "-q"], check=True, timeout=5)
        subprocess.run(["git", "-C", str(source), "add", "-A"], check=True, timeout=5)
        subprocess.run(
            ["git", "-C", str(source), "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
             "commit", "-qm", "source baseline"], check=True, timeout=5,
        )
        return source

    def run_launch_with_failing_command(self, command: str, script: str) -> subprocess.CompletedProcess[str]:
        source = self.source_copy()
        body = (source / "verification/SKILL.md").read_text(encoding="utf-8")
        launch = body.split("### Launch and doctor\n", 1)[1].split("```sh\n", 1)[1].split("\n```", 1)[0]
        files_before = {p.relative_to(source): p.read_bytes() for p in source.rglob("*") if p.is_file() and ".git" not in p.parts}
        head_before = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True, timeout=5).strip()
        fake_bin = self.root / "recipe-bin"
        fake_bin.mkdir()
        fake = fake_bin / command
        fake.write_text(script, encoding="utf-8")
        fake.chmod(0o755)
        if command == "mkdir":
            allocation = self.root / "allocation"
            allocation.mkdir()
            fake_mktemp = fake_bin / "mktemp"
            fake_mktemp.write_text(f"#!/bin/sh\nprintf '%s\\n' {shlex.quote(str(allocation))}\n", encoding="utf-8")
            fake_mktemp.chmod(0o755)
        env = dict(os.environ, PATH=str(fake_bin) + os.pathsep + os.environ.get("PATH", ""))
        result = subprocess.run(["/bin/sh", "-c", launch], cwd=source, env=env, capture_output=True, text=True, timeout=10)
        files_after = {p.relative_to(source): p.read_bytes() for p in source.rglob("*") if p.is_file() and ".git" not in p.parts}
        self.assertEqual(files_after, files_before)
        self.assertEqual(subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True, timeout=5).strip(), head_before)
        self.assertEqual(subprocess.check_output(["git", "-C", str(source), "status", "--porcelain=v1"], text=True, timeout=5).strip(), "")
        return result

    @unittest.skipUnless(Path("/bin/sh").is_file(), "shell recipe requires /bin/sh")
    def test_launch_recipe_failed_allocation_does_not_write_source(self) -> None:
        result = self.run_launch_with_failing_command(
            "mktemp", "#!/bin/sh\nprintf 'allocation failed by fixture\\n' >&2\nexit 1\n",
        )
        self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
        self.assertIn("Pilot setup stopped: temporary directory allocation failed", result.stderr)

    @unittest.skipUnless(Path("/bin/sh").is_file(), "shell recipe requires /bin/sh")
    def test_launch_recipe_failed_cd_does_not_write_source(self) -> None:
        result = self.run_launch_with_failing_command(
            "mkdir", "#!/bin/sh\nexit 0\n",
        )
        self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
        self.assertIn("Pilot setup stopped: fixture directory change failed", result.stderr)

    def test_clean_index_exit_zero_and_no_source_write(self) -> None:
        before = {p.relative_to(self.repo): p.read_bytes() for p in self.repo.rglob("*") if p.is_file() and ".git" not in p.parts}
        head = self.git("rev-parse", "HEAD")
        result = self.check()
        after = {p.relative_to(self.repo): p.read_bytes() for p in self.repo.rglob("*") if p.is_file() and ".git" not in p.parts}
        self.assertEqual((result.returncode, result.stdout.strip()), (0, "fixture-validation: passed"), result.stderr)
        self.assertEqual(before, after)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        self.assertEqual(self.git("status", "--porcelain=v1"), "")

    def test_staged_three_violations_with_independent_index_readback(self) -> None:
        readme = self.repo / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "[Missing](docs/absent.md)\n[Untracked](docs/untracked.md)\n", encoding="utf-8")
        untracked = self.repo / "docs/untracked.md"
        untracked.write_text("Only in the worktree.\n", encoding="utf-8")
        skill = self.repo / "skills/example/SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8").replace("description: Check one small fixture.", "description:"), encoding="utf-8")
        self.git("add", "README.md", "skills/example/SKILL.md")
        before = self.git("status", "--porcelain=v1")
        self.assertEqual(self.git("diff", "--cached", "--name-only").splitlines(), ["README.md", "skills/example/SKILL.md"])
        self.assertEqual(self.git("diff", "--name-only"), "")
        self.assertIn("docs/absent.md", self.git("show", ":README.md"))
        self.assertIn("description:\n", self.git("show", ":skills/example/SKILL.md"))
        self.assertTrue(untracked.is_file())
        self.assertNotIn("docs/untracked.md", self.git("ls-files"))
        result = self.check()
        self.assertEqual(result.returncode, 1, (result.stdout, result.stderr))
        self.assertEqual(result.stdout.splitlines(), [
            "missing link target: docs/absent.md",
            "untracked link target: docs/untracked.md",
            "missing skill description: skills/example/SKILL.md",
        ])
        self.assertEqual(self.git("status", "--porcelain=v1"), before)
        self.assertEqual(untracked.read_text(encoding="utf-8"), "Only in the worktree.\n")

    def test_invalid_and_nested_roots_exit_two(self) -> None:
        outside = self.root / "not-a-repo"
        outside.mkdir()
        nested = self.repo / "nested"
        nested.mkdir()
        invalid = self.check(outside)
        self.assertEqual(invalid.returncode, 2)
        self.assertIn("fixture-error:", invalid.stderr)
        nested_result = self.check(nested)
        self.assertEqual(nested_result.returncode, 2)
        self.assertIn("not a nested directory", nested_result.stderr)

    @unittest.skipUnless(os.name == "posix", "symlink fixture requires POSIX")
    def test_untracked_symlink_cannot_probe_outside_root(self) -> None:
        outside = self.root / "outside.md"
        outside.write_text("private fixture data\n", encoding="utf-8")
        (self.repo / "docs/untracked.md").symlink_to(outside)
        readme = self.repo / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "[Outside](docs/untracked.md)\n", encoding="utf-8")
        self.git("add", "README.md")
        result = self.check()
        self.assertEqual(result.returncode, 2)
        self.assertIn("link target leaves fixture root", result.stderr)
        self.assertNotIn("private fixture data", result.stdout + result.stderr)

    def test_help_is_offline_and_unavailable_git_exits_two(self) -> None:
        env = dict(os.environ, PATH=str(self.root / "empty-bin"))
        help_result = subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--help"],
            capture_output=True, text=True, env=env, timeout=3,
        )
        self.assertEqual(help_result.returncode, 0, help_result.stderr)
        self.assertIn("--root", help_result.stdout)
        result = self.check(env=env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("Git unavailable", result.stderr)

    def test_oversized_indexed_blob_is_bounded_runtime_error(self) -> None:
        readme = self.repo / "README.md"
        readme.write_text("# Fixture\n" + "[Guide](docs/guide.md)\n" * 5000, encoding="utf-8")
        self.git("add", "README.md")
        before = self.git("status", "--porcelain=v1")
        result = self.check()
        self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
        self.assertIn("Git output limit exceeded", result.stderr)
        self.assertEqual(self.git("status", "--porcelain=v1"), before)

    @unittest.skipUnless(os.name == "posix" and Path("/usr/bin/yes").is_file(), "POSIX pipe-child fixture")
    def test_exited_git_parent_with_pipe_child_is_bounded(self) -> None:
        fake_bin = self.root / "pipe-bin"
        fake_bin.mkdir()
        marker = self.root / "child-pid"
        fake_git = fake_bin / "git"
        fake_git.write_text(
            f"#!/bin/sh\n/usr/bin/yes child &\nprintf '%s\\n' \"$!\" > '{marker}'\nexit 0\n",
            encoding="utf-8",
        )
        fake_git.chmod(0o755)
        started = time.monotonic()
        child_pid = None
        try:
            result = self.check(env=dict(os.environ, PATH=str(fake_bin)))
            self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
            self.assertIn("Git output limit exceeded", result.stderr)
            self.assertLess(time.monotonic() - started, 6)
            self.assertTrue(marker.is_file())
            child_pid = int(marker.read_text(encoding="ascii"))
            for _ in range(50):
                try:
                    os.kill(child_pid, 0)
                except ProcessLookupError:
                    break
                proc_stat = Path(f"/proc/{child_pid}/stat")
                if proc_stat.exists() and proc_stat.read_text(encoding="ascii").split(") ", 1)[1].startswith("Z "):
                    break
                time.sleep(0.02)
            else:
                self.fail("pipe-owning child still runnable")
        finally:
            if child_pid is not None:
                try:
                    os.kill(child_pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass

    @unittest.skipUnless(os.name == "posix", "POSIX executable fixture")
    def test_hanging_git_read_is_bounded(self) -> None:
        fake_bin = self.root / "fake-bin"
        fake_bin.mkdir()
        fake_git = fake_bin / "git"
        fake_git.write_text("#!/bin/sh\nexec /bin/sleep 9\n", encoding="utf-8")
        fake_git.chmod(0o755)
        started = time.monotonic()
        result = self.check(env=dict(os.environ, PATH=str(fake_bin)))
        elapsed = time.monotonic() - started
        self.assertEqual(result.returncode, 2, (result.stdout, result.stderr))
        self.assertIn("Git read deadline exceeded", result.stderr)
        self.assertLess(elapsed, 6)


if __name__ == "__main__":
    unittest.main()
