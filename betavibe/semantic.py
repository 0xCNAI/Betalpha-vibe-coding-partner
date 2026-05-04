from __future__ import annotations

from pathlib import Path
import sqlite3
import struct

from .models import Insight

MODEL_DIR = Path(__file__).resolve().parents[1] / "models" / "minilm-l6-v2"

_SESSION = None
_TOKENIZER = None


def model_size_bytes() -> int:
    if not MODEL_DIR.exists():
        return 0
    return sum(path.stat().st_size for path in MODEL_DIR.iterdir() if path.is_file())


def model_available() -> bool:
    return (MODEL_DIR / "model.int8.onnx").exists() and (MODEL_DIR / "tokenizer.json").exists()


def _load_model():
    global _SESSION, _TOKENIZER
    if _SESSION is None or _TOKENIZER is None:
        import onnxruntime as ort
        from tokenizers import Tokenizer

        _TOKENIZER = Tokenizer.from_file(str(MODEL_DIR / "tokenizer.json"))
        _SESSION = ort.InferenceSession(str(MODEL_DIR / "model.int8.onnx"), providers=["CPUExecutionProvider"])
    return _SESSION, _TOKENIZER


def embed_text(text: str) -> list[float]:
    import numpy as np

    session, tokenizer = _load_model()
    enc = tokenizer.encode(text or "")
    feeds = {
        "input_ids": np.array([enc.ids], dtype=np.int64),
        "attention_mask": np.array([enc.attention_mask], dtype=np.int64),
        "token_type_ids": np.array([enc.type_ids], dtype=np.int64),
    }
    inputs = {item.name for item in session.get_inputs()}
    output = session.run(None, {name: feeds[name] for name in inputs})[0]
    mask = feeds["attention_mask"]
    pooled = (output * mask[:, :, None]).sum(axis=1) / np.maximum(mask.sum(axis=1, keepdims=True), 1)
    norm = np.linalg.norm(pooled, axis=1, keepdims=True)
    pooled = pooled / np.maximum(norm, 1e-12)
    return pooled[0].astype("float32").tolist()


def _pack(values: list[float]) -> bytes:
    return struct.pack(f"{len(values)}f", *values)


def _unpack(blob: bytes) -> list[float]:
    return list(struct.unpack(f"{len(blob) // 4}f", blob))


def embeddings_path(registry: Path) -> Path:
    return registry / "insights" / "embeddings.sqlite"


def init_embeddings(registry: Path) -> Path:
    path = embeddings_path(registry)
    path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(path) as db:
        db.execute(
            "CREATE TABLE IF NOT EXISTS embeddings (slug TEXT PRIMARY KEY, path TEXT NOT NULL, title TEXT NOT NULL, tags TEXT NOT NULL, tech_stack TEXT NOT NULL, pattern TEXT NOT NULL, embedding BLOB NOT NULL)"
        )
    return path


def index_insight(registry: Path, insight: Insight) -> None:
    if not model_available():
        return
    path = init_embeddings(registry)
    pattern = insight.transferable_pattern or insight.prevention_signal
    emb = _pack(embed_text(pattern))
    with sqlite3.connect(path) as db:
        db.execute(
            "INSERT OR REPLACE INTO embeddings (slug, path, title, tags, tech_stack, pattern, embedding) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                insight.slug,
                str(insight.path or ""),
                insight.title,
                ",".join(insight.tags),
                ",".join(insight.tech_stack),
                pattern,
                emb,
            ),
        )


def rebuild_embeddings(registry: Path, insights: list[Insight]) -> Path:
    path = init_embeddings(registry)
    with sqlite3.connect(path) as db:
        db.execute("DELETE FROM embeddings")
    for insight in insights:
        index_insight(registry, insight)
    return path


def cosine(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    import numpy as np

    return float(np.dot(np.array(left, dtype=np.float32), np.array(right, dtype=np.float32)))


def semantic_scores(registry: Path, query: str) -> dict[str, float]:
    path = embeddings_path(registry)
    if not model_available() or not path.exists():
        return {}
    query_embedding = embed_text(query)
    scores: dict[str, float] = {}
    with sqlite3.connect(path) as db:
        for slug, blob in db.execute("SELECT slug, embedding FROM embeddings"):
            scores[slug] = cosine(query_embedding, _unpack(blob))
    return scores
