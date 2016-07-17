#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import asyncore
import logging
import socket

from asynchat_echo_handler import EchoHandler

class EchoServer(asyncore.dispatcher):
    """Riceve connessioni ed imposta gestori per ogni client.
    """
    
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(1)
        return

    def handle_accept(self):
        # Chiamato quando un client si connette al nostro socket
        client_info = self.accept()
        EchoHandler(sock=client_info[0])
        # Si vuole avere a che fare con un solo client alla volta
        # quindi si chiude non appena viene impostato il gestore
        # Normalmente non si dovrebbe fare ciò ed il server
        # rimarrebbe in esecuzione per sempre o fintanto che non
        # riceve istruzioni per terminare.
        self.handle_close()
        return
    
    def handle_close(self):
        self.close()