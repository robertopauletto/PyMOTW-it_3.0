# doctest_normalize_whitespace.py

def my_function(a, b):
    """Ritorna a * b.

    >>> my_function(['A', 'B'], 3)  #doctest: +NORMALIZE_WHITESPACE
    ['A', 'B',
     'A', 'B',
     'A', 'B']

    Questo non corrisponde a causa di spazi extra dopo la [ nella
    lista.

    >>> my_function(['A', 'B'], 2) #doctest: +NORMALIZE_WHITESPACE
    [ 'A', 'B',
      'A', 'B', ]
    """
    return a * b
