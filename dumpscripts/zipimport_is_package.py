# zipimport_is_package.py

import zipimport

importer = zipimport.zipimporter('esempio_zipimport.zip')
for name in ['zipimport_is_package', 'pacchetto_esempio']:
    print(name, importer.is_package(name))
