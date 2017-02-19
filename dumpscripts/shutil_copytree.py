# shutil_copytree.py

import glob
import pprint
import shutil

print('PRIMA:')
pprint.pprint(glob.glob('/tmp/example/*'))

shutil.copytree('../shutil', '/tmp/example')

print('\nDOPO:')
pprint.pprint(glob.glob('/tmp/example/*'))
