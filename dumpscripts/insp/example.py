#!/usr/bin/env python

# Questo commento compare per primo
# e si sviluppa su due righe

# Questo commento non viene mostrato nell'output di getcomments()

"""File di esempio che funge da base per gli esempi di inspect."""

def module_level_function(arg1, arg2='default', *args, **kwargs):
    """Questa funzione viene dichiarata a livello di modulo."""
    local_variable = arg1
    return

class A(object):
    """La classe A."""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Ritorna il nome dell'istanza."
        return self.name

instance_of_a = A('istanza_di_esempio')

class B(A):
    """Questa e' la classe B.
    Derivata da A.
    """

    # Questo metodo non fa parte di A.
    def do_something(self):
        """Fa qualche cosa"""
        pass

    def get_name(self):
        "Versione da A sovrascritta"
        return 'B(' + self.name + ')'