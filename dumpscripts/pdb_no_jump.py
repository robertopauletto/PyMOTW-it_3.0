# pdb_no_jump.py

#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#


def f(n):
    if n < 0:
        raise ValueError('Invalid n: %s' % n)
    result = []
    j = 0
    for i in range(n):
        j = i * n + j
        j += n
        result.append(j)
    return result


if __name__ == '__main__':
    try:
        print(f(5))
    finally:
        print('Sempre stampato')

    try:
        print(f(-5))
    except:
        print('Nessun errore')
    else:
        print('Nessun errore')

    print('Ultima istruzione')
