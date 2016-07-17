# contextlib_suppress.py

import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError(
        'L\'operazione è fallita a causa di uno stato esistente'
    )


with contextlib.suppress(NonFatalError):
    # idempotenza: https://it.wikipedia.org/wiki/Idempotenza
    print('si prova una operazione non-idempotente')
    non_idempotent_operation()
    print('successo!')

print('finito')
