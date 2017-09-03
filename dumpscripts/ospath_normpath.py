# ospath_normpath.py

import os.path

PATHS = [
    'uno//due//tre',
    'uno/./due/./tre',
    'uno/../alt/due/tre',
]

for path in PATHS:
    print('{!r:>22} : {!r}'.format(path, os.path.normpath(path)))

