# linecache_missing_file.py
import linecache

# Gli errori sono nascosti anche se linecache non trova il file
no_such_file = linecache.getline(
    'questo_file_ancora_non_esiste.txt', 1,
)
print('NESSUN FILE: {!r}'.format(no_such_file))
