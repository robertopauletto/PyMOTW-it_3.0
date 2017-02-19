# shutil_copyfile.py

import glob
import shutil

print('PRIMA:', glob.glob('shutil_copyfile.*'))

shutil.copyfile('shutil_copyfile.py', 'shutil_copyfile.py.copy')

print('DOPO:', glob.glob('shutil_copyfile.*'))
