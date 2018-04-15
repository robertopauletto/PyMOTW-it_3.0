# importlib_import_module.py

import importlib


m1 = importlib.import_module('esempio.submodule')
print(m1)

m2 = importlib.import_module('.submodule', package='esempio')
print(m2)

print(m1 is m2)
