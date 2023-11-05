from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):

        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if path == '/serial-number-decrypt' and 'serial-number' in query_params:
            # Dummy page which displays decrypted serial number and owner information
            self.path = '/page.html'
        else:
            self.path = '/404.html'
        return super().do_GET()


def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server started on port {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
