# asyncio_call_at.py

import asyncio
import time


def callback(n, loop):
    print('callback {} chiamato a {}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('orario dell\'orologio: {}'.format(time.time()))
    print('orario del ciclo: {}'.format(now))

    print('registrazione dei callback')
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('entrata nel ciclo di eventi')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('chiusura del ciclo di eventi')
    event_loop.close()
