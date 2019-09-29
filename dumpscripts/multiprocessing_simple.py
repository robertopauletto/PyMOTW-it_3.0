# multiprocessing_simple.py

import multiprocessing


def worker():
    """Funzione elaboratore"""
    print('Elaboratore')


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()