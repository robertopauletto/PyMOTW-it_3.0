# functools_cmp_to_key.py

import functools


class MyObject:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'MyObject({})'.format(self.val)


def compare_obj(a, b):
    """Funzione di confronto vecchio stile.
    """
    print('confronto tra {} e {}'.format(a, b))
    if a.val < b.val:
        return -1
    elif a.val > b.val:
        return 1
    return 0

# Genera una funzione chiave utilizzanod cmp_to_key()
get_key = functools.cmp_to_key(compare_obj)


def get_key_wrapper(o):
    "Funzione wrapper per get_key per consentire le istruzioni print."
    new_key = get_key(o)
    print('key_wrapper({}) -> {!r}'.format(o, new_key))
    return new_key

objs = [MyObject(x) for x in range(5, 0, -1)]

for o in sorted(objs, key=get_key_wrapper):
    print(o)
