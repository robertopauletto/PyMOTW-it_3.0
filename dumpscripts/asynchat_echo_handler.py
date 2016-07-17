#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import asynchat
import logging


class EchoHandler(asynchat.async_chat):
    """Gestisce la riproduzione dei messaggi da un singolo client.
    """

    # La dimensione del buffer viene artificialmente ridotta per illustrare
    # l'invio e la ricezione di messaggi parziali.
    ac_in_buffer_size = 64
    ac_out_buffer_size = 64
    
    def __init__(self, sock):
        self.received_data = []
        self.logger = logging.getLogger('EchoHandler')
        asynchat.async_chat.__init__(self, sock)
        # Si comincia cercando il comando ECHO
        self.process_data = self._process_command
        self.set_terminator('\n')
        return

    def collect_incoming_data(self, data):
        """Legge un messaggio in arrivo dal client e lo mette nella coda in
        uscita."""
        self.logger.debug('collect_incoming_data() -> (%d bytes)\n"""%s"""', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        """E' stata trovata la fine di un comando o messaggio."""
        self.logger.debug('found_terminator()')
        self.process_data()
    
    def _process_command(self):        
        """Abbiamo il comando ECHO completp"""
        command = ''.join(self.received_data)
        self.logger.debug('_process_command() "%s"', command)
        command_verb, command_arg = command.strip().split(' ')
        expected_data_len = int(command_arg)
        self.set_terminator(expected_data_len)
        self.process_data = self._process_message
        self.received_data = []
    
    def _process_message(self):
        """Abbiamo letto l'intero emssaggio da ritornare al client"""
        to_echo = ''.join(self.received_data)
        self.logger.debug('_process_message() echoing\n"""%s"""', to_echo)
        self.push(to_echo)
        # Disconnessione dopo avere inviato l'intera risposta
        # visto che si vuole fare sono una cosa per volta
        self.close_when_done()