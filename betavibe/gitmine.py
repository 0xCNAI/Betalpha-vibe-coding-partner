from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
from urllib.parse import urlparse

SIGNAL_WORDS = re.compile(r"\b(fix|fixed|bug|hotfix|regression|revert|rollback|broken|fail|failure|timeout|race|migration|auth|token|schema|ci|test|flake|crash|patch|workaround)\b", re.I)
RISK_PATH = re.compile(r"(auth|oauth|token|secret|cron|launchd|workflow|ci|docker|compose|migration|schema|database|db|config|env|payment|billing|deploy|release)", re.I)


def run(cmd: list[str], cwd: Path) -> str:
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout


def git_log(repo: Path, since: str | None = None, max_commits: int = 300) -> list[dict]:
    args = ["git", "log", f"--max-count={max_commits}", "--date=iso-strict", "--name-only", "--format=--BETAVIBE--%n%H%n%ad%n%s%n%b"]
    if since:
        args.insert(2, f"--since={since}")
    raw = run(args, repo)
    commits: list[dict] = []
    for chunk in raw.split("--BETAVIBE--\n"):
        lines = chunk.strip().splitlines()
        if len(lines) < 3:
            continue
        sha, dt, subject = lines[0], lines[1], lines[2]
        rest = lines[3:]
        files = [x.strip() for x in rest if x.strip() and not x.startswith("    ")]
        body_lines = [x for x in rest if x.startswith("    ")]
        commits.append({"sha": sha, "date": dt, "subject": subject, "body": "\n".join(body_lines), "files": files})
    return commits


