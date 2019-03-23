# sys_getsizeof_object.py

import sys


class WithoutAttributes:
    pass


class WithAttributes:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return


without_attrs = WithoutAttributes()
print('Senza attributi (WithoutAttributes):', sys.getsizeof(without_attrs))

with_attrs = WithAttributes()
print('Con attributi (WithAttributes):', sys.getsizeof(with_attrs))
