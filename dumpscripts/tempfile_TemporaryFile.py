import os
import tempfile

print 'Creazione di un nome di file:'
filename = '/tmp/indovina_il_nome.%s.txt' % os.getpid()
temp = open(filename, 'w+b')
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    temp.close()
    # Elimina espressamente il file temporaneo
    os.remove(filename)

print
print 'TemporaryFile:'
temp = tempfile.TemporaryFile()
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    # Elimina il file automaticamente
    temp.close()
