# contextlib_exitstack_pop_all.py

import contextlib

from contextlib_context_managers import *


def variable_stack(contexts):
    with contextlib.ExitStack() as stack:
        for c in contexts:
            stack.enter_context(c)
        # Ritorna il metodo  close() del nuovo stakc come funzione
        # di pulizia.
        return stack.pop_all().close
    # Ritorna esplicitamente None. Indica che ExitStack potrebbe non essere
    # inizializzato in modo pulito ma quella pulizia è già stata fatta
    return None


print('Nessun errore:')
cleaner = variable_stack([
    HandleError(1),
    HandleError(2),
])
cleaner()

print('\nErrore gestito nella costruzione dello stack dei gestori di contesto:')
try:
    cleaner = variable_stack([
        HandleError(1),
        ErrorOnEnter(2),
    ])
except RuntimeError as err:
    print('errore catturato {}'.format(err))
else:
    if cleaner is not None:
        cleaner()
    else:
        print('nessun pulitore ritornato')

print('\nrrore gestito nella costruzione dello stack dei gestori di contesto:')
try:
    cleaner = variable_stack([
        PassError(1),
        ErrorOnEnter(2),
    ])
except RuntimeError as err:
    print('errore catturato {}'.format(err))
else:
    if cleaner is not None:
        cleaner()
    else:
        print('nessun pulitore ritornato')
