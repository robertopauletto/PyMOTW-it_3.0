# mailbox_maildir_read.py

import mailbox

mbox = mailbox.Maildir('Esempio')
for message in mbox:
    print(message['subject'])
