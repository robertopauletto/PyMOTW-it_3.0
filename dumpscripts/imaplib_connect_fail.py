#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
import ConfigParser
import os

# Read the config file
config = ConfigParser.ConfigParser()
config.read([os.path.expanduser('~/.pymotw')])

# Connect to the server
hostname = config.get('server', 'hostname')
# Aggiunto dal traduttore per utilizzare come esempio
# un account su google
port = config.get('server', 'port')
# Aggiunto dal traduttore
print 'Connessione a', hostname
connection = imaplib.IMAP4_SSL(hostname, port)

# Login to our account
username = config.get('account', 'username')
password = 'questa-è-la-password-sbagliata'
print 'Connesso come', username
connection.login(username, password)