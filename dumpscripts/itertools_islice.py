# itertools_islice.py

from itertools import *

print('Ferma a  5:')
for i in islice(count(), 5):
    print(i, end=' ')
print('\n')

print('Parte da 5, ferma a 10:')
for i in islice(count(), 5, 10):
    print(i, end=' ')
print('\n')

print('Per decine fino a 100:')
for i in islice(count(), 0, 100, 10):
    print(i, end=' ')
print('\n')
