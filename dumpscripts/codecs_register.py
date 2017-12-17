# codecs_register.py

import codecs
import encodings


def search1(encoding):
    print('ricerca1: Ricerca di:', encoding)
    return None


def search2(encoding):
    print('search2: Ricerca di:', encoding)
    return None


codecs.register(search1)
codecs.register(search2)

utf8 = codecs.lookup('utf-8')
print('UTF-8:', utf8)

try:
    unknown = codecs.lookup('codifica-non-presente')
except LookupError as err:
    print('ERRORE:', err)
