# futures_process_pool_map.py

from concurrent import futures
import os


def task(n):
    return (n, os.getpid())


ex = futures.ProcessPoolExecutor(max_workers=2)
results = ex.map(task, range(5, 0, -1))
for n, pid in results:
    print('escuzione del compito {} in elaborazione {}'.format(n, pid))
