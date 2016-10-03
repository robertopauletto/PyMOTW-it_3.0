# itertools_permutations.py

from itertools import *


def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()

print('Tutte le permutazioni:\n')
show(permutations('abcd'))

print('Coppie:\n')
show(permutations('abcd', r=2))
