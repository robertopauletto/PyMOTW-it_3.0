# pathlib_symlink_to.py

import pathlib

p = pathlib.Path('coll_di_esempio')

p.symlink_to('pathlib_symlink_to.py')

print(p)
print(p.resolve().name)
