# pdb_interact.py

import pdb


def f():
    l = ['a', 'b']
    m = 9
    n = 5
    print(l, m , n)


if __name__ == '__main__':
    pdb.set_trace()
    f()
