# threading_lock.py

import logging
import random
import threading
import time


class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('In attesa del bloccaggio')
        self.lock.acquire()
        try:
            logging.debug('Bloccaggio acquisito')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('In pausa %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Fatto')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('In attesa dei thread elaboratori')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Contatorer: %d', counter.value)
