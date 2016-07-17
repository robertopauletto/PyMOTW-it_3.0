import linecache
from linecache_data import *

filename = make_tempfile()

# Le righe vuote includono un ritorno a capo
print '\nVUOTA : "%s"' % linecache.getline(filename, 6)

cleanup(filename)
