# collections_namedtuple_replace.py

import collections

Person = collections.namedtuple('Persona', 'nome anni')

bob = Person(nome='Bob', anni=30)
print('\nPrima:', bob)
bob2 = bob._replace(nome='Robert')
print('Dopo:', bob2)
print('Uguali?:', bob is bob2)
