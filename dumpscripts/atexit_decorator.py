# atexit_decorator.py

import atexit


@atexit.register
def all_done():
    print('all_done()')


print('partenza programma principale')
