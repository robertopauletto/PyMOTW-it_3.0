# multiprocessing_daemon.py

import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print('In partenza:', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(2)
    print('In uscita :', p.name, p.pid)
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print('In partenza:', p.name, p.pid)
    sys.stdout.flush()
    print('In uscita :', p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(
        name='demone',
        target=daemon,
    )
    d.daemon = True

    n = multiprocessing.Process(
        name='non demone',
        target=non_daemon,
    )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
