# gc_debug_leak.py

import gc

flags = gc.DEBUG_LEAK

gc.set_debug(flags)


class Graph:

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
one = Graph('Uno')
two = Graph('Due')
one.set_next(two)
two.set_next(one)


# Costruisce un altro nodo a se stante
three = CleanupGraph('tre')

# Costruisce un ciclo di Grafi con un finalizzatore
four = CleanupGraph('quattro')
five = CleanupGraph('cinque')
four.set_next(five)
five.set_next(four)

# Elimina i riferimenti ai nodi del grafo in questo spazio dei nomi del modulo
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
