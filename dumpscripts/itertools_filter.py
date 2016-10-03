# itertools_filter.py

from itertools import *


def check_item(x):
    print('Verifica:', x)
    return x < 1

for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Trattengo:', i)
