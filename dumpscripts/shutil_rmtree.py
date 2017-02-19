# shutil_rmtree.py

import glob
import pprint
import shutil

print('PRIMA:')
pprint.pprint(glob.glob('/tmp/example/*'))

shutil.rmtree('/tmp/example')

print('\nDOPO:')
pprint.pprint(glob.glob('/tmp/example/*'))
