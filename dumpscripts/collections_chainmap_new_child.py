# collections_chainmap_new_child.py


import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 prima:', m1)
print('m2 prima:', m2)

m2['c'] = 'E'

print('m1 dopo:', m1)
print('m2 dopo:', m2)
