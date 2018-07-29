# zipfile_namelist.py

import zipfile

with zipfile.ZipFile('esempio.zip', 'r') as zf:
    print(zf.namelist())
