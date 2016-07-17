# collections_namedtuple_fields.py

import collections

Person = collections.namedtuple('Persona', 'nome anni')

bob = Person(nome='Bob', anni=30)
print('\nRappresentazione:', bob)
print('Campi:', bob._fields)
