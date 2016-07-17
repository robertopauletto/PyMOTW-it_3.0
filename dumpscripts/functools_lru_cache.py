# functools_lru_cache.py

import functools


@functools.lru_cache()
def expensive(a, b):
    print('expensive({}, {})'.format(a, b))
    return a * b


MAX = 2

print('Primo insieme di chiamate:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

print('\nSecondo  insieme di chiamate:')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())

print('\nPulizia della cache:')
expensive.cache_clear()
print(expensive.cache_info())

print('\nTerzo insieme di chiamate:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())
