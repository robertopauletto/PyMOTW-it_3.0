# doctest_docstrings.py

"""I test possono apparire in una qualsiasi docstring all'interno del modulo

I test a livello di modulo oltrepassano i confini di classi e funzioni

>>> A('a') == B('b')
False
"""


class A:
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
        return ''.join(reversed(self.name))


class B(A):
    """Un'altra semplice classe

    >>> B('different_name').name
    'different_name'"""
