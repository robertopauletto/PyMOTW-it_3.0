# collections_namedtuple_asdict.py
import collections

Person = collections.namedtuple('Persona', 'nome anni')

bob = Person(nome='Bob', anni=30)
print('\nRappresentazione:', bob)
print('Come Dizionario:', bob._asdict())
