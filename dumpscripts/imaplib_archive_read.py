#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
import imaplib_connect
from imaplib_list_parse import parse_list_response

c = imaplib_connect.open_connection()
try:
    c.select('Archive.Today')

    # Che identificativi ci sono nella mailbox=
    typ, [msg_ids] = c.search(None, 'ALL')
    print 'Messaggi di partenza:', msg_ids
    
    # Trova i messaggi
    typ, [msg_ids] = c.search(None, '(SUBJECT "Lorem ipsum")')
    msg_ids = ','.join(msg_ids.split(' '))
    print 'Messaggi corrispondenti:', msg_ids
    
    # Quali sono i flag attuali?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print 'Flags prima:', response
    
    # Cambio il flag Deleted
    typ, response = c.store(msg_ids, '+FLAGS', r'(\Deleted)')
    
    # Quali sono i flag adesso?
    typ, response = c.fetch(msg_ids, '(FLAGS)')
    print 'Flags dopo:', response
    
    # Cancello veramente i messaggi
    typ, response = c.expunge()
    print 'Cancellati:', response
    
    # Quali identificativi sono rimasti nella mailbox?
    typ, [msg_ids] = c.search(None, 'ALL')
    print 'Messaggi rimasti:', msg_ids
    
finally:
    try:
        c.close()
    except:
        pass
    c.logout()
