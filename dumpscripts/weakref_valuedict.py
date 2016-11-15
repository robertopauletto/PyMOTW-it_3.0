# weakref_valuedict.py

import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject(object):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject(%s)' % self.name

    def __del__(self):
        print('    (In eliminazione {})'.format(self))


def demo(cache_factory):
    # trattiene gli oggetti in modo che nessuna weak reference
    # venga rimossa immediatamente
    all_refs = {}
    # creazione della cache utilizzando la factory
    print('TIPO CACHE:', cache_factory)
    cache = cache_factory()
    for name in ['uno', 'due', 'tre']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o  # decref

    print('  all_refs =', end=' ')
    pprint(all_refs)
    print('\n  Prima, la cache contiene:', list(cache.keys()))
    for name, value in cache.items():
        print('    {} = {}'.format(name, value))
        del value  # decref

    # Rimuove tutti i riferimenti agli oggetti tranne la cache
    print('\n Pulizia:')
    del all_refs
    gc.collect()

    print('\n  Dopo, la cache contiene:', list(cache.keys()))
    for name, value in cache.items():
         print('    {} = {}'.format(name, value))
    print('   demo in uscita')
    return

demo(dict)
print
demo(weakref.WeakValueDictionary)
