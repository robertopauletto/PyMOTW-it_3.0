# threading_lock_reacquire.py

import threading

lock = threading.Lock()

print('Primo tentativo :', lock.acquire())
print('Secondo tentativo:', lock.acquire(0))
