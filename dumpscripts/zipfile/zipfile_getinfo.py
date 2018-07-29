# zipfile_getinfo.py

import zipfile

with zipfile.ZipFile('esempio.zip') as zf:
    for filename in ['LEGGIMI.txt', 'nonqui.txt']:
        try:
            info = zf.getinfo(filename)
        except KeyError:
            print('ERRORE: Non trovato {} nel file zip'.format(
                filename))
        else:
            print('{} è {} byte'.format(
                info.filename, info.file_size))
