from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL to extract the query parameters
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if path == '/serialNumberLookup?serial_number=xx':

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
                self.wfile.write("path not found".encode())

        elif path == '/disablementInstructions?product_data=xx':

            if 'product_data' in query_params:
                
                disablement_instructions = "Press exit to disable"  # Dummy disablement instruction text

                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(disablement_instructions.encode())

            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("path not found".encode())

        elif path == '/pairingRegistry?product_data=xx':

            if 'product_data' in query_params:
                
                #owner data phone number and email
                owner_email = "abc@emial.com"
                owner_phone = "1201301400"
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                #owner data object
                owner_data = {"owner_email": owner_email , "owner_phone": owner_phone}
                self.wfile.write(json.dumps(owner_data).encode())
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("path not found".encode())

        else:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("path not found".encode())

def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