def candidate_from_commit(repo: Path, commit: dict) -> dict | None:
    subject = commit["subject"]
    files = commit.get("files", [])
    score = 0
    reasons: list[str] = []
    if SIGNAL_WORDS.search(subject):
        score += 4
        reasons.append("commit message contains failure/fix signal")
    risky = [f for f in files if RISK_PATH.search(f)]
    if risky:
        score += min(4, len(risky))
        reasons.append("touches risky subsystem: " + ", ".join(risky[:4]))
    if subject.lower().startswith("revert"):
        score += 5
        reasons.append("revert / rollback commit")
    if len(files) >= 10:
        score += 2
        reasons.append(f"large change set: {len(files)} files")
    if score < 4:
        return None
    short = commit["sha"][:12]
    title = subject[:90]
    cid = hashlib.sha1((str(repo.resolve()) + commit["sha"]).encode()).hexdigest()[:16]
    tags = infer_tags(subject, files)
    return {
        "id": cid,
        "type": "pitfall" if SIGNAL_WORDS.search(subject) else "spec_guardrail",
        "score": score,
        "title": title,
        "summary": f"Git history candidate from `{repo.name}` commit `{short}`: {subject}",
        "reasons": reasons,
        "tags": tags,
        "tech_stack": infer_tech(files),
        "source": {"kind": "git_commit", "repo": str(repo), "sha": commit["sha"], "date": commit["date"], "files": files[:30]},
        "draft": {
            "symptom": f"Commit message suggests a potential lesson: {subject}",
            "root_cause": "Review the commit diff / PR discussion before promotion.",
            "wrong_paths": "Unknown from git log alone.",
            "fix": f"Inspect with: git show --stat --patch {commit['sha']}",
            "prevention_signal": prevention_signal(subject, risky or files),
            "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
            "evidence": json.dumps({"commit": commit["sha"], "files": files[:20], "reasons": reasons}, ensure_ascii=False, indent=2),
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


def infer_tags(subject: str, files: list[str]) -> list[str]:
    raw = " ".join([subject] + files).lower()
    tags = []
    mapping = {
        "auth": "auth", "oauth": "oauth", "token": "token", "cron": "cron", "launchd": "launchd",
        "workflow": "ci", "github": "github", "migration": "migration", "schema": "schema",
        "docker": "docker", "deploy": "deploy", "test": "test", "flake": "flake",
    }
    for needle, tag in mapping.items():
        if needle in raw and tag not in tags:
            tags.append(tag)
    return tags or ["git-history"]


def infer_tech(files: list[str]) -> list[str]:
    tech = set()
    for f in files:
        if f.endswith((".ts", ".tsx", ".js", ".jsx")):
            tech.add("node")
        if f.endswith(".py"):
            tech.add("python")
        if f.endswith((".go",)):
            tech.add("go")
        if f.endswith((".rs",)):
            tech.add("rust")
        if ".github/workflows" in f:
            tech.add("github-actions")
        if "Dockerfile" in f or "docker" in f.lower():
            tech.add("docker")
    return sorted(tech)


def prevention_signal(subject: str, files: list[str]) -> str:
    focus = files[0] if files else subject
    return f"Before modifying `{focus}` or adjacent subsystem, search this registry and inspect the original fixing commit."


def remote_slug(repo: Path) -> str | None:
    try:
        url = run(["git", "remote", "get-url", "origin"], repo).strip()
    except Exception:
        return None
    if url.startswith("git@"):
        # git@github.com:owner/repo.git
        slug = url.split(":", 1)[-1]
    else:
        parsed = urlparse(url)
        slug = parsed.path.lstrip("/")
    if slug.endswith(".git"):
        slug = slug[:-4]
    return slug if "/" in slug else None


def candidate_from_pr(repo: Path, pr: dict, files: list[str]) -> dict | None:
    title = pr.get("title") or ""
    body = pr.get("body") or ""
    text = f"{title}\n{body}"
    score = 0
    reasons: list[str] = []
    if SIGNAL_WORDS.search(text):
        score += 4
        reasons.append("PR title/body contains failure/fix signal")
    risky = [f for f in files if RISK_PATH.search(f)]
    if risky:
        score += min(4, len(risky))
        reasons.append("PR touches risky subsystem: " + ", ".join(risky[:4]))
    labels = [x.get("name", "") for x in pr.get("labels", [])]
    if any(SIGNAL_WORDS.search(x or "") for x in labels):
        score += 2
        reasons.append("PR labels indicate bug/fix/regression")
    if score < 4:
        return None
    number = pr.get("number")
    cid = hashlib.sha1((str(repo.resolve()) + "pr" + str(number)).encode()).hexdigest()[:16]
    return {
        "id": cid,
        "type": "pitfall" if SIGNAL_WORDS.search(text) else "spec_guardrail",
        "score": score,
        "title": title[:90],
        "summary": f"GitHub PR candidate from `{repo.name}` PR #{number}: {title}",
        "reasons": reasons,
        "tags": infer_tags(text, files),
        "tech_stack": infer_tech(files),
        "source": {"kind": "github_pr", "repo": str(repo), "number": number, "url": pr.get("url"), "merged_at": pr.get("mergedAt"), "files": files[:30]},
        "draft": {
            "symptom": f"PR discussion/title suggests a potential lesson: {title}",
            "root_cause": "Review the PR diff and discussion before promotion.",
            "wrong_paths": "Unknown from PR metadata alone.",
            "fix": f"Inspect with: gh pr view {number} --comments --web",
            "prevention_signal": prevention_signal(title, risky or files),
            "verify_trigger": "When the touched subsystem, framework version, or deployment environment changes.",
            "evidence": json.dumps({"pr": number, "url": pr.get("url"), "labels": labels, "files": files[:20], "reasons": reasons}, ensure_ascii=False, indent=2),
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


def mine_github_prs(repo: Path, limit: int = 50) -> list[dict]:
    slug = remote_slug(repo)
    if not slug:
        return []
    try:
        raw = subprocess.run(
            ["gh", "pr", "list", "--repo", slug, "--state", "all", "--limit", str(limit), "--json", "number,title,body,state,mergedAt,closedAt,url,labels"],
            cwd=repo,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except Exception:
        return []
    prs = json.loads(raw or "[]")
    out: list[dict] = []
    for pr in prs:
        files: list[str] = []
        try:
            raw_files = subprocess.run(
                ["gh", "pr", "view", str(pr["number"]), "--repo", slug, "--json", "files"],
                cwd=repo,
                check=True,
                capture_output=True,
                text=True,
            ).stdout
            files = [f.get("path", "") for f in json.loads(raw_files).get("files", [])]
        except Exception:
            pass
        c = candidate_from_pr(repo, pr, files)
        if c:
            out.append(c)
    return out


def mine_git(repo: Path, since: str | None = None, max_commits: int = 300, with_github: bool = False) -> list[dict]:
    commits = git_log(repo, since=since, max_commits=max_commits)
    candidates = [c for c in (candidate_from_commit(repo, x) for x in commits) if c]
    if with_github:
        candidates.extend(mine_github_prs(repo, limit=min(max_commits, 100)))
    seen = set()
    unique = []
    for c in candidates:
        if c["id"] in seen:
            continue
        seen.add(c["id"])
        unique.append(c)
    unique.sort(key=lambda x: (-x["score"], x["source"].get("date") or x["source"].get("merged_at") or ""))
    return unique
