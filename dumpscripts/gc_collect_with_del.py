#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
import pprint
import Queue

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None
    def set_next(self, next):
        print 'Collegamento nodi %s.next = %s' % (self, next)
        self.next = next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)
    def __del__(self):
        print '%s.__del__()' % self
        
# Construisce un ciclo di Grafi
one = Graph('uno')
two = Graph('due')
three = Graph('tre')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# Rimuove riferimenti ai nodi del grafo nello spazio dei nomi di questo modulo
one = two = three = None

# Mostra gli effetti della garbage collection
print 'In raccolta %d ...'
n = gc.collect()
print 'Oggetti non raggiungibili:'
print 'Garbage rimanente:', 
pprint.pprint(gc.garbage)
