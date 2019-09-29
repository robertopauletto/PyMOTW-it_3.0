# multiprocessing_simpleargs.py

import multiprocessing


def worker(num):
    """Funzione del thread elaboratore"""
    print('Elaboratore:', num)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()