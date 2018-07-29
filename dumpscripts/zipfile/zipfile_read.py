# zipfile_read.py

import zipfile

with zipfile.ZipFile('esempio.zip') as zf:
    for filename in ['LEGGIMI.txt', 'nonqui.txt']:
        try:
            data = zf.read(filename)
        except KeyError:
            print('ERRORE: Non trovato {} nel file zip'.format(
                filename))
        else:
            print(filename, ':')
            print(data)
        print()
