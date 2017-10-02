# pathlib_unlink.py

import pathlib

p = pathlib.Path('toccato')

p.touch()

print('esiste prima della rimozione:', p.exists())

p.unlink()

print('esiste dopo la rimozione:', p.exists())
