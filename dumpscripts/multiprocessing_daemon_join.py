# multiprocessing_daemon_join.py

import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print('In partenza:', name)
    time.sleep(2)
    print('In uscita :', name)


def non_daemon():
    name = multiprocessing.current_process().name
    print('In partenza:', name)
    print('In uscita :', name)


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non-daemon',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
