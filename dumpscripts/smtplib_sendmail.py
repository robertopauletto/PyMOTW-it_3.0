# smtplib_sendmail.py

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('Questo il corpo del messaggio.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Semplice messaggio di prova'

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True)  # mostra la comunicazione con il server
try:
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    msg.as_string())
finally:
    server.quit()
