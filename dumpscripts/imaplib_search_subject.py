# imaplib_search_subject.py

import imaplib
import imaplib_connect
from imaplib_list_parse import parse_list_response

with imaplib_connect.open_connection() as c:
    typ, mailbox_data = c.list()
    for line in mailbox_data:
        flags, delimiter, mbox_name = parse_list_response(line)
        c.select('"{}"'.format(mbox_name), readonly=True)
        typ, msg_ids = c.search(
            None,
            '(SUBJECT "Pymotw3-it imaplib")'
        )
        print(mbox_name, typ, msg_ids)
