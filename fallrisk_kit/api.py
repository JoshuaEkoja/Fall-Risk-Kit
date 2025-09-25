"""Minimal FastAPI API for inspection.

Exposes health, latest risk scores, and alerts endpoints backed by SQLite.
"""
from fastapi import FastAPI
from sqlalchemy import create_engine, text

from .config import CFG

app = FastAPI(title="FallRiskKit (Local)")
_engine = create_engine(f"sqlite:///{CFG.sqlite_path}")


@app.get("/health")
def health():
    """Simple health endpoint."""
    return {"status": "ok"}


@app.get("/risk/latest")
def latest_risk(limit: int = 10):
    """Return latest risk scores from SQLite.

    Args:
        limit: Number of rows to return (default 10).
    """
    with _engine.begin() as conn:
        rows = conn.execute(text("SELECT * FROM risk_scores ORDER BY id DESC LIMIT :lim"), {"lim": limit}).mappings().all()
    return {"items": [dict(r) for r in rows]}


@app.get("/alerts")
def alerts(limit: int = 10):
    """Return recent alerts from SQLite.

    Args:
        limit: Number of rows to return (default 10).
    """
    with _engine.begin() as conn:
        rows = conn.execute(text("SELECT * FROM alerts ORDER BY id DESC LIMIT :lim"), {"lim": limit}).mappings().all()
    return {"items": [dict(r) for r in rows]}
