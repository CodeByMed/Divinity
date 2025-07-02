'''
from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            'message': 'Welcome to the XS13 API!',
            'status': 'success'
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            'received_data': post_data.decode('utf-8'),
            'status': 'success'
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=4443): # PORT ID 4443
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket(httpd.socket, 
                                    certfile='path/to/certfile.pem', 
                                    keyfile='path/to/keyfile.pem', 
                                    server_side=True)
    print(f'HTTPS server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
'''