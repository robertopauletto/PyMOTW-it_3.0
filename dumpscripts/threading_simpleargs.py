# threading_simpleargs.py

import threading


def worker(num):
    """Funzione in esecuzione nel thread"""
    print('Esecutore: %s' % num)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
