# ospath_expandvars.py

import os.path
import os

os.environ['MIAVAR'] = 'VALORE'

print(os.path.expandvars('/percorso/a/$MIAVAR'))
