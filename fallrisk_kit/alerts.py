"""Alerting stage.

Writes alerts to SQLite and prints them to stdout for demo purposes.
"""
from .events import Event
from .config import CFG
from .storage import insert_alert


class Alerting:
    """Alert decisioning for risk score events."""

    def on_score(self, evt: Event):
        """Handle a risk score event and persist an alert if needed.

        Args:
            evt: The risk score event.
        """
        d = evt.detail
        sev = d["severity"]
        if sev in ("medium", "high"):
            msg = f"Fall risk {sev} detected (score={d['score']:.2f})"
            row = {
                "patient_id": d["patientId"],
                "ts": d["ts"],
                "risk_score": d["score"],
                "severity": sev,
                "message": msg,
            }
            insert_alert(row)
            print("ALERT:", msg)
