$env:PYTHONPATH = "."
python - << 'PY'
import asyncio
from simulator.imu_stream import run_simulation

async def go():
    q = asyncio.Queue()
    await run_simulation(q, scenario="fall")

asyncio.run(go())
PY
