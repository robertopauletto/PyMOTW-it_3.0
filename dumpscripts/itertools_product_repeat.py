# itertools_product_repeat.py

from itertools import *


def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()


print('Ripetizione 2:\n')
show(list(product(range(3), repeat=2)))

print('Ripetizione 3:\n')
show(list(product(range(3), repeat=3)))
