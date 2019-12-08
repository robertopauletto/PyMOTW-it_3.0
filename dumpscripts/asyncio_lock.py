# asyncio_lock.py

import asyncio
import functools


def unlock(lock):
    print('callback per rilasciare il bloccaggio')
    lock.release()


async def coro1(lock):
    print('coro1 in attesa del bloccaggio')
    async with lock:
        print('coro1 ha acquisito il bloccaggio')
    print('coro1 ha rilasciato il bloccaggio')


async def coro2(lock):
    print('coro2 in attesa del bloccaggio')
    await lock.acquire()
    try:
        print('coro2 ha acquisito il bloccaggio')
    finally:
        print('coro2 ha rilasciato il bloccaggio')
        lock.release()


async def main(loop):
    # Crea e acquisisce un bloccaggio condiviso
    lock = asyncio.Lock()
    print('acquisizione del bloccaggio prima di far partire coroutine')
    await lock.acquire()
    print('bloccaggio acquisito: {}'.format(lock.locked()))

    # Pianifica un callback per sbloccare il bloccaggio
    loop.call_later(0.1, functools.partial(unlock, lock))

    # Esegue le coroutines che vogliono usare il bloccaggio
    print('in attesa di coroutines')
    await asyncio.wait([coro1(lock), coro2(lock)]),


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
