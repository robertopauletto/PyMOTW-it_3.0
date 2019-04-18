# smtpd_senddata.py

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('Questo il corpo del messaggio.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'destinatario@esempio.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'autore@esempio.com'))
msg['Subject'] = 'Semplice messaggio di test'

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('autore@esempio.com',
                    ['destinatario@esempio.com'],
                    msg.as_string())
finally:
    server.quit()
