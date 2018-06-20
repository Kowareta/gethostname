#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, date, time
import socket
import logging
import sys

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    #GET
    def do_GET(self):

        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        #Send response status code
        self.send_response(200)

        #Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        #Send hostname back to client
        hostname = (socket.gethostname())
        #Write contens as utf-8 data
        self.wfile.write(bytes(hostname, "utf8"))
        return

    #Write stduot/stderr into logfile
    def log_request(self, code='-', size='-'):

        logging.info(("%s - - [%s] %s" %
              (self.address_string(),
               self.log_date_time_string(),
               '"%s" %s %s' % (self.requestline, str(code), str(size))
               )
        ))

def run():

    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y.%m.%d %H:%M:%S:', filename='gethostname.log', level=logging.DEBUG)
    #print('Starting server...')
    logging.info('Starting server...')
    #Server settings
    server_address = ('', 80)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    #print('Server is running...')
    logging.info('Server is running...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping server...\n')

run()
