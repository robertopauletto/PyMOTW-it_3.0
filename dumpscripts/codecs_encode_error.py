import codecs
import sys

error_handling = sys.argv[1]

text = u'pi: \u03c0'

try:
    # Salva i dati, codificati in ASCII, usando la modalita'
    # di gestione errori specificata da riga di comand.
    with codecs.open('encode_error.txt', 'w',
                     encoding='ascii',
                     errors=error_handling) as f:
        f.write(text)
        
except UnicodeEncodeError, err:
    print 'ERRORE:', err
    
else:
    # Se non ci sono errori scrivendo sul file,
    # si mostra il suo contenuto
    with open('encode_error.txt', 'rb') as f:
        print 'Contenuto del file:', repr(f.read())