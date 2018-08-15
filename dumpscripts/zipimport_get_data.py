# zipimport_get_data.py

import sys
sys.path.insert(0, 'esempio_zipimport.zip')

import os
import pacchetto_esempio
print(pacchetto_esempio.__file__)
data = pacchetto_esempio.__loader__.get_data(
    'pacchetto_esempio/README.txt')
print(data.decode('utf-8'))
