# mailbox_maildir_set_subdir.py

import mailbox
import os

print('Prima:')
mbox = mailbox.Maildir('Esempio')
mbox.lock()
try:
    for message_id, message in mbox.iteritems():
        print('{:6} "{}"'.format(message.get_subdir(),
                                 message['subject']))
        message.set_subdir('cur')
        # Si chiede a mailbox di aggiornare il messaggio
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nDopo:')
mbox = mailbox.Maildir('Esempio')
for message in mbox:
    print('{:6} "{}"'.format(message.get_subdir(),
                             message['subject']))

print()
for dirname, subdirs, files in os.walk('Esempio'):
    print(dirname)
    print('  Directory:', subdirs)
    for name in files:
        fullname = os.path.join(dirname, name)
        print(fullname)
