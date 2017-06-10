# http_server_errors.py

from http.server import BaseHTTPRequestHandler


class ErrorHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_error(404)


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), ErrorHandler)
    print('Server in esecuzione, usare <Ctrl-C> per terminare')
    server.serve_forever()
