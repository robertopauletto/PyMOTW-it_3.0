# zipimport_get_data_nozip.py

import os
import pacchetto_esempio

# Trova la directory contenente il pacchetto
# importato e da lì costruisce il nome per il file di dati
pkg_dir = os.path.dirname(pacchetto_esempio.__file__)
data_filename = os.path.join(pkg_dir, 'README.txt')

# Legge il file e mostra il suo contenuto.
print(data_filename, ':')
print(open(data_filename, 'r').read())
