# collections_chainmap_update_directly.py


import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Prima:', m)
m['c'] = 'E'
print('Dopo :', m)
print('a:', a)
