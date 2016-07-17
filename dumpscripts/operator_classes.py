
from operator import *

class MyObj(object):
    """Esempio per l'overloading dell'operatore"""
    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val
        return
    def __str__(self):
        return 'MyObj(%s)' % self.val
    def __lt__(self, other):
        """confronto per minore-di"""
        print 'Test %s < %s' % (self, other)
        return self.val < other.val
    def __add__(self, other):
        """aggiunta valori"""
        print 'Aggiungo %s + %s' % (self, other)
        return MyObj(self.val + other.val)

a = MyObj(1)
b = MyObj(2)

print lt(a, b)
print add(a, b)
