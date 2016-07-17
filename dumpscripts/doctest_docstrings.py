#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#!/usr/bin/env python
# encoding: utf-8

"""I test possono apparire in una qualsiasi docstring all'interno del modulo

I test a livello di modulo oltrepassano i confini di classi e funzioni

>>> A('a') == B('b')
False
"""

class A(object):
    """Semplice classe.

    >>> A('instance_name').name
    'instance_name'
    """
    def __init__(self, name):
        self.name = name
    def method(self):
        """Returns an unusual value.

        >>> A('name').method()
        'eman'
        """
        return ''.join(reversed(list(self.name)))

class B(A):
    """Un'altra semplice classe
        
    >>> B('different_name').name
    'different_name'
    """