$env:PYTHONPATH = "."
uvicorn fallrisk_kit.api:app --reload --host 127.0.0.1 --port 8000
