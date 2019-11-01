# imaplib_list.py

import imaplib
from pprint import pprint
from imaplib_connect import open_connection


with open_connection() as c:
    typ, data = c.list()
    print('Codice risposta:', typ)
    print('Risposta:')
    pprint(data)
