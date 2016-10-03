# itertools_dropwhile.py

from itertools import *


def should_drop(x):
    print('Verifica:', x)
    return x < 1

for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Trattengo:', i)
