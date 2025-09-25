"""FallRisk Kit local package.

Provides an event-driven pipeline for simulated fall-risk monitoring:
- events: in-process event bus
- ingestion: telemetry validation and event publishing
- features: windowing and feature extraction
- risk: baseline risk scoring
- alerts: alert routing and persistence
- fhir_mapper: FHIR Observation/DetectedIssue generation
- api: FastAPI app for inspection
- runner: orchestrator wiring
"""

__all__ = [
    "config",
    "events",
    "storage",
    "ingestion",
    "features",
    "risk",
    "alerts",
    "fhir_mapper",
    "api",
    "runner",
]
