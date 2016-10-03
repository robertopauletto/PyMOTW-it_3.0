# fnmatch_fnmatchcase.py

import fnmatch
import os

pattern = 'FNMATCH_*.PY'
print('Modello :', pattern)
print()

files = os.listdir('.')

for name in files:
    print('Nome file: {:<25} {}'.format(
        name, fnmatch.fnmatchcase(name, pattern)))
