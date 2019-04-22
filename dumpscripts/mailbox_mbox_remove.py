# mailbox_mbox_remove.py

import mailbox

mbox = mailbox.mbox('esempio.mbox')
mbox.lock()
try:
    to_remove = []
    for key, msg in mbox.iteritems():
        if '2' in msg['subject']:
            print('Rimozione di:', key)
            to_remove.append(key)
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

print(open('esempio.mbox', 'r').read())
