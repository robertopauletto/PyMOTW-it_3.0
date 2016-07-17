from codecs_to_hex import to_hex

import codecs
import sys

encoding = sys.argv[1]
filename = encoding + '.txt'

print 'Scrittura verso', filename
with codecs.open(filename, mode='wt', encoding=encoding) as f:
    f.write(u'pi: \u03c0')

# Determina il raggruppamento di byte grouping da usare per to_hex()
nbytes = { 'utf-8':1,
           'utf-16':2,
           'utf-32':4,
           }.get(encoding, 1) 

# Mostra i byte raw nel file
print 'Contenuto del file:'
with open(filename, mode='rt') as f:
    print to_hex(f.read(), nbytes)