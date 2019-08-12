#!/usr/bin/env python

import http.server
import socket
import socketserver

PORT = 8080

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(f'Hostname: {socket.gethostname()}\n'.encode())

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    httpd.shutdown()
    httpd.server_close()
