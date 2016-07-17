# contextlib_contextmanager_decorator.py

import contextlib


@contextlib.contextmanager
def make_context():
    print('  in entrata')
    try:
        # Trattiene il controllo, ma non un valore, poichè qualasiasi
        # valore trattenuto non è disponibile quando il gestore di
        # contesto viene usato come decoratore.
        yield
    except RuntimeError as err:
        print('  ERRORE:', err)
    finally:
        print('  in uscita')


@make_context()
def normal():
    print('    dentro l\'istruzione with:')


@make_context()
def throw_error(err):
    raise err


print('Normale:')
normal()

print('\nErrore gestito:')
throw_error(RuntimeError('si mostra un esempio di gestione di un errore'))

print('\nErrore non gestito:')
throw_error(ValueError('questa eccezione non è gestita'))
