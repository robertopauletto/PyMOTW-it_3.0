===============================
 Come Usare doctest_in_help.py
===============================

Questa libreria è molto semplice, visto che usa una sola funzione chiamata
``my_function()``.

Numeri
=======

``my_function()`` ritorna il prodotto dei suoi parametro.  Per i numeri,
quel valore equivale ad usare l'operatore ``*``.

::

    >>> from doctest_in_help import my_function
    >>> my_function(2, 3)
    6

Funziona anche con valori a virgola mobile.

::

    >>> my_function(2.0, 3)
    6.0

Non-Numeri
===========

Visto che ``*`` è definito anche su tipi di dato diversi dai numeri,
``my_function()`` funziona allo stesso mod se uno dei parametri è una
stringa, lista, o tuple.

::

    >>> my_function('a', 3)
    'aaa'

    >>> my_function(['A', 'B', 'C'], 2)
    ['A', 'B', 'C', 'A', 'B', 'C']
    
    