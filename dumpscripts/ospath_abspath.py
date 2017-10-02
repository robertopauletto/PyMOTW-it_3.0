# ospath_abspath.py

import os
import os.path

os.chdir('/usr')

PATHS = [
    '.',
    '..',
    './uno/due/tre',
    '../uno/due/tre',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.abspath(path)))
