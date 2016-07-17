#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
from pprint import pprint
from imaplib_connect import open_connection

c = open_connection()
try:
    typ, data = c.list()
    print 'Codice risposta:', typ
    print 'Risposta:'
    pprint(data)
finally:
    c.logout()