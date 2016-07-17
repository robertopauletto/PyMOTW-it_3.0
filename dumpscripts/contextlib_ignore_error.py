# contextlib_ignore_error.py

import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'L\'operazione è fallita a causa di uno stato esistente'
    )


try:
    # idempotenza: https://it.wikipedia.org/wiki/Idempotenza
    print('si prova una operazione non-idempotente')
    non_idempotent_operation()
    print('successo!')
except NonFatalError:
    pass

print('finito')
