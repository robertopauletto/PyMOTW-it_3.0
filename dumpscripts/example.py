# example.py
# Questo commento appare per primo
# e si trova du due righe.

# Questo commento non viene visualizzato nel risultato di getcomments().

"""File di esempio che serve come base per gli esempi di ispezione.
"""


def module_level_function(arg1, arg2='default', *args, **kwargs):
    """Questa funzione viene dichiarata nel modulo."""
    local_variable = arg1 * 2
    return local_variable


class A(object):
    """La classe A."""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        "Ritorna il nome dell'istanza"
        return self.name


instance_of_a = A('sample_instance')


class B(A):
    """Questa è la classe B.
    Derivata da A.
    """

    # Questo metodo non fa parte di A.
    def do_something(self):
        """Esegue qualche operazione"""

    def get_name(self):
        "Sovrascrive la versione da A"
        return 'B(' + self.name + ')'
