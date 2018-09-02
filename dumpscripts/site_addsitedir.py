# site_addsitedir.py

import site
import os
import sys

script_directory = os.path.dirname(__file__)
module_directory = os.path.join(script_directory, sys.argv[1])

try:
    import miomodulo
except ImportError as err:
    print('Non posso importare mioodulo:', err)

print()
before_len = len(sys.path)
site.addsitedir(module_directory)
print('Nuovi percorsi:')
for p in sys.path[before_len:]:
    print(p.replace(os.getcwd(), '.'))  # nome directory abbreviato

print()
import miomodulo
