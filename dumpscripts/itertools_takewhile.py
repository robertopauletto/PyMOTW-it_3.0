# itertools_takewhile.py

from itertools import *


def should_take(x):
    print('Verifica:', x)
    return x < 2

for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Trattengo:', i)
