# tarfile_getnames.py

import tarfile

with tarfile.open('esempio.tar', 'r') as t:
    print(t.getnames())
