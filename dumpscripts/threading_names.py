# threading_names.py

import threading
import time


def worker():
    print(threading.current_thread().getName(), 'Partenza')
    time.sleep(0.2)
    print(threading.current_thread().getName(), 'Uscita')


def my_service():
    print(threading.current_thread().getName(), 'Partenza')
    time.sleep(0.3)
    print(threading.current_thread().getName(), 'Uscita')


t = threading.Thread(name='il_mio_servizio', target=my_service)
w = threading.Thread(name='esecutore', target=worker)
w2 = threading.Thread(target=worker)  # usa nome predefinito

w.start()
w2.start()
t.start()
