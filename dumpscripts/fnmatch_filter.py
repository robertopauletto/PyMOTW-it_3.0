# fnmatch_filter.py

import fnmatch
import os
import pprint

pattern = 'fnmatch_*.py'
print('Modello :', pattern)

files = os.listdir('.')

print('\nFile   :')
pprint.pprint(files)

print('\nCorrispondenze :')
pprint.pprint(fnmatch.filter(files, pattern))
