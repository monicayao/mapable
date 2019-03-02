import http.server
import socketserver
import json

PORT = 8000

class HTTPHandler(http.server.BaseHTTPRequestHandler):
    # every HTTP response needs a header
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        print("received GET")

        self._set_headers()
        response = "We do not support GET."

        # encode in order to send json
        self.wfile.write(json.dumps(response).encode())

    def do_HEAD(self):
        self._set_headers()

    # valid json to send:
    # "{\"hi\": \"time for bed\"}"
    def do_POST(self):
        print("received POST")

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len).decode('utf-8')
        input_obj = json.loads(post_body)
        print(input_obj)
        
        # TODO : Handle Input Object

        self._set_headers()

        # TODO : Make Response from Input
        response = "Results updated in server"
        self.wfile.write(json.dumps(response).encode())

with socketserver.TCPServer(("", PORT), HTTPHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
