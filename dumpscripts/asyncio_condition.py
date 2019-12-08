# asyncio_condition.py

import asyncio


async def consumer(condition, n):
    async with condition:
        print('consumatore {} in attesa'.format(n))
        await condition.wait()
        print('consumatore {} attivato'.format(n))
    print('chiusura consumatore {}'.format(n))


async def manipulate_condition(condition):
    print('manipulate_condition in partenza')

    # pausa per lasciare che il consumatore parta
    await asyncio.sleep(0.1)

    for i in range(1, 3):
        async with condition:
            print('notifica {} consumatori'.format(i))
            condition.notify(n=i)
        await asyncio.sleep(0.1)

    async with condition:
        print('notifica i consumatori rimanenti')
        condition.notify_all()

    print('ending manipulate_condition')


async def main(loop):
    # Crea una condizione
    condition = asyncio.Condition()

    # Imposta attività che monitorano la condizione
    consumers = [
        consumer(condition, i)
        for i in range(5)
    ]

    # Pianifica attività per manipolare la variabile della condizione
    loop.create_task(manipulate_condition(condition))

    # Attende che il consumatore abbia terminato
    await asyncio.wait(consumers)


event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
