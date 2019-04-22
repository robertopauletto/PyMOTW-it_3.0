# mailbox_mbox_read.py

import mailbox

mbox = mailbox.mbox('esempio.mbox')
for message in mbox:
    print(message['subject'])
