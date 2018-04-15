# importlib_submodule.py

import importlib

pkg_loader = importlib.find_loader('esempio')
pkg = pkg_loader.load_module()

loader = importlib.find_loader('submodule', pkg.__path__)
print('Caricatore:', loader)

m = loader.load_module()
print('Modulo:', m)
