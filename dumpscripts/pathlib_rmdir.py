# pathlib_rmdir.py

import pathlib

p = pathlib.Path('dir_esempio')

print('Rimozione di {}'.format(p))
p.rmdir()
