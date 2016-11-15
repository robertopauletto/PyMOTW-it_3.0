# weakref_ref.py

import weakref


class ExpensiveObject:

    def __del__(self):
        print('(In eliminazione {})'.format(self))


obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('eliminazione di obj')
del obj
print('r():', r())
