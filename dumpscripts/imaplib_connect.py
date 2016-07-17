#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imaplib
import ConfigParser
import os

def open_connection(verbose=False):
    # Lettura del file di configurazione
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('~/.pymotw')])

    # Connessione al server
    hostname = config.get('server', 'hostname')
    # Aggiunto dal traduttore per utilizzare come esempio
    # un account su google
    port = config.get('server', 'port')
    # Aggiunto dal traduttore
    
    if verbose: print 'Connessione a', hostname
    connection = imaplib.IMAP4_SSL(hostname,port)

    # Connessione al proprio account
    username = config.get('account', 'username')
    password = config.get('account', 'password')
    if verbose: print 'Collegamento come', username
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
        print c
    finally:
        c.logout()