from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess


@dataclass
class GitSyncResult:
    ok: bool
    changed: list[str]
    commit: str | None
    pushed: bool
    message: str


def run_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=False)


def status_paths(repo: Path, paths: list[Path]) -> list[str]:
    rels = [str(p) for p in paths]
    proc = run_git(repo, ["status", "--porcelain", "--", *rels])
    changed = []
    for line in proc.stdout.splitlines():
        if line.strip():
            changed.append(line[3:])
    return changed


def commit_registry(repo: Path, registry: Path, message: str, push: bool = False) -> GitSyncResult:
    repo = repo.resolve()
    registry = registry.resolve()
    try:
        rel_registry = registry.relative_to(repo)
    except ValueError:
        return GitSyncResult(False, [], None, False, f"registry `{registry}` is not inside git repo `{repo}`; cannot commit for cross-device sync")
    if not (repo / ".git").exists():
        return GitSyncResult(False, [], None, False, f"not a git repository: {repo}")

    changed = status_paths(repo, [rel_registry])
    if not changed:
        return GitSyncResult(True, [], None, False, "no registry changes to commit")

    add = run_git(repo, ["add", str(rel_registry)])
    if add.returncode != 0:
        return GitSyncResult(False, changed, None, False, add.stderr.strip() or "git add failed")
    commit = run_git(repo, ["commit", "-m", message])
    if commit.returncode != 0:
        return GitSyncResult(False, changed, None, False, commit.stderr.strip() or commit.stdout.strip() or "git commit failed")
    sha = run_git(repo, ["rev-parse", "--short", "HEAD"]).stdout.strip() or None
    pushed = False
    if push:
        proc = run_git(repo, ["push"])
        if proc.returncode != 0:
            return GitSyncResult(False, changed, sha, False, proc.stderr.strip() or "git push failed")
        pushed = True
    return GitSyncResult(True, changed, sha, pushed, "committed registry changes")
