# atexit_simple.py

import atexit


def all_done():
    print('all_done()')


print('In registrazione')
atexit.register(all_done)
print('Registrato')
