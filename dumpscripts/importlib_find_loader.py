# importlib_find_loader.py

import importlib

loader = importlib.find_loader('esempio')
print('Caricatore:', loader)

m = loader.load_module()
print('Modulo:', m)
