#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import SocketServer

class ForkingEchoRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = '%s: %s' % (cur_pid, data)
        self.request.send(response)
        return

class ForkingEchoServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    pass


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0) # si ottiene una porta dal kernel 
    server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    ip, port = server.server_address # si trova quale porta si è ottenuto

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # non rimane appeso in uscita
    t.start()
    print 'Server loop running in thread:', t.getName()

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Invio dei dati
    message = 'Hello, world'
    print 'In invio: "%s"' % message
    len_sent = s.send(message)

    # Ricezione della risposta
    response = s.recv(1024)
    print 'Ricevuti: "%s"' % response

    # Pulizia
    s.close()
    server.socket.close()