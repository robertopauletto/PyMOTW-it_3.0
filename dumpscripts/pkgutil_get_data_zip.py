# pkgutil_get_data_zip.py

import pkgutil
import zipfile
import sys

# Crea un file ZIP con il codice dalla directory corrente
# ed il template usando un nome che non appare nel filesystem.locale
with zipfile.PyZipFile('pkgwithdatainzip.zip', mode='w') as zf:
    zf.writepy('pkgwithdata/.')
    zf.write('pkgwithdata/templates/base.html',
             'pkgwithdata/templates/fromzip.html',
             )

# Aggiunge il file ZIP al percorso di importazione.
sys.path.insert(0, 'pkgwithdatainzip.zip')

# Importa pkgwithdata per mostrare che proviene dall'archivio  ZIP.
import pkgwithdata
print('Loading pkgwithdata from', pkgwithdata.__file__)

# Stampa il contenuto del template.
print('\nTemplate:')
data = pkgutil.get_data('pkgwithdata', 'templates/fromzip.html')
print(data.decode('utf-8'))
