# ospath_split.py

import os.path

PATHS = [
    '/uno/due/tre',
    '/uno/due/tre/',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.split(path)))
