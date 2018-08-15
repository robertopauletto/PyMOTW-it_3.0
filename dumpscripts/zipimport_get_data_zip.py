# zipimport_get_data_zip.py

import sys
sys.path.insert(0, 'esempio_zipimport.zip')

import os
import pacchetto_esempio
print(pacchetto_esempio.__file__)
data_filename = os.path.join(
    os.path.dirname(pacchetto_esempio.__file__),
    'README.txt',
)
print(data_filename, ':')
print(open(data_filename, 'rt').read())
