# tarfile_getmember.py

import tarfile
import time

with tarfile.open('esempio.tar', 'r') as t:
    for filename in [ 'LEGGIMI.txt', 'nonqui.txt' ]:
        try:
            info = t.getmember(filename)
        except KeyError:
            print("ERROE:  {} non trovato nell'archivio tar".format(
                filename))
        else:
            print("{} è {:d} byte".format(
                info.name, info.size))
