# contextlib_exitstack_enter_context_errors.py

from contextlib_context_managers import *


def variable_stack(n):
    with contextlib.ExitStack() as stack:
        for i in n:
            stack.enter_context(i)


print('Nessun errore:')
variable_stack([
    HandleError(1),
    PassError(2),
])

print('\nErrore alla fine dello stack di contesti:')
variable_stack([
    HandleError(1),
    HandleError(2),
    ErrorOnExit(3),
])

print('\nErrore nel mezzo dello stack di contesti:')
variable_stack([
    HandleError(1),
    PassError(2),
    ErrorOnExit(3),
    HandleError(4),
])

try:
    print('\nErrore ignorato:')
    variable_stack([
        PassError(1),
        ErrorOnExit(2),
    ])
except RuntimeError:
    print('errore gestito al di fuori del contesto')
