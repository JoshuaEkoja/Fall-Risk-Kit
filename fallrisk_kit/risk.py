"""Baseline risk scoring.

Implements a simple heuristic risk model using gyro energy.
"""
from .events import Event
from .config import CFG
from .storage import append_jsonl, insert_risk_row


class RiskScorer:
    """Compute risk score from feature windows.

    Attributes:
        medium: Threshold for medium severity.
        high: Threshold for high severity.
    """

    def __init__(self, medium: float = CFG.medium_threshold, high: float = CFG.high_threshold):
        self.medium = medium
        self.high = high

    def on_features(self, evt: Event):
        """Handle a features.windowed.ready event and emit a risk score event.

        Args:
            evt: The feature-ready event.

        Returns:
            Event("frk.risk.score.computed", ...)
        """
        d = evt.detail
        energy = float(d["features"]["gyro_energy_z"])  # simple heuristic
        score = min(1.0, energy / 100.0)
        severity = "high" if score >= self.high else "medium" if score >= self.medium else "low"
        out = {
            "eventType": "frk.risk.score.computed",
            "deviceId": d["deviceId"],
            "patientId": d["patientId"],
            "ts": d["ts"],
            "model": "rcf-baseline-sim",
            "score": score,
            "severity": severity,
        }
        append_jsonl(CFG.curated_risk_dir / "risk.jsonl", out)
        insert_risk_row({
            "device_id": out["deviceId"],
            "patient_id": out["patientId"],
            "ts": out["ts"],
            "model": out["model"],
            "score": out["score"],
            "severity": out["severity"],
        })
        return Event("frk.risk.score.computed", out)
