# operator_classes.py

from operator import *


class MyObj:
    """Esempio per overload di operatore"""

    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val

    def __str__(self):
        return 'MyObj({})'.format(self.val)

    def __lt__(self, other):
        """confronto per minore di"""
        print('Verifica {} < {}'.format(self, other))
        return self.val < other.val

    def __add__(self, other):
        """aggiunge valori"""
        print('Aggiungo {} + {}'.format(self, other))
        return MyObj(self.val + other.val)


a = MyObj(1)
b = MyObj(2)

print('Confronto:')
print(lt(a, b))

print('\nAritmetica:')
print(add(a, b))
