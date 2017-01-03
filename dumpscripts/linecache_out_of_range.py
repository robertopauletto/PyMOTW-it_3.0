# linecache_out_of_range.py

import linecache
from linecache_data import *

filename = make_tempfile()

# La cache ritorna sempre una stringa, ed usa
# una stringa vuota per indicare una riga che
# non esiste.
not_there = linecache.getline(filename, 500)
print('NON QUI: {!r} comprende {} caratteri'.format(
    not_there, len(not_there)))

cleanup(filename)
