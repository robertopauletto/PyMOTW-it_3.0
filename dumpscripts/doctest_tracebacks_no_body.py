#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def this_raises():
    """Questa funzione solleva sempre una eccezione

    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: L'errore è qui
    """
    raise RuntimeError("L'errore è qui")