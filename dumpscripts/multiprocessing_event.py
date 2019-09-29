# multiprocessing_event.py

import multiprocessing
import time


def wait_for_event(e):
    """Attence che l'evento sia impostato prima di fare qualcosa"""
    print('wait_for_event: in partenza')
    e.wait()
    print('wait_for_event: e.is_set()->', e.is_set())


def wait_for_event_timeout(e, t):
    """Attende t secondi, poi va in pausa"""
    print('wait_for_event_timeout: starting')
    e.wait(t)
    print('wait_for_event_timeout: e.is_set()->', e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    w1.start()

    w2 = multiprocessing.Process(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    w2.start()

    print('principale: in attesa prima di chiamare Event.set()')
    time.sleep(3)
    e.set()
    print('principale: evento impostato')
