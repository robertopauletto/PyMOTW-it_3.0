# cgitb_exception_properties.py

import cgitb
cgitb.enable(format='text')


class MyException(Exception):
    """Aggiunge proprieta' extra ad una eccezione personalizzata
    """

    def __init__(self, message, bad_value):
        self.bad_value = bad_value
        Exception.__init__(self, message)
        return

raise MyException('Messaggio normale', bad_value=99)
