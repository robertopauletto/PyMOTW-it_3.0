# asyncio_coroutine_chain.py

import asyncio


async def outer():
    print('all\'esterno')
    print('in attesa di result1')
    result1 = await phase1()
    print('in attesa di result2')
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    print('in phase1')
    return 'result1'


async def phase2(arg):
    print('in phase2')
    return 'result2 deriva da {}'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print('valore ritornato: {!r}'.format(return_value))
finally:
    event_loop.close()
