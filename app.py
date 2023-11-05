from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL to extract the query parameters
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if 'serial_number' in query_params:
            encrypted_serial_number = query_params['serial_number'][0]
            # Replace this with your decryption logic
            decrypted_serial_number = "adlu2uhjhb23627"  # Dummy value for demonstration

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(decrypted_serial_number.encode())
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Serial number parameter missing".encode())

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
