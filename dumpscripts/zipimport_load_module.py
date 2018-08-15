# zipimport_load_module.py

import zipimport

importer = zipimport.zipimporter('esempio_zipimport.zip')
module = importer.load_module('zipimport_get_code')
print('Nome       :', module.__name__)
print('Caricatore :', module.__loader__)
print('Codice     :', module.code)
