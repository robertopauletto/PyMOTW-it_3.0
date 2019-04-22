# mailbox_mbox_create.py

import mailbox
import email.utils

from_addr = email.utils.formataddr(('Autore',
                                    'autore@esempio.com'))
to_addr = email.utils.formataddr(('Destinatario',
                                  'destinatario@esempio.com'))

payload = '''Questo e' il corpo.
From (sara' prefissato da sequenza di escape).
Ci sono 3 righe.
'''

mbox = mailbox.mbox('esempio.mbox')
mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('autore Sat Feb  7 01:05:34 2009')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Messaggio campione 1'
    msg.set_payload(payload)
    mbox.add(msg)
    mbox.flush()

    msg = mailbox.mboxMessage()
    msg.set_unixfrom('autore')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Messaggio campione 2'
    msg.set_payload("Questo e' il secondo corpo.\n")
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

print(open('esempio.mbox', 'r').read())
