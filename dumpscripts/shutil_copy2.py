from shutil import *
import os
import time

def show_file_info(filename):
    stat_info = os.stat(filename)
    print '\tModo      :', stat_info.st_mode
    print '\tCreato    :', time.ctime(stat_info.st_ctime)
    print '\tAccesso   :', time.ctime(stat_info.st_atime)
    print '\tModificato:', time.ctime(stat_info.st_mtime)

os.mkdir('esempio')
print 'SORGENTE:'
show_file_info('shutil_copy2.py')
copy2('shutil_copy2.py', 'esempio')
print 'DESTIN:'
show_file_info('esempio/shutil_copy2.py')
