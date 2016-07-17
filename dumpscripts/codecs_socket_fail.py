#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import SocketServer

class Echo(SocketServer.BaseRequestHandler):

    def handle(self):
        # Ottengo alcuni byte e li riverbero al client.
        data = self.request.recv(1024)
        self.request.send(data)
        return


if __name__ == '__main__':
    import codecs
    import socket
    import threading

    address = ('localhost', 0) # Lasciamo che il kernel ci fornisca una porta
    server = SocketServer.TCPServer(address, Echo)
    ip, port = server.server_address # scopriamo quale porta ci è stata assegnata

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) #  non lo lasciamo appeso all'uscita
    t.start()

    # Connessione al server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Invia i data
    text = u'pi: π'
    len_sent = s.send(text)

    # Riceve una risposta
    response = s.recv(len_sent)
    print repr(response)

    # Pulizia
    s.close()
    server.socket.close()
