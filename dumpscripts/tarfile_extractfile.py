# tarfile_extractfile.py

import tarfile

with tarfile.open('esempio.tar', 'r') as t:
    for filename in [ 'LEGGIMI.txt', 'nonqui.txt' ]:
        try:
            f = t.extractfile(filename)
        except KeyError:
            print("ERROR: {} non trovato nell'archivio tar".format(
                filename))
        else:
            print(filename, ':')
            print(f.read().decode('utf-8'))
