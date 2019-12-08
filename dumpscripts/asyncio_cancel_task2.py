# asyncio_cancel_task2.py

import asyncio


async def task_func():
    print('in task_func, in pausa')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task_func è stata cancellata')
        raise
    return 'the result'


def task_canceller(t):
    print('in task_canceller')
    t.cancel()
    print('cancellazione del task')


async def main(loop):
    print('creazione task')
    task = loop.create_task(task_func())
    loop.call_soon(task_canceller, task)
    try:
        await task
    except asyncio.CancelledError:
        print('anche main() vede il task come cancellato')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
