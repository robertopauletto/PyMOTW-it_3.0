# asyncio_coroutine.py

import asyncio


async def coroutine():
    print('nella coroutine')


event_loop = asyncio.get_event_loop()
try:
    print('coroutine in partenza')
    coro = coroutine()
    print('entrata nel ciclo di eventi')
    event_loop.run_until_complete(coro)
finally:
    print('chiusura del ciclo di eventi')
    event_loop.close()
