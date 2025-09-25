"""Project configuration and paths.

Defines sampling/windowing parameters, storage directories, and alert thresholds.
"""
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    """Runtime configuration for the local pipeline.

    Attributes:
        sample_rate_hz: Telemetry sampling rate in Hertz.
        window_seconds: Number of seconds per feature window.
        base_dir: Base data directory.
        raw_dir: Directory for raw telemetry archives (JSONL).
        curated_features_dir: Directory for feature windows.
        curated_risk_dir: Directory for risk outputs.
        fhir_dir: Directory for FHIR resources.
        sqlite_path: SQLite database file path.
        medium_threshold: Threshold for medium severity risk.
        high_threshold: Threshold for high severity risk.
    """

    sample_rate_hz: int = 20
    window_seconds: int = 10

    base_dir: Path = Path(__file__).resolve().parents[1] / "data"
    raw_dir: Path = base_dir / "raw"
    curated_features_dir: Path = base_dir / "curated" / "features"
    curated_risk_dir: Path = base_dir / "curated" / "risk"
    fhir_dir: Path = base_dir / "curated" / "fhir"

    sqlite_path: Path = base_dir / "frk.db"

    medium_threshold: float = 0.5
    high_threshold: float = 0.8


CFG = Config()
for p in [CFG.raw_dir, CFG.curated_features_dir, CFG.curated_risk_dir, CFG.fhir_dir]:
    p.mkdir(parents=True, exist_ok=True)
