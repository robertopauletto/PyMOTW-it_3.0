# doctest_blankline_fail.py

def double_space(lines):
    """Stampa un elenco di righe con doppia riga di  spaziatura

    >>> double_space(['Riga uno.', 'Riga due.'])
    Riga uno.

    Riga due.

    """
    for l in lines:
        print(l)
        print()
