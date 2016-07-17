# collections_namedtuple_person.py

import collections

Person = collections.namedtuple('Persona', 'nome anni')

bob = Person(nome='Bob', anni=30)
print('\nRappresentazione:', bob)

jane = Person(nome='Jane', anni=29)
print('\nCampo per indice:', jane.nome)

print('\nCampi per indice:')
for p in [bob, jane]:
    print('{} ha {} anni'.format(*p))
