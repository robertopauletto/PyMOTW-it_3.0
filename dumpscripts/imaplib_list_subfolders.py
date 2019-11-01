# imaplib_list_subfolders.py

import imaplib

from imaplib_connect import open_connection

with open_connection() as c:
    typ, data = c.list(directory='INBOX.Esempio')

print('Codice di risposta:', typ)

for line in data:
    print('Risposta del server:', line)
