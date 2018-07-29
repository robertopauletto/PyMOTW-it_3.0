# zipfile_pyzipfile.py

import sys
import zipfile

if __name__ == '__main__':
    with zipfile.PyZipFile('pyzipfile.zip', mode='w') as zf:
        zf.debug = 3
        print('Aggiungo file python')
        zf.writepy('.')
    for name in zf.namelist():
        print(name)

    print()
    sys.path.insert(0, 'pyzipfile.zip')
    import zipfile_pyzipfile
    print('Importati da:', zipfile_pyzipfile.__file__)
