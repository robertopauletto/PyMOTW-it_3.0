import doctest_private_tests_external

__test__ = {
    'numbers':"""
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",

    'strings':"""
>>> my_function('a', 3)
'aaa'

>>> my_function(3, 'a')
'aaa'
""",

    'external':doctest_private_tests_external,
    
    }

def my_function(a, b):
    """Ritorna a * b
    """
    return a * b