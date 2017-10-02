# pathlib_stat.py

import pathlib
import sys
import time

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

p = pathlib.Path(filename)
stat_info = p.stat()

print('{}:'.format(filename))
print('  Dimnsione      :', stat_info.st_size)
print('  Permessi       :', oct(stat_info.st_mode))
print('  Proprietario   :', stat_info.st_uid)
print('  Dispositivo    :', stat_info.st_dev)
print('  Creato         :', time.ctime(stat_info.st_ctime))
print('  Ultima modifica:', time.ctime(stat_info.st_mtime))
print('  Ultimo accesso :', time.ctime(stat_info.st_atime))
