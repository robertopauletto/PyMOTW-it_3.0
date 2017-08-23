# pathlib_parents.py

import pathlib

p = pathlib.PurePosixPath('/usr/local/lib')

print('genitore: {}'.format(p.parent))

print('\ngerarchia:')
for up in p.parents:
    print(up)
