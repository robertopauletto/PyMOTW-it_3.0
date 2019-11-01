# imaplib_delete_messages.py

import imaplib
import imaplib_connect
from imaplib_list_parse import parse_list_response

with imaplib_connect.open_connection() as c:
    c.select('INBOX.Esempio.Oggi')

    # Che identificativi ci sono nella casella?
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Messaggi di partenza:', msg_ids)

    # Trova i(l) messaggi(o)
    typ, [msg_ids] = c.search(
        None,
        '(SUBJECT "oggetto va qui")',
    )
    msg_ids = ','.join(msg_ids.decode('utf-8').split(' '))
    print('Messaggi corrispondenti:', msg_ids)

    # Quali sono i segnalatori correnti?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Segnalatori prima:', response)

    # Modifica il segnalatore Delete
    typ, response = c.store(msg_ids, '+FLAGS', r'(\Deleted)')

    # Quali sono i segnalatori adesso?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print('Segnalatori after:', response)

    # Really delete the message.
    typ, response = c.expunge()
    print('Cancellati definitivamente:', response)

    # Che identificativi sono rimasti  nella casella?
    typ, [msg_ids] = c.search(None, 'ALL')
    print('Messaggi rimasti:', msg_ids)
