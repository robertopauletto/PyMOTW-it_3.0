# threading_timer.py

import threading
import time
import logging


def delayed():
    logging.debug('elaboratore in esecuzione')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

t1 = threading.Timer(0.3, delayed)
t1.setName('t1')
t2 = threading.Timer(0.3, delayed)
t2.setName('t2')

logging.debug('timer partiti')
t1.start()
t2.start()

logging.debug('in attesa prima di cancellare %s', t2.getName())
time.sleep(0.2)
logging.debug('cancellazione %s', t2.getName())
t2.cancel()
logging.debug('fatto')
