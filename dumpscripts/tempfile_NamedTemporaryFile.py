import os
import tempfile

temp = tempfile.NamedTemporaryFile()
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    # Elimina il file automaticamente
    temp.close()
print 'Esiste dopo la chiusura:', os.path.exists(temp.name)
