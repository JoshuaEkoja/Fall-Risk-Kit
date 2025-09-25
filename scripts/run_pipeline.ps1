$env:PYTHONPATH = "."
python - << 'PY'
import asyncio
from fallrisk_kit.runner import main
from simulator.imu_stream import run_simulation

async def go():
    q = asyncio.Queue()
    # start simulator in the background
    async def sim():
        await run_simulation(q, scenario="fall")
    asyncio.create_task(sim())
    await main(q)

try:
    asyncio.run(go())
except KeyboardInterrupt:
    pass
PY
