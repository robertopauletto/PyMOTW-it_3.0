# shutil_copy.py

import glob
import os
import shutil

os.mkdir('example')
print('PRIMA:', glob.glob('example/*'))

shutil.copy('shutil_copy.py', 'example')

print('DOPO :', glob.glob('example/*'))
