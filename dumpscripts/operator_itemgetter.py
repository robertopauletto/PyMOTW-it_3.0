# operator_itemgetter.py

from operator import *

l = [dict(val=-1 * i) for i in range(4)]
print('Dizionali:')
print(' originale:', l)
g = itemgetter('val')
vals = [g(i) for i in l]
print('   valori:', vals)
print('   ordinati:', sorted(l, key=g))

print
l = [(i, i * -2) for i in range(4)]
print('\nTuple:')
print(' originale:', l)
g = itemgetter(1)
vals = [g(i) for i in l]
print('   valori:', vals)
print('   ordinati:', sorted(l, key=g))
