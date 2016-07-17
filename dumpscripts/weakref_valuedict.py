#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_LEAK)

class ExpensiveObject(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'ExpensiveObject(%s)' % self.name
    def __del__(self):
        print '(Deleting %s)' % self
        
def demo(cache_factory):
    # trattiene gli oggetti in modo che nessuna weak reference
    # venga rimossa immediatamente
    all_refs = {}
    # La cache utilizza la factory che forniamo
    print 'TIPO CACHE:', cache_factory
    cache = cache_factory()
    for name in [ 'uno', 'due', 'tre' ]:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o # decref

    print 'all_refs =',
    pprint(all_refs)
    print 'Prima, la cache contiene:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
        del value # decref
        
    # Rimuove tutti i riferimenti ai nostri oggetti tranne la cache
    print 'Pulizia:'
    del all_refs
    gc.collect()

    print 'Dopo, la cache contiene:', cache.keys()
    for name, value in cache.items():
        print '  %s = %s' % (name, value)
    print 'demo in uscita'
    return

demo(dict)
print
demo(weakref.WeakValueDictionary)