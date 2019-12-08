# asyncio_future_callback.py

import asyncio
import functools


def callback(future, n):
    print('{}: future completato: {}'.format(n, future.result()))


async def register_callbacks(all_done):
    print('registrazione dei callbacks sul future')
    all_done.add_done_callback(functools.partial(callback, n=1))
    all_done.add_done_callback(functools.partial(callback, n=2))


async def main(all_done):
    await register_callbacks(all_done)
    print('impostazione risultato del future')
    all_done.set_result('il risultato')


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.run_until_complete(main(all_done))
finally:
    event_loop.close()
