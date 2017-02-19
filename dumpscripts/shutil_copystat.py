# shutil_copystat.py

import os
import shutil
import time


def show_file_info(filename):
    stat_info = os.stat(filename)
    print('  Modalità  :', oct(stat_info.st_mode))
    print('  Creato    :', time.ctime(stat_info.st_ctime))
    print('  Accesso   :', time.ctime(stat_info.st_atime))
    print('  Modificato:', time.ctime(stat_info.st_mtime))


with open('file_da_cambiare.txt', 'wt') as f:
    f.write('contenuto')
os.chmod('file_da_cambiare.txt', 0o444)

print('PRIMA:')
show_file_info('file_da_cambiare.txt')

shutil.copystat('shutil_copystat.py', 'file_da_cambiare.txt')

print('DOPO:')
show_file_info('file_da_cambiare.txt')
