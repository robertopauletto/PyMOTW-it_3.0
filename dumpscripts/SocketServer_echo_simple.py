#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import SocketServer

class EchoRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # Restituisce i dati ricevuti al client
        data = self.request.recv(1024)
        self.request.send(data)
        return

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0) # si ottiene una porta dal kernel 
    server = SocketServer.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address # si trova quale porta si è ottenuto

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # non rimane appeso in uscita
    t.start()

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Invio dei dati
    message = 'Hello, world'
    print 'In invio: "%s"' % message
    len_sent = s.send(message)

    # Ricezione della risposta
    response = s.recv(len_sent)
    print 'Ricevuti: "%s"' % response

    # Pulizia
    s.close()
    server.socket.close()