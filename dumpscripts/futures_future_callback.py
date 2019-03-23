# futures_future_callback.py

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
        error = fn.exception()
        if error:
            print('{}: errore restituito: {}'.format(
                fn.arg, error))
        else:
            result = fn.result()
            print('{}: valore restituito: {}'.format(
                fn.arg, result))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('principale: in partenza')
    f = ex.submit(task, 5)
    f.arg = 5
    f.add_done_callback(done)
    result = f.result()
