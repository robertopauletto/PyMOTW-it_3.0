#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
from pprint import pprint
import weakref

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.other = None
    def set_next(self, other):
        print '%s.set_next(%s (%s))' % (self.name, other, type(other))
        self.other = other
    def all_nodes(self):
        "Genera i nodi nella sequenza del grafo."
        yield self
        n = self.other
        while n and n.name != self.name:
            yield n
            n = n.other
        if n is self:
            yield n
        return
    def __str__(self):
        return '->'.join([n.name for n in self.all_nodes()])
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)
    def __del__(self):
        print '(Eliminazione di  %s)' % self.name
        self.set_next(None)

class WeakGraph(Graph):
    def set_next(self, other):
        if other is not None:
            # Verificare se si debba sostituire il riferimento ad
            # other con una weakref.
            if self in other.all_nodes():
                other = weakref.proxy(other)
        super(WeakGraph, self).set_next(other)
        return

def collect_and_show_garbage():
    "Mostra che garbage è presente."
    print 'Raccolta...'
    n = gc.collect()
    print 'Oggetti irraggiungili:', n
    print 'Garbage:', 
    pprint(gc.garbage)

def demo(graph_factory):
    print 'Impostazione del grafo'
    one = graph_factory('uno')
    two = graph_factory('due')
    three = graph_factory('tre')
    one.set_next(two)
    two.set_next(three)
    three.set_next(one)

    print
    print 'Grafi :'
    print str(one)
    print str(two)
    print str(three)
    collect_and_show_garbage()

    print
    three = None
    two = None
    print 'Dopo la rimozione di 2 riferimenti:'
    print str(one)
    collect_and_show_garbage()

    print
    print "Rimozione dell'ultimo riferimento"
    one = None
    collect_and_show_garbage()