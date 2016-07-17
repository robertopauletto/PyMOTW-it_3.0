#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import bz2
import logging
import SocketServer
import binascii

BLOCK_SIZE = 32

class Bz2RequestHandler(SocketServer.BaseRequestHandler):

    logger = logging.getLogger('Server')
    
    def handle(self):
        compressor = bz2.BZ2Compressor()
        
        # Scopre cosa vuole il client
        filename = self.request.recv(1024)
        self.logger.debug('il client ha richiesto: "%s"', filename)
        
        # Invia blocchi del file mentre vengono compressi
        with open(filename, 'rb') as input:
            while True:            
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW "%s"', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug('INVIO "%s"', binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('BUFFERING')
        
        # Invia qualsiasi dato rimasto nel buffer al compressore
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('SVUOTAMENTO "%s"', binascii.hexlify(to_send))
            self.request.send(to_send)
        return


if __name__ == '__main__':
    import socket
    import threading
    from cStringIO import StringIO

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )
    logger = logging.getLogger('Client')

    # Imposta un server, che viene eseguito in un thread separato
    address = ('localhost', 0) # Ottiene una porta dal kernel
    server = SocketServer.TCPServer(address, Bz2RequestHandler)
    ip, port = server.server_address # Scopre quale porta è stata ottenuta

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # Connessione al server
    logger.info('Contatto il server su %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Chiede un file
    requested_file = 'lorem.txt'
    logger.debug('invio del nome del file: "%s"', requested_file)
    len_sent = s.send(requested_file)

    # Riceve una risposta
    buffer = StringIO()
    decompressor = bz2.BZ2Decompressor()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('LETTURA "%s"', binascii.hexlify(response))

        # Include tutti i dati non consumati quando si alimenta il decompressore.
        decompressed = decompressor.decompress(response)
        if decompressed:
            logger.debug('DECOMPRESSI "%s"', decompressed)
            buffer.write(decompressed)
        else:
            logger.debug('BUFFERING')

    full_response = buffer.getvalue()
    lorem = open('lorem.txt', 'rt').read()
    logger.debug('la risposta corrisponde al contenuto del file: %s', full_response == lorem)

    # Pulizia
    s.close()
    server.socket.close()
