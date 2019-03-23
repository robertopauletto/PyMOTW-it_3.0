# futures_future_exception.py

from concurrent import futures


def task(n):
    print('{}: in partenza'.format(n))
    raise ValueError('il valore {} non è buono'.format(n))


ex = futures.ThreadPoolExecutor(max_workers=2)
print('principale: in partenza')
f = ex.submit(task, 5)

error = f.exception()
print('principale: errore: {}'.format(error))

try:
    result = f.result()
except ValueError as e:
    print('principale: visto l\'errore "{}" accedendo a result'.format(e))
