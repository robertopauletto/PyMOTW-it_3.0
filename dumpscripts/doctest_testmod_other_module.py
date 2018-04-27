# doctest_testmod_other_module.py

import doctest_simple

if __name__ == '__main__':
    import doctest
    doctest.testmod(doctest_simple)
