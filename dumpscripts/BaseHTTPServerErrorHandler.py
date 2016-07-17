#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler

class ErrorHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_error(404)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), ErrorHandler)
    print 'Server in esecuzione, usare <Ctrl-C> per interrompere'
    server.serve_forever()