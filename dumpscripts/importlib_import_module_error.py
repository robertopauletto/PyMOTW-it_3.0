# importlib_import_module_error.py

import importlib


try:
    importlib.import_module('esempio.nosuchmodule')
except ImportError as err:
    print('Errore:', err)
