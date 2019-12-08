# asyncio_future_event_loop.py

import asyncio


def mark_done(future, result):
    print('Impostazione del risultato future a {!r}'.format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print('pianificazione mark_done')
    event_loop.call_soon(mark_done, all_done, 'il risultato')

    print('entrata nel ciclo di eventi')
    result = event_loop.run_until_complete(all_done)
    print('risultato restituito: {!r}'.format(result))
finally:
    print('chiusura del ciclo di eventi')
    event_loop.close()

print('risultato future: {!r}'.format(all_done.result()))
