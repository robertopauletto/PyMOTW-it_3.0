#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
from pprint import pprint
import weakref

from weakref_graph import Graph, demo, collect_and_show_garbage

gc.set_debug(gc.DEBUG_LEAK)

print 'Impostazione del ciclo'
print
demo(Graph)

print
print 'Interruzione del ciclo e pulizia del garbage'
print
gc.garbage[0].set_next(None)
while gc.garbage:
    del gc.garbage[0]
print
collect_and_show_garbage()