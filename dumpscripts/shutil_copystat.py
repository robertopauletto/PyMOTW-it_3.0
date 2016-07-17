from shutil import *
import os
import time

def show_file_info(filename):
    stat_info = os.stat(filename)
    print '\tModo      :', stat_info.st_mode
    print '\tCreato    :', time.ctime(stat_info.st_ctime)
    print '\tAccesso   :', time.ctime(stat_info.st_atime)
    print '\tModificato:', time.ctime(stat_info.st_mtime)

f = open('file_da_cambiare.txt', 'wt')
f.write('contenuto')
f.close()
os.chmod('file_da_cambiare.txt', 0444)

print 'PRIMA:'
show_file_info('file_da_cambiare.txt')
copystat('shutil_copystat.py', 'file_da_cambiare.txt')
print 'DOPO :'
show_file_info('file_da_cambiare.txt')
