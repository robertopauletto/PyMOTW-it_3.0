# threading_event.py

import logging
import threading
import time


def wait_for_event(e):
    """Attende che l'evento sia impostato prima di fare qualsiasi cosa"""
    logging.debug('wait_for_event in partenza')
    event_is_set = e.wait()
    logging.debug('evento impostato: %s', event_is_set)


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.is_set():
        logging.debug('wait_for_event_timeout in partenza')
        event_is_set = e.wait(t)
        logging.debug('evento impostato: %s', event_is_set)
        if event_is_set:
            logging.debug('evento in elaborazione')
        else:
            logging.debug('altro lavoro in esecuzione')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

e = threading.Event()
t1 = threading.Thread(
    name='block',
    target=wait_for_event,
    args=(e,),
)
t1.start()

t2 = threading.Thread(
    name='nonblock',
    target=wait_for_event_timeout,
    args=(e, 2),
)
t2.start()

logging.debug('In attesa prima di chiamare Event.set()')
time.sleep(0.3)
e.set()
logging.debug('Event è impostato')
