# functools_lru_cache_expire.py

import functools


@functools.lru_cache(maxsize=2)
def expensive(a, b):
    print('chiamata di expensive({}, {})'.format(a, b))
    return a * b


def make_call(a, b):
    print('({}, {})'.format(a, b), end=' ')
    pre_hits = expensive.cache_info().hits
    expensive(a, b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print('utilizzo la cache')


print('Impostazione della cache')
make_call(1, 2)
make_call(2, 3)

print('\nUtilizzo di elementi in cache')
make_call(1, 2)
make_call(2, 3)

print('\nCalcolo di un nuovo valore, provocando la scadenza della cache')
make_call(3, 4)

print('\nLa cache contiene ancora un vecchio elemento')
make_call(2, 3)

print('\nGli elementi più vecchi devono essere ricalcolati')
make_call(1, 2)
