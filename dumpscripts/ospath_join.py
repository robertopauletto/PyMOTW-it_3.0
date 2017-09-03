# ospath_join.py

import os.path

PATHS = [
    ('uno', 'due', 'tre'),
    ('/', 'uno', 'due', 'tre'),
    ('/uno', '/due', '/tre'),
]

for parts in PATHS:
    print('{} : {!r}'.format(parts, os.path.join(*parts)))

