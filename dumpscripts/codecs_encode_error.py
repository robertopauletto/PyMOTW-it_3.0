# codecs_encode_error.py

import codecs
import sys

error_handling = sys.argv[1]

text = 'français'

try:
    # Salva i dati, codificati come ASCII, usando la modalità di gestione
    # errori specificata da riga di comando
    with codecs.open('encode_error.txt', 'w',
                     encoding='ascii',
                     errors=error_handling) as f:
        f.write(text)

except UnicodeEncodeError as err:
    print('ERRORE:', err)

else:
    # Se non ci sono errori nella scrittura al file
    # mostra il contenuto
    with open('encode_error.txt', 'rb') as f:
        print('Contenuto del file: {!r}'.format(f.read()))
