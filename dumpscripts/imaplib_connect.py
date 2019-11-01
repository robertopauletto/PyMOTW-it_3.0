# imaplib_connect.py

import imaplib
import configparser
import os


def open_connection(verbose=False):
    # Legge il file di configurazione
    config = configparser.ConfigParser()
    config.read([os.path.expanduser('~/.pymotw3')])

    # Connessione al server
    hostname = config.get('server', 'hostname')
    if verbose:
        print('Connessione a', hostname)
    connection = imaplib.IMAP4_SSL(hostname)

    # Accesso all'utenza
    username = config.get('account', 'username')
    password = config.get('account', 'password')
    print(username, password)
    if verbose:
        print('Autenticazione come', username)
    connection.login(username, password)
    return connection


if __name__ == '__main__':
    with open_connection(verbose=True) as c:
        print(c)

