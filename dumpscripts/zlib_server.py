#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import zlib
import logging
import SocketServer
import binascii

BLOCK_SIZE = 64

class ZlibRequestHandler(SocketServer.BaseRequestHandler):

    logger = logging.getLogger('Server')
    
    def handle(self):
        compressor = zlib.compressobj(1)
        
        # Scopre cosa vuole il client
        filename = self.request.recv(1024)
        self.logger.debug('il client richiede: "%s"', filename)
        
        # Invia pezzi del file mentre vengono compressi
        with open(filename, 'rb') as input:
            while True:            
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('RAW "%s"', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug('IN INVIO "%s"', binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('BUFFERING')
        
        # Invia tutti i dati che il compressore ha nel buffer
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

    # Imposta un server, in esecuzione su di un thread separato
    address = ('localhost', 0) # lasciamo che il kernel ci dia una porta
    server = SocketServer.TCPServer(address, ZlibRequestHandler)
    ip, port = server.server_address # scopriamo che porta abbiamo ottenuto

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # Connessione al server
    logger.info('Contatto il server su %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Richiesta di un file
    requested_file = 'lorem.txt'
    logger.debug('invio nome file: "%s"', requested_file)
    len_sent = s.send(requested_file)

    # Ricezione della risposta
    buffer = StringIO()
    decompressor = zlib.decompressobj()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('LETTURA "%s"', binascii.hexlify(response))

        # Include any unconsumed data when feeding the decompressor.
        # Comprende tutti i dati non utilizzati quando si alimenta il decompressore
        to_decompress = decompressor.unconsumed_tail + response
        while to_decompress:
            decompressed = decompressor.decompress(to_decompress)
            if decompressed:
                logger.debug('DECOMPRESSIONE "%s"', decompressed)
                buffer.write(decompressed)
                # Cerca dati inutilizzati a causa del buffer overflow
                to_decompress = decompressor.unconsumed_tail
            else:
                logger.debug('BUFFERING')
                to_decompress = None

    # Si occupa dei dati rimasti all'interno del buffer del decompressore
    remainder = decompressor.flush()
    if remainder:
        logger.debug('SVUOTATI "%s"', remainder)
        buffer.write(reaminder)
    
    full_response = buffer.getvalue()
    lorem = open('lorem.txt', 'rt').read()
    logger.debug('la risposta corrisponde al contenuto del file: %s', full_response == lorem)

    # Pulizia
    s.close()
    server.socket.close()
