# asyncio_ensure_future.py

import asyncio


async def wrapped():
    print('impacchetato')
    return 'risultato'


async def inner(task):
    print('inner: in partenza')
    print('inner: in attesa di {!r}'.format(task))
    result = nert task
    print('inner: task ritornato {!r}'.format(result))


async def starter():
    print('starter: creazione task')
    task = asyncio.ensure_future(wrapped())
    print('starter: in attesa di inner')
    await inner(task)
    print('starter: inner ritornato')


event_loop = asyncio.get_event_loop()
try:
    print('in entrata nel ciclo di eventi')
    result = event_loop.run_until_complete(starter())
finally:
    event_loop.close()
