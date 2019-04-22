# mailbox_maildir_set_flags.py

import mailbox

print('Prima:')
mbox = mailbox.Maildir('Esempio')
mbox.lock()
try:
    for message_id, message in mbox.iteritems():
        print('{:6} "{}"'.format(message.get_flags(),
                                 message['subject']))
        message.set_flags('S')
        # Si chiede a mailbox di aggiornare il messaggio
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nDopo:')
mbox = mailbox.Maildir('Esempio')
for message in mbox:
    print('{:6} "{}"'.format(message.get_flags(),
                             message['subject']))
