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
