# futures_future_callback_cancel.py

from concurrent import futures
import time


def task(n):
    print('{}: in pausa'.format(n))
    time.sleep(0.5)
    print('{}: fatto'.format(n))
    return n / 10


def done(fn):
    if fn.cancelled():
        print('{}: cancellato'.format(fn.arg))
    elif fn.done():
        print('{}: non cancellato'.format(fn.arg))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('principale: in partenza')
    tasks = []

    for i in range(10, 0, -1):
        print('principale: sottomesso {}'.format(i))
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))

    for i, t in reversed(tasks):
        if not t.cancel():
            print('principale: non si cancella {}'.format(i))

    ex.shutdown()
