# gc_collect.py

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

# Costruisce un ciclo di Grafi
one = Graph('uno')
two = Graph('due')
three = Graph('tre')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# Rimuove riferimenti ai nodi del grafo nello spazio dei nomi di questo modulo
one = two = three = None
\
# Mostra gli effetti del garbage collection
for i in range(2):
    print('In raccolta {} ...'.format(i))
    n = gc.collect()
    print('Oggetti non raggiungibili:', n)
    print('Garbage rimanente:', end=' ')
    pprint.pprint(gc.garbage)
