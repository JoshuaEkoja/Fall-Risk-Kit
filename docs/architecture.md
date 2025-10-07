# Architecture

This project simulates an AWS-native, event-driven pipeline locally using `asyncio`:

- `events.py`: in-process event bus (simulates EventBridge)
- `ingestion.py`: validates telemetry and emits `frk.telemetry.ingested`
- `features.py`: fixed-size windowing and feature extraction
- `risk.py`: baseline anomaly/risk scoring
- `alerts.py`: alert routing and persistence to SQLite
- `fhir_mapper.py`: maps risk events to FHIR Observation/DetectedIssue
- `api.py`: FastAPI for simple inspection (health, latest risk, alerts)
- `runner.py`: orchestrator wiring the pipeline
- `simulator/imu_stream.py`: synthetic IMU telemetry generator


## Stacks mapping (AWS → Local)

See Stacks for the full list and assessment: [docs/stacks.md](stacks.md).

At a glance:
- Event bus → fallrisk_kit.events (EventBridge analogue)
- Ingestion → fallrisk_kit.ingestion (IoT rules → event fan-out)
- Stream processing → fallrisk_kit.features, fallrisk_kit.risk
- Data lake zones → data/raw, data/curated/*
- FHIR mapping → fallrisk_kit.fhir_mapper
- API/interop → fallrisk_kit.api
- Alerts/notifications → fallrisk_kit.alerts (SQLite + files)
