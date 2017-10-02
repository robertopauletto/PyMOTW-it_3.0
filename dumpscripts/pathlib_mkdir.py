# pathlib_mkdir.py

import pathlib

p = pathlib.Path('dir_esempio')

print('Creazione di {}'.format(p))
p.mkdir()
