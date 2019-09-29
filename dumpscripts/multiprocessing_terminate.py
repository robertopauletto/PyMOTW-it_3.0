# multiprocessing_terminate.py

import multiprocessing
import time


def slow_worker():
    print('Elaboratore in partenza')
    time.sleep(0.1)
    print('Elaborazione conclusa')


if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print('PRIMA:', p, p.is_alive())

    p.start()
    print('DURANTE:', p, p.is_alive())

    p.terminate()
    print('TERMINATO:', p, p.is_alive())

    p.join()
    print('CON JOIN:', p, p.is_alive())
