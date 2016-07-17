from shutil import *
from commands import *
import os

f = open('file_da_cambiare.txt', 'wt')
f.write('contenuto')
f.close()
os.chmod('file_da_cambiare.txt', 0444)

print 'PRIMA:', getstatus('file_da_cambiare.txt')
copymode('shutil_copymode.py', 'file_da_cambiare.txt')
print 'DOPO :', getstatus('file_da_cambiare.txt')
