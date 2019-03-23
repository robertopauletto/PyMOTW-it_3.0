# futures_thread_pool_map.py

from concurrent import futures
import threading
import time


def task(n):
    print('{}: in pausa {}'.format(
        threading.current_thread().name,
        n)
    )
    time.sleep(n / 10)
    print('{}: eseguito con {}'.format(
        threading.current_thread().name,
        n)
    )
    return n / 10


ex = futures.ThreadPoolExecutor(max_workers=2)
print('principale: in partenza')
results = ex.map(task, range(5, 0, -1))
print('principale: risultati non elaborati {}'.format(results))
print('principale: in attesa dei veri risultati')
real_results = list(results)
print('principale: resultati: {}'.format(real_results))
