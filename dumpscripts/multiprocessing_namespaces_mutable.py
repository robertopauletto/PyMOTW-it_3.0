# multiprocessing_namespaces_mutable.py

import multiprocessing


def producer(ns, event):
    # DOES NOT UPDATE GLOBAL VALUE!
    ns.my_list.append('Questo è il valroe')
    event.set()


def consumer(ns, event):
    print('Prima dell\' evento:', ns.my_list)
    event.wait()
    print('Dopo l\' evento :', ns.my_list)


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = []

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
