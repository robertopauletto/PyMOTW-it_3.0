import linecache
from linecache_data import *

filename = make_tempfile()

# La cache ritorna sempre una stringa, ed usa
# una stringa vuota per indicare una riga che
# non esiste.
non_qui = linecache.getline(filename, 500)
print "\nNON QUI: '%s' comprende %d caratteri" %  (non_qui, len(non_qui))

cleanup(filename)
