# multiprocessing_log_to_stderr.py

import multiprocessing
import logging
import sys


def worker():
    print('Esecuzione di qualche attività')
    sys.stdout.flush()


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
