# asyncio_wait.py

import asyncio


async def phase(i):
    print('nella fase {}'.format(i))
    await asyncio.sleep(0.1 * i)
    print('completato per phase {}'.format(i))
    return 'fase risulta {}'.format(i)


async def main(num_phases):
    print('partenza di main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('in attesa di completamento fasi')
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print('resultati: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
