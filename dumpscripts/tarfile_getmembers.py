# tarfile_getmembers.py

import tarfile
import time

with tarfile.open('example.tar', 'r') as t:
    for member_info in t.getmembers():
        print(member_info.name)
        print('  Modificato:', time.ctime(member_info.mtime))
        print('  Modalità  :', oct(member_info.mode))
        print('  Tipo      :', member_info.type)
        print('  Dimensione:', member_info.size, 'byte')
        print()
