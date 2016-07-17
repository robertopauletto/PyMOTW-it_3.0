#!/usr/bin/env python
# -*- coding: UTF-8*-

import mailbox

mbox = mailbox.mbox('example.mbox')
to_remove = []
for key, msg in mbox.iteritems():
    if '2' in msg['subject']:
        print 'Rimuovo:', key
        to_remove.append(key)
mbox.lock()
try:
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

print open('example.mbox', 'r').read()
