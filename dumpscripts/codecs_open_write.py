# codecs_open_write.py

from codecs_to_hex import to_hex

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print('Scrittura verso', filename)
with codecs.open(filename, mode='w', encoding=encoding) as f:
    f.write('français')

# Determina il raggruppamento di byte da usare per to_hex()
nbytes = {
    'utf-8': 1,
    'utf-16': 2,
    'utf-32': 4,
}.get(encoding, 1)

# Mostra i byte raw nel file
print('Contenuto del file:')
with open(filename, mode='rb') as f:
    print(to_hex(f.read(), nbytes))
