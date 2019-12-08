# asyncio_wait_timeout.py

import asyncio


async def phase(i):
    print('nella fase {}'.format(i))
    try:
        await asyncio.sleep(0.1 * i)
    except asyncio.CancelledError:
        print('fase {} cancellata'.format(i))
        raise
    else:
        print('fase {} completata'.format(i))
        return 'risultato {} di fase'.format(i)


async def main(num_phases):
    print('in partenza main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('si attende 0.1 per il completamento delle fasi')
    completed, pending = await asyncio.wait(phases, timeout=0.1)
    print('{} completate e {} pendenti'.format(
        len(completed), len(pending),
    ))
    # Si eliminano le attività rimanenti in modoe che non  generino errori
    # quando si esce senza completarle
    if pending:
        print('eliminazione dei tasks')
        for t in pending:
            t.cancel()
    print('in uscita da main')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()
