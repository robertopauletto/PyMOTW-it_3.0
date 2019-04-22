# mailbox_maildir_add_flag.py

import mailbox

print('Prima:')
mbox = mailbox.Maildir('Esempio')
mbox.lock()
try:
    for message_id, message in mbox.iteritems():
        print('{:6} "{}"'.format(message.get_flags(),
                                 message['subject']))
        message.add_flag('F')
        # Si chiede a milabox di aggiornare il messaggio
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nDopo:')
mbox = mailbox.Maildir('Esempio')
for message in mbox:
    print('{:6} "{}"'.format(message.get_flags(),
                             message['subject']))
