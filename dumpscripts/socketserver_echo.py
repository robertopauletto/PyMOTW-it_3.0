# socketserver_echo.py

import logging
import sys
import socketserver

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(self, request,
                                                 client_address,
                                                 server)
        return

    def setup(self):
        self.logger.debug('setup')
        return socketserver.BaseRequestHandler.setup(self)

    def handle(self):
        self.logger.debug('handle')

        # Ritona gli stessi dati al client
        data = self.request.recv(1024)
        self.logger.debug('recv()->"%s"', data)
        self.request.send(data)
        return

    def finish(self):
        self.logger.debug('finish')
        return socketserver.BaseRequestHandler.finish(self)


class EchoServer(socketserver.TCPServer):

    def __init__(self, server_address,
                 handler_class=EchoRequestHandler,
                 ):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug('__init__')
        socketserver.TCPServer.__init__(self, server_address,
                                        handler_class)
        return

    def server_activate(self):
        self.logger.debug('server_activate')
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self, poll_interval=0.5):
        self.logger.debug('in attesa della richiesta')
        self.logger.info(
            'Gestione della richiesta, premere <Ctrl-C> per abbandonare'
        )
        socketserver.TCPServer.serve_forever(self, poll_interval)
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug('verify_request(%s, %s)',
                          request, client_address)
        return socketserver.TCPServer.verify_request(
            self, request, client_address,
        )

    def process_request(self, request, client_address):
        self.logger.debug('process_request(%s, %s)',
                          request, client_address)
        return socketserver.TCPServer.process_request(
            self, request, client_address,
        )

    def server_close(self):
        self.logger.debug('server_close')
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        self.logger.debug('finish_request(%s, %s)',
                          request, client_address)
        return socketserver.TCPServer.finish_request(
            self, request, client_address,
        )

    def close_request(self, request_address):
        self.logger.debug('close_request(%s)', request_address)
        return socketserver.TCPServer.close_request(
            self, request_address,
        )

    def shutdown(self):
        self.logger.debug('shutdown()')
        return socketserver.TCPServer.shutdown(self)


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0)  # lasciamo assegnare la porta al kernel
    server = EchoServer(address, EchoRequestHandler)
    ip, port = server.server_address  # che porta è stata assegnata?

    # Partenza del server in un thread
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)  # non rimane piantato in uscita
    t.start()

    logger = logging.getLogger('client')
    logger.info('Server su %s:%s', ip, port)

    # Connessione al server
    logger.debug('creazione del socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connessione al server')
    s.connect((ip, port))

    # Invio dati
    message = 'Ciao, mondo'.encode()
    logger.debug('invio dati: %r', message)
    len_sent = s.send(message)

    # Ricezione di una risposta
    logger.debug('in attesa di risposta')
    response = s.recv(len_sent)
    logger.debug('risposta dal server: %r', response)

    # Pulizia
    server.shutdown()
    logger.debug('chiusura del socket')
    s.close()
    logger.debug('fatto')
    server.socket.close()
