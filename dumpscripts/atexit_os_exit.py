# atexit_os_exit.py

import atexit
import os


def not_called():
    print('Questa non dovrebbe essere chiamata')


print('In registrazione')
atexit.register(not_called)
print('Registrato')

print('In uscita...')
os._exit(0)
