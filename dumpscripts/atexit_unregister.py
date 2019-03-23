# atexit_unregister.py

import atexit


def my_cleanup(name):
    print('my_cleanup({})'.format(name))


atexit.register(my_cleanup, 'primo')
atexit.register(my_cleanup, 'secondo')
atexit.register(my_cleanup, 'terzo')

atexit.unregister(my_cleanup)
