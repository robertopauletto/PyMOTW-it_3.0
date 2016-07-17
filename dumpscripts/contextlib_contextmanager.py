# contextlib_contextmanager.py

import contextlib


@contextlib.contextmanager
def make_context():
    print('  in entrata')
    try:
        yield {}
    except RuntimeError as err:
        print('  ERRORE:', err)
    finally:
        print('  in uscita')

print('Normale:')
with make_context() as value:
    print('    dentro l\'istruzione with:', value)

print('\nErrore gestito:')
with make_context() as value:
    raise RuntimeError('si mostra un esempio di gestione di un errore')

print('\nErrore non gestito:')
with make_context() as value:
    raise ValueError('questa eccezione non è gestita')
