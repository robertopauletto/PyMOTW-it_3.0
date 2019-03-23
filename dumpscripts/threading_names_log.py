# threading_names_log.py

import logging
import threading
import time


def worker():
    logging.debug('Partenza')
    time.sleep(0.2)
    logging.debug('Uscita')


def my_service():
    logging.debug('Partenza')
    time.sleep(0.3)
    logging.debug('Uscita')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t = threading.Thread(name='il_mio_servizio', target=my_service)
w = threading.Thread(name='esecutore', target=worker)
w2 = threading.Thread(target=worker)  # usa nome predefinito

w.start()
w2.start()
t.start()
