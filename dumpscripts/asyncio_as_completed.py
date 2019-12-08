# asyncio_as_completed.py

import asyncio


async def phase(i):
    print('in fase {}'.format(i))
    await asyncio.sleep(0.5 - (0.1 * i))
    print('fase {} terminata'.format(i))
    return 'risultato {} fase'.format(i)


async def main(num_phases):
    print('in partenza main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('in attesa del completamento delle fasi')
    results = []
    for next_to_complete in asyncio.as_completed(phases):
        answer = await next_to_complete
        print('risposta ricevuta {!r}'.format(answer))
        results.append(answer)
    print('resultati: {!r}'.format(results))
    return results


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
