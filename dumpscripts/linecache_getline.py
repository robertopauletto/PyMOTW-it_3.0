# linecache_getline.py

import linecache
from linecache_data import *

filename = make_tempfile()

# Estrazione della stessa riga dalla sorgente e dalla cache.
# (Notare che linecache conta da 1)
print('SORGENTE:')
print('{!r}'.format(lorem.split('\n')[4]))
print()
print('CACHE:')
print('{!r}'.format(linecache.getline(filename, 5)))

cleanup(filename)
