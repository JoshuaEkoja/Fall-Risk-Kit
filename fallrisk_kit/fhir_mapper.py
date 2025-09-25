"""FHIR mapping stage.

Converts risk score events into FHIR R4 Observation and high severity into DetectedIssue.
"""
import json
from pathlib import Path

from .events import Event
from .config import CFG


class FhirMapper:
    """Map risk scores to FHIR resources and write them as JSONL files."""

    def __init__(self):
        self.out_dir: Path = CFG.fhir_dir

    def on_score(self, evt: Event):
        """Handle a risk score event and emit FHIR resources to disk.

        Args:
            evt: The risk score event.
        """
        d = evt.detail
        obs = {
            "resourceType": "Observation",
            "status": "final",
            "category": [{
                "coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "activity"}]
            }],
            "code": {"text": "Fall risk score"},
            "subject": {"reference": f"Patient/{d['patientId']}"},
            "effectiveDateTime": d["ts"],
            "valueQuantity": {"value": d["score"], "unit": "unitless", "system": "http://unitsofmeasure.org"},
            "meta": {"tag": [{"system": "https://fallriskkit.org/tags", "code": "frk"}]}
        }
        self._write_jsonl(self.out_dir / "Observation.jsonl", obs)

        if d["severity"] == "high":
            issue = {
                "resourceType": "DetectedIssue",
                "status": "final",
                "code": {"text": "High fall risk"},
                "severity": "high",
                "patient": {"reference": f"Patient/{d['patientId']}"},
                "identifiedDateTime": d["ts"],
                "detail": f"High fall risk detected by {d['model']} (score={d['score']:.2f})"
            }
            self._write_jsonl(self.out_dir / "DetectedIssue.jsonl", issue)

    def _write_jsonl(self, path: Path, obj):
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(obj) + "\n")
