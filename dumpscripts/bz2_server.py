# bz2_server.py
# -*- coding: utf-8 -*-
import bz2
import logging
import socketserver
import binascii

BLOCK_SIZE = 32


class Bz2RequestHandler(socketserver.BaseRequestHandler):

    logger = logging.getLogger('Server')

    def handle(self):
        compressor = bz2.BZ2Compressor()

        # Cosa vuole il client?
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('il client richiede: "%s"', filename)

        # Invio di pezzi del file mentre si stanno comprimento
        with open(filename, 'rb') as input:
            while True:
                block = input.read(BLOCK_SIZE)
                if not block:
                    break
                self.logger.debug('GREZZI %r', block)
                compressed = compressor.compress(block)
                if compressed:
                    self.logger.debug(
                        'IN INVIO %r',
                        binascii.hexlify(compressed))
                    self.request.send(compressed)
                else:
                    self.logger.debug('ACCUMULO')

        # Invia tutti i dati accumulati al compressore
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('SCARICAMENTO %r',
                              binascii.hexlify(to_send))
            self.request.send(to_send)
        return

if __name__ == '__main__':
    import socket
    import sys
    from io import StringIO
    import threading

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )

    # Set up a server, running in a separate thread
    address = ('localhost', 0)  # let the kernel assign a port
    server = socketserver.TCPServer(address, Bz2RequestHandler)
    ip, port = server.server_address  # what port was assigned?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    logger = logging.getLogger('Client')

    # Connessione al server
    logger.info('Contatto il server us %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Richiesta di un  file
    requested_file = (sys.argv[0]
                      if len(sys.argv) > 1
                      else 'lorem.txt')
    logger.debug('invio del nome del file: "%s"', requested_file)
    len_sent = s.send(requested_file.encode('utf-8'))

    # Riceve una risposta
    buffer = StringIO()
    decompressor = bz2.BZ2Decompressor()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('LETTURA %r', binascii.hexlify(response))

        # Include tutti i dati non consumati quando si
        #  alimenta il decompressore.
        decompressed = decompressor.decompress(response)
        if decompressed:
            logger.debug('DECOMPRESSI %r', decompressed)
            buffer.write(decompressed.decode('utf-8'))
        else:
            logger.debug('ACCUMULO')

    full_response = buffer.getvalue()
    lorem = open(requested_file, 'rt').read()
    logger.debug('la risposta corrisponde al contenuto del file: %s',
                 full_response == lorem)

    # Pulizia
    server.shutdown()
    server.socket.close()
    s.close()
