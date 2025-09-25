# Usage

## Setup
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\requirements.txt
```

## Run the pipeline
```powershell
$env:PYTHONPATH = "."
python -m fallrisk_kit.runner
```

## Run the API
```powershell
uvicorn fallrisk_kit.api:app --reload --host 127.0.0.1 --port 8000
```

## Build and serve docs
```powershell
$env:PYTHONPATH = "."; mkdocs serve
# or
mkdocs build
```
