# multiprocessing_namespaces.py

import multiprocessing


def producer(ns, event):
    ns.value = 'Questo è il valore'
    event.set()


def consumer(ns, event):
    try:
        print('Prima dell\'evento: {}'.format(ns.value))
    except Exception as err:
        print('Prima dell\'evento, errore:', str(err))
    event.wait()
    print('Dopo l\'evento:', ns.value)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    event = multiprocessing.Event()
    p = multiprocessing.Process(
        target=producer,
        args=(namespace, event),
    )
    c = multiprocessing.Process(
        target=consumer,
        args=(namespace, event),
    )

    c.start()
    p.start()

    c.join()
    p.join()
