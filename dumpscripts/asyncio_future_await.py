# asyncio_future_await.py

import asyncio


def mark_done(future, result):
    print('impostazione del risultato del future a {!r}'.format(result))
    future.set_result(result)


async def main(loop):
    all_done = asyncio.Future()

    print('pianificazione di mark_done')
    loop.call_soon(mark_done, all_done, 'il risultato')

    result = await all_done
    print('risultato ritornato: {!r}'.format(result))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
