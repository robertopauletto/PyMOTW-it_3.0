# ospath_dirname.py

import os.path

PATHS = [
    '/uno/due/tre',
    '/uno/due/tre/',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.dirname(path)))
