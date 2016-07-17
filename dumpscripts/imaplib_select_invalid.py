#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
import imaplib_connect

c = imaplib_connect.open_connection()
try:
    typ, data = c.select('Non Esiste')
    print typ, data
finally:
    c.logout()