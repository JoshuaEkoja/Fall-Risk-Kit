from fallrisk_kit.risk import RiskScorer
from fallrisk_kit.events import Event


def test_risk_severity_thresholds():
    rs = RiskScorer(medium=0.5, high=0.8)
    evt = Event("features.windowed.ready", {"deviceId":"d","patientId":"p","ts":"t","features": {"gyro_energy_z": 200}})
    out = rs.on_features(evt)
    assert out.detail["severity"] == "high"
