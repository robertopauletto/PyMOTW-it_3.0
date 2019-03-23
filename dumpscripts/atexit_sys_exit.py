# atexit_sys_exit.py
import atexit
import sys


def all_done():
    print('all_done()')


print('In registrazione')
atexit.register(all_done)
print('Registrato')

print('In uscita...')
sys.exit()
