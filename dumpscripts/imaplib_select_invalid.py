# imaplib_select_invalid.py

import imaplib
import imaplib_connect

with imaplib_connect.open_connection() as c:
    typ, data = c.select('Non Esiste')
    print(typ, data)
