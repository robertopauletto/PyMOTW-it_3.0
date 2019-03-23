# threading_daemon.py

import threading
import time
import logging


def daemon():
    logging.debug('Partenza')
    time.sleep(0.2)
    logging.debug('Uscita')


def non_daemon():
    logging.debug('Partenza')
    logging.debug('Uscita')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

d = threading.Thread(name='demone', target=daemon, daemon=True)

t = threading.Thread(name='non-demone', target=non_daemon)

d.start()
t.start()
