# zipimport_get_code.py

import zipimport

importer = zipimport.zipimporter('esempio_zipimport.zip')
code = importer.get_code('zipimport_get_code')
print(code)
