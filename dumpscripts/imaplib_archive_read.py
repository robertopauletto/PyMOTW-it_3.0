# imaplib_archive_read.py

import imaplib
import imaplib_connect


with imaplib_connect.open_connection() as c:
    # Trova i messaggi visti (SEEN) in INBOX
    c.select('INBOX')
    typ, [response] = c.search(None, 'SEEN')
    if typ != 'OK':
        raise RuntimeError(response)
    msg_ids = ','.join(response.decode('utf-8').split(' '))

    # Crea una nuova casella, "INBOX.Esempio.Oggi"
    typ, create_response = c.create('INBOX.Esempio.Oggi')
    print('Creato INBOX.Esempio.Oggi:', create_response)

    # Copia i messaggi
    print('IN COPIA:', msg_ids)
    c.copy(msg_ids, 'INBOX.Esempio.Oggi')

    # Legge il risultato
    c.select('INBOX.Esempio.Oggi')
    typ, [response] = c.search(None, 'ALL')
    print('COPIATI:', response)
