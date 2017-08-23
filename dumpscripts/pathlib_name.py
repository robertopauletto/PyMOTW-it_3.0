# pathlib_name.py

import pathlib

p = pathlib.PurePosixPath('./source/pathlib/pathlib_name.py')
print('percorso   : {}'.format(p))
print('nome       : {}'.format(p.name))
print('suffisso   : {}'.format(p.suffix))
print('radice nome: {}'.format(p.stem))
