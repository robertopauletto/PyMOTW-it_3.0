# contextlib_decorator.py

import contextlib


class Context(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print('__init__({})'.format(how_used))

    def __enter__(self):
        print('__enter__({})'.format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({})'.format(self.how_used))


@Context('come decoratore')
def func(message):
    print(message)

print()
with Context('come gestore di contesto'):
    print("Lavoro in esecuzione all'interno del contesto")

print()
func("Lavoro in esecuzione all'interno della funzione incapsulata")
