# threading_lock_with.py

import threading
import logging


def worker_with(lock):
    with lock:
        logging.debug('Bloccaggio acquisito via with')


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquisito direttamente')
    finally:
        lock.release()


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()
