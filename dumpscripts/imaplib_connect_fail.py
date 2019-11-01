# imaplib_connect_fail.py

import imaplib
import configparser
import os


# Legge il file di configurazione
config = configparser.ConfigParser()
config.read([os.path.expanduser('~/.pymotw3')])

# Connessione al server
hostname = config.get('server', 'hostname')
print('Connessione a', hostname)
connection = imaplib.IMAP4_SSL(hostname)

# Accesso all'utenza
username = config.get('account', 'username')
password = 'password_errata'
print('Autenticazione come', username)
try:
    connection.login(username, password)
except Exception as err:
    print('ERRORE:', err)
