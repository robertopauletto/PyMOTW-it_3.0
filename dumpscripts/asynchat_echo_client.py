#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import asynchat
import logging
import socket


class EchoClient(asynchat.async_chat):
    """Sends messages to the server and receives responses.
    """

    # La dimensione del buffer viene artificialmente ridotta per illustrare
    # l'invio e la ricezione di messaggi parziali.
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64
    
    def __init__(self, host, port, message):
        self.message = message
        self.received_data = []
        self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host, port))
        return
        
    def handle_connect(self):
        self.logger.debug('handle_connect()')
        # Invia il comando
        self.push('ECHO %d\n' % len(self.message))
        # Invia i dati
        self.push_with_producer(EchoProducer(self.message, buffer_size=self.ac_out_buffer_size))
        # Ci si attende che i dati ritornino tali e quali 
        # quindi si imposta un terminatore basato sulla lunghezza dei dati
        self.set_terminator(len(self.message))
    
    def collect_incoming_data(self, data):
        """Legge un messaggio in arrivo dal client e lo mette nella coda in
        uscita."""
        self.logger.debug('collect_incoming_data() -> (%d)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RICEVUTA COPIA DEL MESSAGGIO')
        else:
            self.logger.debug('ERRORE IN TRANSMISSIONE')
            self.logger.debug('ATTESI   "%s"', self.message)
            self.logger.debug('RICEVUTI "%s"', received_message)
        return

class EchoProducer(asynchat.simple_producer):

    logger = logging.getLogger('EchoProducer')

    def more(self):
        response = asynchat.simple_producer.more(self)
        self.logger.debug('more() -> (%s bytes)\n"""%s"""', len(response), response)
        return response