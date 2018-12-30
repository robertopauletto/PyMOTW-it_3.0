# dis_class.py

#!/usr/bin/env python
# encoding: utf-8

import dis


class MyObject:
    """Esempio per dis."""

    CLASS_ATTRIBUTE = 'un qualche valore'

    def __str__(self):
        return 'MyObject({})'.format(self.name)

    def __init__(self, name):
        self.name = name


dis.dis(MyObject)
