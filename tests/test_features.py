from fallrisk_kit.features import FeatureExtractor
from fallrisk_kit.events import Event


def test_feature_windowing():
    fx = FeatureExtractor(sample_rate_hz=2, window_seconds=2)  # 4 samples
    produced = []
    # push 4 telemetry points
    for i in range(4):
        evt = Event("frk.telemetry.ingested", {
            "deviceId": "d1", "patientId": "p1", "ts": f"2025-09-25T00:00:0{i}Z",
            "accel": {"x": 0.0, "y": 0.0, "z": 1.0},
            "gyro": {"x": 0.0, "y": 0.0, "z": 0.5}
        })
        out = fx.on_telemetry(evt)
        if out:
            produced.append(out)
    assert len(produced) == 1
    assert produced[0].detail["features"]["gyro_energy_z"] > 0
