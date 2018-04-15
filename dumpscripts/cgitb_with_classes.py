# cgitb_with_classes.py

import cgitb
cgitb.enable(format='text', context=12)


class BrokenClass:
    """Questa classe ha un errore
    """

    def __init__(self, a, b):
        """Cautela nel passare argomenti qui..
        """
        self.a = a
        self.b = b
        self.c = self.a * self.b
        # Un commento
        # veramente
        # lungo
        # va
        # qui.
        self.d = self.a / self.b
        return

o = BrokenClass(1, 0)
