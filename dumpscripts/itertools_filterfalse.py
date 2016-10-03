# itertools_filterfalse.py

from itertools import *


def check_item(x):
    print('Verifica:', x)
    return x < 1

for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print('Trattengo:', i)
