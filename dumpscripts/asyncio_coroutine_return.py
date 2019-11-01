# asyncio_coroutine_return.py

import asyncio


async def coroutine():
    print('nella coroutine')
    return 'risultato'


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(
        coroutine()
    )
    print('ritornato: {!r}'.format(return_value))
finally:
    event_loop.close()
