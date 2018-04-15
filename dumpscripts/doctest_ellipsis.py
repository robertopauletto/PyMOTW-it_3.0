# doctest_ellipsis.py

class MyClass:
    pass


def unpredictable(obj):
    """Ritorna una nuova lista che contiene obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return [obj]
