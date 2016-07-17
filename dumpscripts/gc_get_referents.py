#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
import pprint

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None
    def set_next(self, next):
        print 'Collegamento nodi %s.next = %s' % (self, next)
        self.next = next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)

# Costruisce un ciclo di Grafi
one = Graph('uno')
two = Graph('due')
three = Graph('tre')
one.set_next(two)
two.set_next(three)
three.set_next(one)

print
print 'tre si riferisce a:'
for r in gc.get_referents(three):
    pprint.pprint(r)
