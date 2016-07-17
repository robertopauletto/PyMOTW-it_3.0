from shutil import *
import os

os.mkdir('esempio')
print 'PRIMA:', os.listdir('esempio')
copy('shutil_copy.py', 'esempio')
print 'DOPO :', os.listdir('esempio')
