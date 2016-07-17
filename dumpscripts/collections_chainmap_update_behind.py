# collections_chainmap_update_behind.py


import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print('Prima: {}'.format(m['c']))
a['c'] = 'E'
print('Dopo : {}'.format(m['c']))
