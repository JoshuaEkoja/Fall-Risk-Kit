# FallRisk Kit (Local)

An event-driven, local Python simulation of a fall-risk monitoring pipeline. This repository mirrors an AWS-native design but runs entirely on your machine with Python and asyncio.

What’s included:
- In-process event bus (simulates EventBridge)
- Pipeline: ingestion → features → risk scoring → alerts → FHIR mapping
- Local storage: JSONL files and SQLite
- Minimal FastAPI API for inspection
- Simulator that generates synthetic IMU telemetry
- Tests (pytest)
- MkDocs documentation (Material theme) with auto-generated API reference

Quickstart (Windows PowerShell):
1) Create venv and install deps
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt
```

2) Run pipeline + simulator (separate shells or use the helper script)
```powershell
$env:PYTHONPATH = "."
python -m fallrisk_kit.runner
```

3) Run API
```powershell
uvicorn fallrisk_kit.api:app --reload --host 127.0.0.1 --port 8000
```

4) Docs (MkDocs)
```powershell
$env:PYTHONPATH = "."; mkdocs serve
# or
mkdocs build
```

5) Tests
```powershell
pytest -q
```

See docs/architecture.md and docs/usage.md for details.
