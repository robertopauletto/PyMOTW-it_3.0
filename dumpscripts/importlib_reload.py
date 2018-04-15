# importlib_reload.py

import importlib


m1 = importlib.import_module('esempio.submodule')
print(m1)

m2 = importlib.reload(m1)
print(m1 is m2)
