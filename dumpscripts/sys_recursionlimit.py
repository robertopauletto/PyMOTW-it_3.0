# sys_recursionlimit.py

import sys

print('Limite iniziale', sys.getrecursionlimit())

sys.setrecursionlimit(10)

print('Limite modificato', sys.getrecursionlimit())


def generate_recursion_error(i):
    print('generate_recursion_error({})'.format(i))
    generate_recursion_error(i + 1)


try:
    generate_recursion_error(1)
except RuntimeError as err:
    print('Eccezione catturata:', err)
