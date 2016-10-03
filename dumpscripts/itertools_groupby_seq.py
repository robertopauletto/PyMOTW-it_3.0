# itertools_groupby_seq.py

import functools
from itertools import *
import operator
import pprint


@functools.total_ordering
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __gt__(self, other):
        return (self.x, self.y) > (other.x, other.y)


# Crea un insieme di dati di istanze di Point
data = list(map(Point,
                cycle(islice(count(), 3)),
                islice(count(), 7)))
print('Dati:')
pprint.pprint(data, width=35)
print()

# Cerca di raggruppare i dati non ordinati in baase al valore di X
print('Raggruppati, non ordinati:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# Ordina i dati
data.sort()
print('Ordinati:')
pprint.pprint(data, width=35)
print()

# Raggruppa i dati ordinati in base ai valori di X
print('Raggruppati, ordinati:')
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()
