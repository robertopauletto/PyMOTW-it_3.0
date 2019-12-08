# asyncio_cancel_task.py

import asyncio


async def task_func():
    print('in task_func')
    return 'il risultato'


async def main(loop):
    print('creazione task')
    task = loop.create_task(task_func())

    print('cancellazione task')
    task.cancel()

    print('task cancellato {!r}'.format(task))
    try:
        await task
    except asyncio.CancelledError:
        print('catturato errore dal task cancellato')
    else:
        print('task result: {!r}'.format(task.result()))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
