# getpass_defaults.py

import getpass

try:
    p = getpass.getpass()
except Exception as err:
    print('ERRORE:', err)
else:
    print('Hai digitato:', p)
