# ospath_splitext.py

import os.path

PATHS = [
    'nomefile.txt',
    'nomefile',
    '/percorso/a/nomefile.txt',
    '/',
    '',
    'mio-filecompresso.tar.gz',
    'no-estensione.',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))
