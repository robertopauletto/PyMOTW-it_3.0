# doctest_blankline.py

def double_space(lines):
    """Stampa un elenco di righe con doppia spaziatura

    >>> double_space(['Riga uno.', 'Riga due.'])
    Riga uno.
    <BLANKLINE>
    Riga due.
    <BLANKLINE>
    """
    for l in lines:
        print(l)
        print()
