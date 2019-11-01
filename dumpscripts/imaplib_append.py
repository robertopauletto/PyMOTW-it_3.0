# imaplib_append.py

import imaplib
import time
import email.message
import imaplib_connect

new_message = email.message.Message()
new_message.set_unixfrom('pymotw3-ot')
new_message['Subject'] = 'Oggetto va qui'
new_message['From'] = 'pymotw3@esempio.com'
new_message['To'] = 'esempio@esempio.com'
new_message.set_payload('Il corpo del messaggio.\n')

print(new_message)

with imaplib_connect.open_connection() as c:
    c.append('INBOX', '',
             imaplib.Time2Internaldate(time.time()),
             str(new_message).encode('utf-8'))

    # Mostra le intestazioni di tutti i messaggi della casella di osta
    c.select('INBOX')
    typ, [msg_ids] = c.search(None, 'ALL')
    for num in msg_ids.split():
        typ, msg_data = c.fetch(num, '(BODY.PEEK[HEADER])')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                print('\n{}:'.format(num))
                print(response_part[1])
