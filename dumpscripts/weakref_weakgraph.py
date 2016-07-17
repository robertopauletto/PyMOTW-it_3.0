#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
from pprint import pprint
import weakref

from weakref_graph import Graph, demo

class WeakGraph(Graph):
    def set_next(self, other):
        if other is not None:
            # Verificare se si debba sostituire il riferimento ad
            # other con una weakref.
            if self in other.all_nodes():
                other = weakref.proxy(other)
        super(WeakGraph, self).set_next(other)
        return

demo(WeakGraph)    