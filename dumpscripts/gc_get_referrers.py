# gc_get_referrers.py

import gc
import pprint


class Graph(object):

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        print('Collegamento nodi {}.next = {}'.format(self, next))
        self.next = next

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.name)

    def __del__(self):
        print('{}.__del__()'.format(self))

# Costruisce un ciclo di Grafi
one = Graph('uno')
two = Graph('due')
three = Graph('tre')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# Rimuove riferimenti ai nodi del grafo nello spazio dei nomi di questo modulo
one = two = three = None

# Se si raccoglie ora gli oggetti non sono possono essere raccolti
print()
print('In raccolta ...')
n = gc.collect()
print('Oggetti non raggiungibili:', n)
print('Garbage rimanente:', end=' ')
pprint.pprint(gc.garbage)

REFERRERS_TO_IGNORE = [locals(), globals(), gc.garbage]


def find_referring_graphs(obj):
    print('Si cercano riferimenti a {}').format(repr(obj))
    referrers = (r for r in gc.get_referrers(obj)
                 if r not in REFERRERS_TO_IGNORE)
    for ref in referrers:
        if isinstance(ref, Graph):
            # Un nodo grafo
            yield ref
        elif isinstance(ref, dict):
            # Una istanza od un altro dizionario di spazio dei nomi
            for parent in find_referring_graphs(ref):
                yield parent


#  Cerca oggetti che fanno riferimento ad oggetti che rimangono in gc.garbage.
print()
print('Pulizia dei referenti:')
for obj in gc.garbage:
    for ref in find_referring_graphs(obj):
        ref.set_next(None)
        del ref  # rimuove riferimento locale per poter eliminare il nodo
    del obj  # rimuove riferimento locale così che si possa eliminare il nodo


# Pulizia dei riferimenti mantenuti da gc.garbage
print()
print('Pulizia di gc.garbage:')
del gc.garbage[:]

# A questo punto tutto dovrebbe essere stato liberato
print()
print('In raccolta ...')
n = gc.collect()
print('Oggetti non raggiungibili:')
print('Garbage rimanente:', end=' ')
pprint.pprint(gc.garbage)
