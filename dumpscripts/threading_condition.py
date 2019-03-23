# threading_condition.py

import logging
import threading
import time


def consumer(cond):
    """Attende la condizione ed usa la risorsa"""
    logging.debug('Partenza del thread consumer ')
    with cond:
        cond.wait()
        logging.debug('La risorsa è disponibile per consumer')


def producer(cond):
    """Imposta la risorsa che viene usata da consumer"""
    logging.debug('Partenza del thread producer')
    with cond:
        logging.debug('Si rende disponibile la risorsa')
        cond.notifyAll()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer,
                      args=(condition,))
c2 = threading.Thread(name='c2', target=consumer,
                      args=(condition,))
p = threading.Thread(name='p', target=producer,
                     args=(condition,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()
