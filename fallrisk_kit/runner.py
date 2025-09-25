"""Pipeline orchestrator.

Wires together stages using the in-process event bus and consumes a queue
of incoming telemetry (from the simulator or other producers).
"""
import asyncio
from typing import Dict

from .events import EventBus, Event
from .ingestion import handle_ingest
from .features import FeatureExtractor
from .risk import RiskScorer
from .alerts import Alerting
from .fhir_mapper import FhirMapper
from .storage import init_sqlite


async def main(event_source: "asyncio.Queue[Dict]"):
    """Run the pipeline, consuming telemetry from an asyncio queue.

    Args:
        event_source: A queue of telemetry payloads to ingest.
    """
    init_sqlite()
    bus = EventBus()

    # Wire pipeline
    ingest = handle_ingest(bus)
    feats = FeatureExtractor()
    risk = RiskScorer()
    alerts = Alerting()
    fhir = FhirMapper()

    bus.subscribe("frk.telemetry.ingested", lambda e: (evt := feats.on_telemetry(e)) and bus.publish(evt))
    bus.subscribe("features.windowed.ready", lambda e: bus.publish(risk.on_features(e)))
    bus.subscribe("frk.risk.score.computed", alerts.on_score)
    bus.subscribe("frk.risk.score.computed", fhir.on_score)

    # run bus in background
    bus_task = asyncio.create_task(bus.run())

    # pump events from the external queue into ingestion
    async def pump():
        while True:
            payload = await event_source.get()
            res = ingest(payload)
            if asyncio.iscoroutine(res):
                await res
            event_source.task_done()

    pump_task = asyncio.create_task(pump())
    await asyncio.gather(bus_task, pump_task)


if __name__ == "__main__":
    q: "asyncio.Queue[Dict]" = asyncio.Queue()
    asyncio.run(main(q))
