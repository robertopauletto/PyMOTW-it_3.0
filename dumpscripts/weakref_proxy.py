# weakref_proxy.py

import weakref


class ExpensiveObject:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('(Eliminazione di  {})'.format(self))


obj = ExpensiveObject('Il mio oggetto')
r = weakref.ref(obj)
p = weakref.proxy(obj)

print('via obj:', obj.name)
print('via ref:', r().name)
print('via proxy:', p.name)
del obj
print('via proxy:', p.name)

