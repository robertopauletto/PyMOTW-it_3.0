# asyncio_gather.py

import asyncio


async def phase1():
    print('in phase1')
    await asyncio.sleep(2)
    print('terminata phase1')
    return 'risultato di phase1'


async def phase2():
    print('in phase2')
    await asyncio.sleep(1)
    print('terminata phase2')
    return 'risultato di phase2'


async def main():
    print('in partenza main')
    print('in attesa del completamento delle fasi')
    results = await asyncio.gather(
        phase1(),
        phase2(),
    )
    print('results: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main())
finally:
    event_loop.close()
