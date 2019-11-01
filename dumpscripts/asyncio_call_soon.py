# asyncio_call_soon.py

import asyncio
import functools


def callback(arg, *, kwarg='default'):
    print('callback chiamato con {} e {}'.format(arg, kwarg))


async def main(loop):
    print('registrazione callbacks')
    loop.call_soon(callback, 1)
    wrapped = functools.partial(callback, kwarg='non default')
    loop.call_soon(wrapped, 2)

    await asyncio.sleep(0.1)


event_loop = asyncio.get_event_loop()
try:
    print('entrata nel ciclo di eventi')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('chiusura del ciclo di eventi')
    event_loop.close()
