# zlib_server.py

import zlib
import logging
import socketserver
import binascii

BLOCK_SIZE = 64


class ZlibRequestHandler(socketserver.BaseRequestHandler):

    logger = logging.getLogger('Server')

    def handle(self):
        compressor = zlib.compressobj(1)

        # Scopre quale file vuole il client
        filename = self.request.recv(1024).decode('utf-8')
        self.logger.debug('il client richiede: %r', filename)

        # Invia pezzi del file mentre vengono compressi
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
                    self.logger.debug('IN BUFFER')

        # Invia tutti i dati che il compressore ha nel buffer
        remaining = compressor.flush()
        while remaining:
            to_send = remaining[:BLOCK_SIZE]
            remaining = remaining[BLOCK_SIZE:]
            self.logger.debug('SVUOTAMENTO %r',
                              binascii.hexlify(to_send))
            self.request.send(to_send)
        return


if __name__ == '__main__':
    import socket
    import threading
    from io import BytesIO

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(name)s: %(message)s',
    )
    logger = logging.getLogger('Client')

    # mposta un server, in esecuzione su di un thread separato
    address = ('localhost', 0)  # lasciamo che il kernel ci dia una porta
    server = socketserver.TCPServer(address, ZlibRequestHandler)
    ip, port = server.server_address  # quale porta è stata assegnata?

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    # onnessione al server come client
    logger.info('Contatto il server su %s:%s', ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Richiesta di un  file
    requested_file = 'lorem.txt'
    logger.debug('invio file con nome: %r', requested_file)
    len_sent = s.send(requested_file.encode('utf-8'))

    # Ricezione risposta
    buffer = BytesIO()
    decompressor = zlib.decompressobj()
    while True:
        response = s.recv(BLOCK_SIZE)
        if not response:
            break
        logger.debug('READ %r', binascii.hexlify(response))

        # Comprende tutti i dati non utilizzati quando
        # si alimenta il decompressore.
        to_decompress = decompressor.unconsumed_tail + response
        while to_decompress:
            decompressed = decompressor.decompress(to_decompress)
            if decompressed:
                logger.debug('DECOMPRESSSI %r', decompressed)
                buffer.write(decompressed)
                # Cerca dati non consumati a causa del buffer overflow
                to_decompress = decompressor.unconsumed_tail
            else:
                logger.debug('IN BUFFER')
                to_decompress = None

    # Si occupa dei dati rimasti all'interno del buffer del decompressore
    remainder = decompressor.flush()
    if remainder:
        logger.debug('SVUOTAMENTO %r', remainder)
        buffer.write(remainder)

    full_response = buffer.getvalue()
    lorem = open('lorem.txt', 'rb').read()
    logger.debug('la risposta corrisponde al contenuto del file: %s',
                 full_response == lorem)

    # Pulizia
    s.close()
    server.socket.close()
