import linecache

# Cerca il modulo linecache, usando
# la ricerca built-in in sys.path
module_line = linecache.getline('linecache.py', 3)
print '\nMODULO : ', module_line
