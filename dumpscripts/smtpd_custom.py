# smtpd_custom.py

import smtpd
import asyncore


class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print('Messaggio in ricezione da:', peer)
        print('Mittente del messaggio   :', mailfrom)
        print('Messaggio indirizzato a  :', rcpttos)
        print('Lunghezza del messaggio  :', len(data))


server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()
