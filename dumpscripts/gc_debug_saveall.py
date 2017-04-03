# gc_debug_saveall.py

import gc

flags = (gc.DEBUG_COLLECTABLE |
         gc.DEBUG_UNCOLLECTABLE |
         gc.DEBUG_SAVEALL
         )

gc.set_debug(flags)


class Graph(object):

    def __init__(self, name):
        self.name = name
        self.next = None

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__, self.name)


class CleanupGraph(Graph):

    def __del__(self):
        print('{}.__del__()'.format(self))


# Costruisce un ciclo di Grafi
one = Graph('uno')
two = Graph('due')
one.set_next(two)
two.set_next(one)

# Costruisce un altro nodo a se stante
three = CleanupGraph('tre')

# Costruisce un ciclo di grafi con un finalizzatore
four = CleanupGraph('quattro')
five = CleanupGraph('cinque')
four.set_next(five)
five.set_next(four)

# Rimuove riferimenti ai nodi del grafo nello spazio dei nomi di questo modulo
one = two = three = four = five = None

# Force una raccolta
print('In raccolta')
gc.collect()
print('Fatto')

# Riporta ciò che è rimasto
for o in gc.garbage:
    if isinstance(o, Graph):
        print('Trattenuto: {} 0x{:x}'.format(o, id(o)))

# Reimposta i flag di debug prima di uscire per evitare di scaricare molte
# nformazioni extra che renderebbe l'output di esempio meno chiaro
gc.set_debug(0)

