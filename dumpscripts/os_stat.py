# os_stat.py

import os
import sys
import time

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

stat_info = os.stat(filename)

print('os.stat({}):'.format(filename))
print('  Dimensione     :', stat_info.st_size)
print('  Permessi       :', oct(stat_info.st_mode))
print('  Proprietario   :', stat_info.st_uid)
print('  Dispositivo    :', stat_info.st_dev)
print('  Creato         :', time.ctime(stat_info.st_ctime))
print('  Ultima modifica:', time.ctime(stat_info.st_mtime))
print('  Ultimo accesso :', time.ctime(stat_info.st_atime))
