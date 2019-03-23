# threading_simple.py

import threading


def worker():
    """funzione in esecuzione nel thread"""
    print('Esecutore')


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
