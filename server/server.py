import http.server
import socketserver
import json

PORT = 8000

# The path algorithm
def pathAlg(jsonObj):
    startNode = jsonObj["startLocation"]
    startHourStr = jsonObj["startTime"]
    waitTime = {}
    for key in 
    # create complete graph

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
        
        result = pathAlg(input_obj)

        self._set_headers()
        response = result
        self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), HTTPHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
