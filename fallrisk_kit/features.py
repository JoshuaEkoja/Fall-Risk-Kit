"""Feature extraction with fixed-size windowing.

Collects per-device windows and computes simple statistical features.
"""
from collections import defaultdict, deque
from typing import Deque, Dict, List

import numpy as np

from .events import Event
from .config import CFG
from .storage import append_jsonl


class FeatureExtractor:
    """Windowing and feature extraction.

    Attributes:
        window_len: Number of samples in each fixed-size window.
        buffers: Per-device ring buffers for telemetry.
    """

    def __init__(self, sample_rate_hz: int = CFG.sample_rate_hz, window_seconds: int = CFG.window_seconds):
        self.window_len = sample_rate_hz * window_seconds
        self.buffers: Dict[str, Deque[Dict]] = defaultdict(lambda: deque(maxlen=self.window_len))

    def on_telemetry(self, evt: Event):
        """Process a telemetry event and emit features when window completes.

        Args:
            evt: A `frk.telemetry.ingested` event.

        Returns:
            An Event("features.windowed.ready", ...) when the window fills; otherwise None.
        """
        d = evt.detail
        key = d["deviceId"]
        buf = self.buffers[key]
        buf.append(d)
        if len(buf) == self.window_len:
            feats = self._compute(list(buf))
            out = {
                "eventType": "features.windowed.ready",
                "deviceId": d["deviceId"],
                "patientId": d["patientId"],
                "window": {"size": self.window_len},
                "features": feats,
                "ts": d["ts"],
            }
            append_jsonl(CFG.curated_features_dir / "features.jsonl", out)
            return Event("features.windowed.ready", out)
        return None

    def _compute(self, window: List[Dict]):
        """Compute simple features over a completed window.

        Args:
            window: List of telemetry samples.

        Returns:
            Mapping of feature names to values.
        """
        ax = np.array([x["accel"]["x"] for x in window])
        ay = np.array([x["accel"]["y"] for x in window])
        az = np.array([x["accel"]["z"] for x in window])
        gz = np.array([x["gyro"]["z"] for x in window])
        return {
            "accel_mean": [float(ax.mean()), float(ay.mean()), float(az.mean())],
            "accel_std": [float(ax.std()), float(ay.std()), float(az.std())],
            "gyro_energy_z": float(np.sum(np.abs(gz))),
        }
