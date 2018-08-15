# zipimport_find_module.py

import zipimport

importer = zipimport.zipimporter('esempio_zipimport.zip')

for module_name in ['zipimport_find_module', 'non_qui']:
    print(module_name, ':', importer.find_module(module_name))
