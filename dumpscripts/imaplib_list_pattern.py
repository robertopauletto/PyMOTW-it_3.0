# imaplib_list_pattern.py

import imaplib

from imaplib_connect import open_connection

with open_connection() as c:
    typ, data = c.list(pattern='*Esempio*')

print('Codice risposta:', typ)

for line in data:
    print('Risposta del server:', line)
