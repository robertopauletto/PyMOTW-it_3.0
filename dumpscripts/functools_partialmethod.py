# functools_partialmethod.py

import functools


def standalone(self, a=1, b=2):
    "Funzione standalone"
    print('  chiamata standalone con:', (self, a, b))
    if self is not None:
        print('  self.attr =', self.attr)


class MyClass:
    "Classe Demo per functools"

    def __init__(self):
        self.attr = 'attributo di istanza'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


o = MyClass()

print('standalone')
standalone(None)
print()

print('method1 come partialmethod')
o.method1()
print()

print('method2 come partial')
try:
    o.method2()
except TypeError as err:
    print('ERRORE: {}'.format(err))
