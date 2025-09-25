"""Synthetic IMU telemetry generator for the local pipeline.

Produces randomized accelerometer/gyroscope samples at a given rate. A "fall"
scenario injects bursts on gyro Z to trigger high risk scores in the demo.
"""
import asyncio
import random
from datetime import datetime, timedelta
from typing import Dict

from fallrisk_kit.config import CFG


async def generate(
    q: "asyncio.Queue[Dict]",
    device_id: str = "imu-12345",
    patient_id: str = "pt-42",
    duration_s: int = 30,
    rate_hz: int = CFG.sample_rate_hz,
    scenario: str = "normal",
):
    """Push telemetry samples into a queue for a duration.

    Args:
        q: Target queue consumed by the pipeline.
        device_id: IMU device identifier.
        patient_id: Logical patient identifier.
        duration_s: Duration to stream in seconds.
        rate_hz: Sampling rate.
        scenario: One of {"normal", "walk", "fall"}.
    """
    interval = 1.0 / rate_hz
    end = datetime.utcnow() + timedelta(seconds=duration_s)
    while datetime.utcnow() < end:
        base_accel = {
            "x": random.uniform(-0.05, 0.05),
            "y": random.uniform(-0.05, 0.05),
            "z": random.uniform(0.9, 1.1),
        }
        base_gyro = {
            "x": random.uniform(-0.1, 0.1),
            "y": random.uniform(-0.1, 0.1),
            "z": random.uniform(-0.1, 0.1),
        }
        if scenario == "fall":
            base_gyro["z"] += random.uniform(3.0, 6.0)
        elif scenario == "walk":
            base_gyro["z"] += random.uniform(0.5, 1.5)

        msg = {
            "eventType": "sim.telemetry",
            "deviceId": device_id,
            "patientId": patient_id,
            "ts": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "accel": base_accel,
            "gyro": base_gyro,
            "meta": {"fw": "1.0.0", "battery": random.uniform(0.2, 1.0)},
        }
        await q.put(msg)
        await asyncio.sleep(interval)


async def run_simulation(q, scenario: str = "fall"):
    """Run a single simulation scenario into the queue."""
    await generate(q, scenario=scenario)


if __name__ == "__main__":
    asyncio.run(run_simulation(asyncio.Queue()))
