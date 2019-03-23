# threading_rlock.py

import threading

lock = threading.RLock()

print('Primo tentativo :', lock.acquire())
print('Secondo tentativo:', lock.acquire(0))
