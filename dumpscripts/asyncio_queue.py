# asyncio_queue.py

import asyncio


async def consumer(n, q):
    print('consumatore {}: in partenza'.format(n))
    while True:
        print('consumatore {}: in attesa di un elemento'.format(n))
        item = await q.get()
        print('consumatore {}: ha elemento {}'.format(n, item))
        if item is None:
            # None è il segnale di arresto
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
    print('consumatore {}: in chiusura'.format(n))


async def producer(q, num_workers):
    print('produttore: in partenza')
    # Aggiunge alcuni numeri alla coda per simulare dei compiti
    for i in range(num_workers * 3):
        await q.put(i)
        print('produttore: aggiunto compito {} alla coda'.format(i))
    # Aggiunge elementi None alla coda
    # per segnalare al consumatore di uscire
    print('produttore: aggiunta di segnali di arresto alla coda')
    for i in range(num_workers):
        await q.put(None)
    print('produttore: in attesa che la coda si svuoti')
    await q.join()
    print('produttore: in chiusura')


async def main(loop, num_consumers):
    # Crea la coda con dimensione fissa in modo che il produttore
    # possa bloccare fino a che il consumatore abbia estratto qualche elemento
    q = asyncio.Queue(maxsize=num_consumers)

    # Pianifica il compito del consumatore
    consumers = [
        loop.create_task(consumer(i, q))
        for i in range(num_consumers)
    ]

    # Pianifica il compito del produttore.
    prod = loop.create_task(producer(q, num_consumers))

    # Attende che tutte le coroutine finiscano
    await asyncio.wait(consumers + [prod])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop, 2))
finally:
    event_loop.close()
