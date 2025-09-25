"""Ingestion stage.

Validates incoming telemetry and publishes `frk.telemetry.ingested` events.
"""
from typing import Dict

from .events import Event, EventBus
from .storage import append_jsonl
from .config import CFG

REQUIRED_FIELDS = {"deviceId", "patientId", "ts", "accel", "gyro"}


def validate(msg: Dict) -> Dict:
    """Validate a telemetry message for required fields.

    Args:
        msg: Telemetry payload.

    Returns:
        The same payload if valid.

    Raises:
        ValueError: If required fields are missing.
    """
    missing = REQUIRED_FIELDS - set(msg)
    if missing:
        raise ValueError(f"Missing fields: {missing}")
    return msg


def handle_ingest(bus: EventBus):
    """Create an ingestion handler that writes raw and emits an event.

    Args:
        bus: Event bus to publish into.

    Returns:
        A function that ingests validated telemetry and publishes an event.
    """

    def _handler(payload: Dict):
        msg = validate(payload)
        append_jsonl(CFG.raw_dir / "telemetry.jsonl", msg)
        return bus.publish(Event("frk.telemetry.ingested", msg))

    return _handler
