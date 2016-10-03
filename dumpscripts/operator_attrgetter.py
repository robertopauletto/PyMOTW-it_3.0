# operator_attrgetter.py

from operator import *


class MyObj:
    """classe di esempio for attrgetter"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)


l = [MyObj(i) for i in range(5)]
print('oggetti   :', l)

# Estrae il valore 'arg' da ogni oggetto
g = attrgetter('arg')
vals = [g(i) for i in l]
print('valori arg:', vals)

# Sort using arg
l.reverse()
print('invertiti  :', l)
print('ordinati   :', sorted(l, key=g))
