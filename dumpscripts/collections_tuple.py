# collections_tuple.py

import collections

Person = collections.namedtuple('Persona', 'name age')

bob = ('Bob', 30, 'maschio')
print('Rappresentazione:', bob)

jane = ('Jane', 29, 'femmina')
print('\nCampo per indice:', jane[0])

print('\nCampi per indice:')
for p in [bob, jane]:
    print('{} ha {} anni, {}'.format(*p))
