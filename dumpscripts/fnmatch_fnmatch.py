# fnmatch_fnmatch.py

import fnmatch
import os

pattern = 'fnmatch_*.py'
print('Modello :', pattern)
print()

files = os.listdir('.')
for name in files:
    print('Nome file: {:<25} {}'.format(
        name, fnmatch.fnmatch(name, pattern)))
