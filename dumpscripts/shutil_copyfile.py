from shutil import *
from glob import glob

print 'PRIMA:', glob('shutil_copyfile.*')
copyfile('shutil_copyfile.py', 'shutil_copyfile.py.copy')
print 'DOPO :', glob('shutil_copyfile.*')
