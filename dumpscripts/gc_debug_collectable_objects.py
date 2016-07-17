#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc

flags = (gc.DEBUG_COLLECTABLE |
         gc.DEBUG_UNCOLLECTABLE |
         gc.DEBUG_OBJECTS
         )
gc.set_debug(flags)

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None
        print 'Creazione di %s 0x%x (%s)' % (self.__class__.__name__, id(self), name)
    def set_next(self, next):
        print 'Connessione nodi %s.next = %s' % (self, next)
        self.next = next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)

class CleanupGraph(Graph):
    def __del__(self):
        print '%s.__del__()' % self

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

print

# Force una raccolta
print 'In raccolta'
gc.collect()
print 'Fatto'