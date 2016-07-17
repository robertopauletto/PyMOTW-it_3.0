#!/usr/binf/env python
# -*- coding: UTF-8 -*-

import asyncore
import logging

class EchoServer(asyncore.dispatcher):
    """Riceve connessione ed imposta handler per ogni  client.
    """
    
    def __init__(self, address):
        self.logger = logging.getLogger('EchoServer')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.logger.debug('attaccato a %s', self.address)
        self.listen(1)
        return

    def handle_accept(self):
        # Chiamato quando un client si connette al nostro socket
        client_info = self.accept()
        self.logger.debug('handle_accept() -> %s', client_info[1])
        EchoHandler(sock=client_info[0])
        # Si vuole gestire un solo client alla volta,
        # quindi chiudiamo non appena viene impostato l'handler.
        # Normalmente non si dovrebbe fare così ed il server
        # rimaarrebbe in esecuzione per sempre o fino a che non riceve
        # istruzioni di arresto.
        self.handle_close()
        return
    
    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()
        return

class EchoHandler(asyncore.dispatcher):
    """Gestisce i messaggi di echoing da un singolo client.
    """
    
    def __init__(self, sock, chunk_size=256):
        self.chunk_size = chunk_size
        self.logger = logging.getLogger('EchoHandler%s' % str(sock.getsockname()))
        asyncore.dispatcher.__init__(self, sock=sock)
        self.data_to_write = []
        return
    
    def writable(self):
        """Se abbiamo ricevuto dati li scriviamo."""
        response = bool(self.data_to_write)
        self.logger.debug('writable() -> %s', response)
        return response
    
    def handle_write(self):
        """Scriviamo quanto più possibile del messaggio più recente ricevuto."""
        data = self.data_to_write.pop()
        sent = self.send(data[:self.chunk_size])
        if sent < len(data):
            remaining = data[sent:]
            self.data.to_write.append(remaining)
        self.logger.debug('handle_write() -> (%d) "%s"', sent, data[:sent])
        if not self.writable():
            self.handle_close()

    def handle_read(self):
        """Legge un messaggio in arrivo dal client e lo mette nella coda in uscita."""
        data = self.recv(self.chunk_size)
        self.logger.debug('handle_read() -> (%d) "%s"', len(data), data)
        self.data_to_write.insert(0, data)
    
    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()


class EchoClient(asyncore.dispatcher):
    """Invia messaggi al server e riceve risposte
    """
    
    def __init__(self, host, port, message, chunk_size=512):
        self.message = message
        self.to_send = message
        self.received_data = []
        self.chunk_size = chunk_size
        self.logger = logging.getLogger('EchoClient')
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug('connessione a %s', (host, port))
        self.connect((host, port))
        return
        
    def handle_connect(self):
        self.logger.debug('handle_connect()')
    
    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RECEVUTA COPIA DEL MESSAGGIO')
        else:
            self.logger.debug('ERRORE IN TRASMISSIONE')
            self.logger.debug('ATTESI   "%s"', self.message)
            self.logger.debug('RICEVUTI "%s"', received_message)
        return
    
    def writable(self):
        self.logger.debug('writable() -> %s', bool(self.to_send))
        return bool(self.to_send)

    def handle_write(self):
        sent = self.send(self.to_send[:self.chunk_size])
        self.logger.debug('handle_write() -> (%d) "%s"', sent, self.to_send[:sent])
        self.to_send = self.to_send[sent:]

    def handle_read(self):
        data = self.recv(self.chunk_size)
        self.logger.debug('handle_read() -> (%d) "%s"', len(data), data)
        self.received_data.append(data)
        

if __name__ == '__main__':
    import socket

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )

    address = ('localhost', 0) # let the kernel give us a port
    server = EchoServer(address)
    ip, port = server.address # find out what port we were given

    client = EchoClient(ip, port, message=open('lorem.txt', 'r').read())

    asyncore.loop()