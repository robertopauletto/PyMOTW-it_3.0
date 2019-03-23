# atexit_unregister_not_registered.py

import atexit


def my_cleanup(name):
    print('my_cleanup({})'.format(name))


if False:
    atexit.register(my_cleanup, 'mai registrato')

atexit.unregister(my_cleanup)
