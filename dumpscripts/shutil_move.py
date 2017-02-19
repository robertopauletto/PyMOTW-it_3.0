# shutil_move.py

import glob
import shutil

with open('example.txt', 'wt') as f:
    f.write('contents')

print('PRIMA: ', glob.glob('example*'))

shutil.move('example.txt', 'example.out')

print('DOPO : ', glob.glob('example*'))
