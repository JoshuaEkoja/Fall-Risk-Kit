"""Local storage utilities.

Provides helpers for JSONL archival and SQLite persistence.
"""
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable

from sqlalchemy import create_engine, text

from .config import CFG

_engine = create_engine(f"sqlite:///{CFG.sqlite_path}")


def append_jsonl(path: Path, obj: Dict):
    """Append a single JSON object as a line to a JSONL file.

    Args:
        path: Destination file path.
        obj: JSON-serializable object.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj) + "\n")


def now_iso() -> str:
    """Return current UTC time in ISO 8601 format with seconds precision."""
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def init_sqlite():
    """Initialize SQLite tables if they do not exist."""
    with _engine.begin() as conn:
        conn.execute(text(
            """
            CREATE TABLE IF NOT EXISTS risk_scores (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              device_id TEXT,
              patient_id TEXT,
              ts TEXT,
              model TEXT,
              score REAL,
              severity TEXT
            );
            """
        ))
        conn.execute(text(
            """
            CREATE TABLE IF NOT EXISTS alerts (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              patient_id TEXT,
              ts TEXT,
              risk_score REAL,
              severity TEXT,
              message TEXT
            );
            """
        ))


def insert_risk_row(row: Dict):
    """Insert a risk score record into SQLite.

    Args:
        row: Mapping with device_id, patient_id, ts, model, score, severity.
    """
    with _engine.begin() as conn:
        conn.execute(text(
            "INSERT INTO risk_scores (device_id, patient_id, ts, model, score, severity) VALUES (:device_id, :patient_id, :ts, :model, :score, :severity)"
        ), row)


def insert_alert(row: Dict):
    """Insert an alert record into SQLite.

    Args:
        row: Mapping with patient_id, ts, risk_score, severity, message.
    """
    with _engine.begin() as conn:
        conn.execute(text(
            "INSERT INTO alerts (patient_id, ts, risk_score, severity, message) VALUES (:patient_id, :ts, :risk_score, :severity, :message)"
        ), row)


def dump_many_jsonl(path: Path, rows: Iterable[Dict]):
    """Append many objects to a JSONL file.

    Args:
        path: Destination JSONL file.
        rows: Iterable of JSON-serializable objects.
    """
    for r in rows:
        append_jsonl(path, r)
