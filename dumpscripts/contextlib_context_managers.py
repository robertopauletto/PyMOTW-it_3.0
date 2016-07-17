# contextlib_context_managers.py

import contextlib


class Tracker:
    "Classe base per i gestori di contesto."

    def __init__(self, i):
        self.i = i

    def msg(self, s):
        print('  {}({}): {}'.format(
            self.__class__.__name__, self.i, s))

    def __enter__(self):
        self.msg('in entrata')


class HandleError(Tracker):
    "Se si riceve una eccezione si tratta come fosse gestita"

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('gestione eccezione {!r}'.format(
                exc_details[1]))
        self.msg('in uscita {}'.format(received_exc))
        # Ritorna un valore booleano che indica se l'eccezione
        # è stata gestita
        return received_exc


class PassError(Tracker):
    "Se si riceve una eccezione, la si propaga."

    def __exit__(self, *exc_details):
        received_exc = exc_details[1] is not None
        if received_exc:
            self.msg('passaggio dell\'eccezione {!r}'.format(
                exc_details[1]))
        self.msg('in uscita')
        # Return False, indicating any exception was not handled.
        return False


class ErrorOnExit(Tracker):
    "Genera una eccezione."

    def __exit__(self, *exc_details):
        self.msg('sollevo un errore')
        raise RuntimeError('da {}'.format(self.i))


class ErrorOnEnter(Tracker):
    "Genera una eccezione."

    def __enter__(self):
        self.msg('sollevo un errore in entrata')
        raise RuntimeError('from {}'.format(self.i))

    def __exit__(self, *exc_info):
        self.msg('in uscita')
