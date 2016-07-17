import codecs
import sys

from codecs_to_hex import to_hex

error_handling = sys.argv[1]

text = u'pi: \u03c0'
print 'Originale         :', repr(text)

# Salva i dati con una codifica   
with codecs.open('decode_error.txt', 'w', encoding='utf-16') as f:
    f.write(text)

# Scarica i dati dal file
with open('decode_error.txt', 'rb') as f:
    print 'Contenuto del file:', to_hex(f.read(), 1)

# Tenta di leggere i dati con la codifica errata
with codecs.open('decode_error.txt', 'r',
                 encoding='utf-8',
                 errors=error_handling) as f:
    try:
        data = f.read()
    except UnicodeDecodeError, err:
        print 'ERRORE:', err
    else:
        print 'Letto        :', repr(data)