#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def this_raises():
    """Questa funzione solleva sempre una eccezione

    >>> this_raises()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/no/such/path/doctest_tracebacks.py", line 14, in this_raises
        raise RuntimeError("L'errore è qui")
    RuntimeError: L'errore è qui
    """
    raise RuntimeError("L'errore è qui")