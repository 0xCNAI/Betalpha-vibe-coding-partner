from __future__ import annotations

from collections import Counter
from datetime import date
import math
import re
from .models import Insight

TOKEN_RE = re.compile(r"[a-zA-Z0-9_./:-]+|[\u4e00-\u9fff]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "") if len(t.strip()) > 1]


def insight_text(i: Insight) -> str:
    return "\n".join([
        i.title,
        i.summary,
        i.prevention_signal,
        " ".join(i.tags),
        " ".join(i.tech_stack),
        "\n".join(i.body.values()),
    ])


def search_insights(insights: list[Insight], query: str, limit: int = 8) -> list[tuple[float, Insight, list[str]]]:
    q_tokens = tokenize(query)
    if not q_tokens:
        return []
    docs = [tokenize(insight_text(i)) for i in insights]
    df = Counter(tok for doc in docs for tok in set(doc))
    n = max(len(docs), 1)
    scored = []
    for insight, doc in zip(insights, docs):
        tf = Counter(doc)
        matched: list[str] = []
        score = 0.0
        fields_boost = tokenize(" ".join([insight.title, insight.summary, insight.prevention_signal, " ".join(insight.tags), " ".join(insight.tech_stack)]))
        field_tf = Counter(fields_boost)
        for tok in q_tokens:
            if tf[tok] or any(tok in d or d in tok for d in set(doc)):
                matched.append(tok)
                idf = math.log((n + 1) / (df.get(tok, 0) + 1)) + 1
                score += (tf[tok] + 2 * field_tf[tok]) * idf
                # partial token fallback for compound terms like line-bot vs line bot
                if tf[tok] == 0:
                    score += 0.4
        if score:
            # favor fresh insights slightly
            try:
                age = (date.today() - date.fromisoformat(insight.last_verified_at)).days
                score *= max(0.65, 1 - age / 1000)
            except Exception:
                pass
            scored.append((score, insight, matched))
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:limit]
