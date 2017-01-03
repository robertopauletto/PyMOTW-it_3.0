# linecache_empty_line.py

import linecache
from linecache_data import *

filename = make_tempfile()

# Le righe vuote includono un ritorno a capo
print('VUOTE : {!r}'.format(linecache.getline(filename, 8)))
