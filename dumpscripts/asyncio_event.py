# asyncio_event.py

import asyncio
import functools


def set_event(event):
    print('impostazione evento in callback')
    event.set()


async def coro1(event):
    print('coro1 in attesa dell\'evento')
    await event.wait()
    print('coro1 attivato')


async def coro2(event):
    print('coro2 in attesa dell\'evento')
    await event.wait()
    print('coro2 attivato')


async def main(loop):
    # Crea un evento condiviso
    event = asyncio.Event()
    print('stato di partenza evento: {}'.format(event.is_set()))

    loop.call_later(
        0.1, functools.partial(set_event, event)
    )

    await asyncio.wait([coro1(event), coro2(event)])
    print('stato di fine evento: {}'.format(event.is_set()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
