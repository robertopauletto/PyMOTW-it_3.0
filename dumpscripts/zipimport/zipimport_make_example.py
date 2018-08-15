# zipimport_make_example.py

import sys
import zipfile

if __name__ == '__main__':
    zf = zipfile.PyZipFile('esempio_zipimport.zip', mode='w')
    try:
        zf.writepy('.')
        zf.write('zipimport_get_source.py')
        zf.write('pacchetto_esempio/README.txt')
    finally:
        zf.close()
    for name in zf.namelist():
        print(name)
