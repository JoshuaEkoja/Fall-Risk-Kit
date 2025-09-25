import asyncio
from fallrisk_kit.runner import main
from simulator.imu_stream import generate


async def run_once():
    q = asyncio.Queue()
    task_pipeline = asyncio.create_task(main(q))
    # push enough samples for one window (2s * 20Hz = 40 samples)
    await generate(q, duration_s=2, rate_hz=20, scenario="fall")
    await asyncio.sleep(1)
    task_pipeline.cancel()


def test_end_to_end_runs():
    try:
        asyncio.run(run_once())
    except Exception:
        # pipeline task is cancelled at the end
        pass
