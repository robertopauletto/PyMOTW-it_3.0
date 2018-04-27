# doctest_tracebacks_no_body.py

def this_raises():
    """Questa funzione solleva sempre una eccezione

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: L'errore è qui

    >>> this_raises()
    Traceback (innermost last):
    RuntimeError: L'errore è qui
    """
    raise RuntimeError("L'errore è qui")
