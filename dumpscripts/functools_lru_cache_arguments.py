# functools_lru_cache_arguments.py

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


make_call(1, 2)

try:
    make_call([1], 2)
except TypeError as err:
    print('ERRORE: {}'.format(err))

try:
    make_call(1, {'2': 'due'})
except TypeError as err:
    print('ERRORE: {}'.format(err))
