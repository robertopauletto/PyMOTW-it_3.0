# shutil_copy2.py

import os
import shutil
import time


def show_file_info(filename):
    stat_info = os.stat(filename)
    print('  Modalità  :', oct(stat_info.st_mode))
    print('  Creato    :', time.ctime(stat_info.st_ctime))
    print('  Accesso   :', time.ctime(stat_info.st_atime))
    print('  Modificato:', time.ctime(stat_info.st_mtime))


os.mkdir('example')
print('SORGENTE:')
show_file_info('shutil_copy2.py')

shutil.copy2('shutil_copy2.py', 'example')

print('DESTINAZIONE:')
show_file_info('example/shutil_copy2.py')
