#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
import pprint
import sys

try:
    threshold = int(sys.argv[1])
except (IndexError, ValueError, TypeError):
    print 'Soglia mancante o non valida, si utilizza la predefinita'
    threshold = 5

class MyObj(object):
    def __init__(self, name):
        self.name = name
        print 'Creato', self.name

gc.set_debug(gc.DEBUG_STATS)

gc.set_threshold(threshold, 1, 1)
print 'Soglie:', gc.get_threshold()

print 'Pulisce il collettore forzando una esecuzione'
gc.collect()
print

print 'Creazione oggetti'
objs = []
for i in range(10):
    objs.append(MyObj(i))
