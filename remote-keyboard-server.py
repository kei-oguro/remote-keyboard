from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from pynput.keyboard import Controller

keyboard = Controller()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        parsed = urlparse(self.path)
        if parsed.path == "/send":
            self.send(parse_qs(parsed.query))

    def send(self, query):
        if keys := query.get("key"):
            for key in keys:
                keyboard.type(key)


HTTPServer(("", 8000), MyServer).serve_forever()
