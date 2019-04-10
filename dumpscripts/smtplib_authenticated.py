# smtplib_authenticated.py

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

# Chiede all'utente le informazioni di connessione
to_email = input('Destinatario: ')
servername = input('Nome server mail: ')
serverport = input('Porta del server: ')
if serverport:
    serverport = int(serverport)
else:
    serverport = 25
use_tls = input('Usare TLS? (si/no): ').lower()
username = input('Nome utente mail: ')
password = getpass.getpass("%s's password: " % username)

# Crea il messaggio
msg = MIMEText('Messaggio di prova da PyMOTW3-it.')
msg.set_unixfrom('author')
msg['To'] = email.utils.formataddr(('Recipient', to_email))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Prova da PyMOTW3-it'

if use_tls.startswith('s'):
    print('inizio con una connessione sicura')
    server = smtplib.SMTP_SSL(servername, serverport)
else:
    print('inizio con una connessione non sicura')
    server = smtplib.SMTP(servername, serverport)
try:
    server.set_debuglevel(True)

    # Ci identifichiamo, chiedendo al server quali caratteristiche supporta
    server.ehlo()

    # Se è possibile criptare la sessione, si fa
    if server.has_extn('STARTTLS'):
        print('(partenza di TLS)')
        server.starttls()
        server.ehlo()  # nuova identificazione su connessione TLS
    else:
        print('(no STARTTLS)')

    if server.has_extn('AUTH'):
        print('(autenticazione)')
        server.login(username, password)
    else:
        print('(no AUTH)')

    server.sendmail('author@example.com',
                    [to_email],
                    msg.as_string())
finally:
    server.quit()
