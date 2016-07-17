# collections_counter_arithmetic.py

import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alfabeto')

print('C1:', c1)
print('C2:', c2)

print('\nContatori combinati:')
print(c1 + c2)

print('\nSottrazione:')
print(c1 - c2)

print('\nIntersezione (considerando i minimi positivi):')
print(c1 & c2)

print('\nUnione (considerando i massimi):')
print(c1 | c2)
