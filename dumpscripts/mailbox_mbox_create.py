#!/usr/bin/env python
# -*- coding: UTF-8*-

import mailbox
import email.utils

from_addr = email.utils.formataddr(('Author', 'author@example.com'))
to_addr = email.utils.formataddr(('Recipient', 'recipient@example.com'))

mbox = mailbox.mbox('example.mbox')
mbox.lock()
try:
    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author Sat Feb  7 01:05:34 2009')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Messaggio di prova n. 1'
    msg.set_payload('Questo è il corpo del messaggio.\nFrom (dovrebbe essere prefissato da >).\nCi sono 3 righe.\n')
    mbox.add(msg)
    mbox.flush()

    msg = mailbox.mboxMessage()
    msg.set_unixfrom('author')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Messaggio di prova n. 2'
    msg.set_payload('Questo è il corpo del secondo messaggio.\n')
    mbox.add(msg)
    mbox.flush()
finally:
    mbox.unlock()

print open('example.mbox', 'r').read()

