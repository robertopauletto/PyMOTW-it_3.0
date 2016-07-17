# collections_namedtuple_rename.py

import collections

with_class = collections.namedtuple(
    'Persona', 'nome class anni',
    rename=True)
print(with_class._fields)

two_ages = collections.namedtuple(
    'Persona', 'nome anni anni',
    rename=True)
print(two_ages._fields)
