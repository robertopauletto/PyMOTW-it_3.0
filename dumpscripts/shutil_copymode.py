# shutil_copymode.py

import os
import shutil
import subprocess

with open('file_da_cambiare.txt', 'wt') as f:
    f.write('contenuto')
os.chmod('file_da_cambiare.txt', 0o444)

print('PRIMA:', oct(os.stat('file_da_cambiare.txt').st_mode))

shutil.copymode('shutil_copymode.py', 'file_da_cambiare.txt')

print('DOPO :', oct(os.stat('file_da_cambiare.txt').st_mode))
