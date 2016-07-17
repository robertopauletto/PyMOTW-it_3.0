# contextlib_closing.py

import contextlib

class Door(object):
    def __init__(self):
        print('  __init__()')
        self.status = 'aperto'

    def close(self):
        print('  close()')
        self.status = 'chiuso'

print('Esempio Normale:')
with contextlib.closing(Door()) as door:
    print('  dentro l\'istruzione with: {}'.format(door.status))
print('  al di fuori dell\'istruzione with: {}'.format(door.status))


print('\nEsempio di gestione errore:')
try:
    with contextlib.closing(Door()) as door:
        print('  sollevata da dentro l\'istruzione with')
        raise RuntimeError('messaggio di errore')
except Exception as err:
    print('  Si è verificato un errore:', err)
