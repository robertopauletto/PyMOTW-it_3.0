# mailbox_maildir_create.py

import mailbox
import email.utils
import os

from_addr = email.utils.formataddr(('Autore', 'autore@esempio.com'))
to_addr = email.utils.formataddr(('Destinatario', 'destinatario@esempio.com'))

payload = '''Questo e' il corpo.
From (non viene preceduta da sequenza di escape).
Ci sono tre righe.
'''

mbox = mailbox.Maildir('Esempio')
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
    msg.set_unixfrom('autore Sat Feb  7 01:05:34 2009')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Messaggio campione 2'
    msg.set_payload("Questo e' il secondo corpo.\n")
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

for dirname, subdirs, files in os.walk('Esempio'):
    print(dirname)
    print('  Directory:', subdirs)
    for name in files:
        fullname = os.path.join(dirname, name)
        print('\n***', fullname)
        print(open(fullname).read())
        print('*' * 20)
