# doctest_private_tests.py

import doctest_private_tests_external

__test__ = {
    'nummeri': """
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",

    'stringhe': """
>>> my_function('a', 3)
'aaa'

>>> my_function(3, 'a')
'aaa'
""",

    'esterni': doctest_private_tests_external,
}


def my_function(a, b):
    """Returns a * b
    """
    return a * b
