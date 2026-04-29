from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import re
import subprocess

from .gitmine import git_log, infer_tags, infer_tech

FIX_RE = re.compile(r"\b(fix|fixed|hotfix|bug|regression|broken|fail|failure|permission-denied|timeout|crash|rollback|revert|build blockers?)\b", re.I)
TOPIC_RE = re.compile(r"(auth|login|firebase|firestore|rules|functions?|typescript|build|schema|migration|receive|picker|picking|hq|home|hooks?|maestro|test|android|expo|batch|catalog|supplement|delivery|replenishment|submodule|gateway|sessions?|browser|mcp|discord|telegram|cron|memory|agent|resolver|runtime|gbrain|registry|cli|api|config|oauth|webhook|database|cache|sync|deploy|worker|queue|mobile|ios|electron|vite|react)", re.I)


def run_git(repo: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=False)


def _normalize_topic(value: str) -> str:
    value = re.sub(r"[^a-z0-9_.-]+", "-", value.lower()).strip("-_")
    aliases = {"session": "sessions", "function": "functions", "hook": "hooks", "rule": "rules"}
    return aliases.get(value.rstrip("s"), value.rstrip("s")) or "general"


def _path_topics(files: list[str]) -> list[str]:
    hits: list[str] = []
    skip = {"src", "lib", "app", "packages", "apps", "scripts", "tests", "test", "dist", "build"}
    for path in files:
        parts = [p for p in Path(path).parts if p not in skip and not p.startswith(".")]
        candidates = []
        if parts:
            candidates.append(parts[0])
        if len(parts) > 1:
            candidates.append(f"{parts[0]}/{Path(parts[-1]).stem}" if parts[0] in {"skills", "agents", "packages", "apps"} else Path(parts[-1]).stem)
        for c in candidates:
            topic = _normalize_topic(c)
            if len(topic) >= 3 and topic not in hits:
                hits.append(topic)
    return hits


def _topic(commit: dict) -> str:
    files = commit.get("files", [])
    text = " ".join([commit.get("subject", ""), commit.get("body", ""), *files]).lower()
    hits = []
    for match in TOPIC_RE.finditer(text):
        value = _normalize_topic(match.group(1))
        if value not in hits:
            hits.append(value)
    for value in _path_topics(files):
        if value not in hits:
            hits.append(value)
    return "+".join(hits[:3]) or "general"


def _subject_summary(subjects: list[str]) -> str:
    for subject in subjects:
        if FIX_RE.search(subject):
            return subject
    return subjects[0] if subjects else "Untitled cluster"


def _patch_excerpt(repo: Path, sha: str, max_chars: int = 1800) -> str:
    proc = run_git(repo, ["show", "--stat", "--patch", "--find-renames", "--format=medium", sha])
    if proc.returncode != 0:
        return ""
    text = proc.stdout.strip()
    return text[:max_chars]


def excavate(repo: Path, max_commits: int = 200, cluster_window: int = 4, limit: int = 20, include_patch: bool = True) -> list[dict]:
    commits = git_log(repo, max_commits=max_commits)
    clusters: dict[str, list[dict]] = defaultdict(list)
    for index, commit in enumerate(commits):
        if not FIX_RE.search(commit.get("subject", "") + "\n" + commit.get("body", "")):
            continue
        topic = _topic(commit)
        # Include adjacent older commits as context. git log is newest-first, so
        # indexes after the fix commit are the work that immediately preceded it.
        context = commits[index : min(len(commits), index + cluster_window)]
        key = f"{topic}:{commit['sha'][:12]}"
        clusters[key] = context

    findings = []
    for key, group in clusters.items():
        fix = group[0]
        subjects = [c.get("subject", "") for c in group]
        files = []
        for c in group:
            for f in c.get("files", []):
                if f not in files:
                    files.append(f)
        title = _subject_summary(subjects)[:100]
        topic = key.split(":", 1)[0]
        score = 4 + min(3, len(group) - 1) + min(3, len(files) // 8)
        if any("test" in s.lower() or "maestro" in s.lower() for s in subjects):
            score += 1
        fid = hashlib.sha1((str(repo.resolve()) + key).encode()).hexdigest()[:16]
        evidence = {
            "fix_commit": fix["sha"],
            "context_commits": [c["sha"] for c in group[1:]],
            "subjects": subjects,
            "files": files[:40],
            "patch_excerpt": _patch_excerpt(repo, fix["sha"]) if include_patch else "",
        }
        findings.append({
            "id": fid,
            "type": "pitfall",
            "confidence": "medium" if include_patch else "low",
            "score": score,
            "topic": topic,
            "title": title,
            "summary": f"Forensic cluster from `{repo.name}` around fix commit `{fix['sha'][:12]}`: {title}",
            "tags": infer_tags(" ".join(subjects), files),
            "tech_stack": infer_tech(files),
            "source": {"kind": "forensic_git_cluster", "repo": str(repo), "sha": fix["sha"], "date": fix.get("date"), "files": files[:40]},
            "draft": {
                "symptom": f"History shows a fix/regression cluster: {title}",
                "root_cause": "Inferred from git history only. Confirm against patch/test evidence before promotion.",
                "wrong_paths": "Unknown unless adjacent commits or session logs show failed attempts.",
                "fix": f"Inspect fix commit: git show --stat --patch {fix['sha']}",
                "prevention_signal": f"Before touching `{files[0] if files else topic}` or related `{topic}` code, inspect this cluster and run the verification commands tied to it.",
                "verify_trigger": "When the same files/subsystem, framework version, auth/rules/build config, or deployment environment changes.",
                "evidence": evidence,
            },
            "created_at": datetime.now(timezone.utc).isoformat(),
        })
    findings.sort(key=lambda x: (-x["score"], x["title"]))
    return findings[:limit]


def write_report(findings: list[dict], out: Path, repo: Path) -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Betavibe Forensic Excavation Report",
        "",
        f"- repo: `{repo}`",
        f"- findings: {len(findings)}",
        "- mode: git forensic clusters; no network required",
        "",
        "## Findings",
        "",
    ]
    if not findings:
        lines.append("No fix/regression clusters found. Try increasing `--max-commits` or adding PR/CI/session sources later.")
    for i, f in enumerate(findings, 1):
        ev = f.get("draft", {}).get("evidence", {})
        lines.extend([
            f"### {i}. {f['title']}",
            "",
            f"- id: `{f['id']}`",
            f"- score: {f['score']}",
            f"- confidence: {f['confidence']}",
            f"- topic: `{f['topic']}`",
            f"- fix_commit: `{ev.get('fix_commit', '')[:12]}`",
            f"- context_commits: {', '.join(x[:12] for x in ev.get('context_commits', [])) or 'none'}",
            f"- tags: {', '.join(f.get('tags', []))}",
            f"- files: {', '.join(ev.get('files', [])[:8])}",
            "",
            f"**Draft symptom**: {f['draft']['symptom']}",
            "",
            f"**Prevention signal**: {f['draft']['prevention_signal']}",
            "",
        ])
    out.write_text("\n".join(lines), encoding="utf-8")
    return out
