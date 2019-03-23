# futures_thread_pool_submit.py

from concurrent import futures
import threading
import time


def task(n):
    print('{}: in pausa {}'.format(
        threading.current_thread().name,
        n)
    )
    time.sleep(n / 10)
    print('{}: fatto con {}'.format(
        threading.current_thread().name,
        n)
    )
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
print('principale: starting')
f = ex.submit(task, 5)
print('principale: future: {}'.format(f))
print('principale: in attesa di risultati')
result = f.result()
print('principale: risultato: {}'.format(result))
print('principale: future dopo il risultato: {}'.format(f))
