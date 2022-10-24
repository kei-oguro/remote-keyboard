from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, List
from urllib.parse import parse_qs, urlparse
from pynput.keyboard import Controller

_keyboard = Controller()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/send":
            self.send(parse_qs(parsed.query))
        elif parsed.path == "/welcome":
            self.displayAddress()
        elif parsed.path == "/":
            self.displayClientPage()
        else:
            self.send_error(404, f"Unknown resource address {parsed.path}")

    def send(self, query: Dict[str, List[str]]) -> None:
        """文字列をキーボードから入力する"""
        self.sendHeader("text/plain")
        if strings := query.get("str"):
            for string in strings:
                _keyboard.type(string)

    def displayAddress(self) -> None:
        self.send_error(404, "not implemented, yet.")
        # self.sendHeader("image/jpeg")
        # todo: convert address into QR code.

    def displayClientPage(self) -> None:
        self.sendHeader("text/html")
        self.wfile.write(self.GetClientPage())

    def GetClientPage(self) -> bytes:
        if not hasattr(self, "clientPage") or self.clientPage is None:
            with open("remote-keyboard-client.html", "rb") as f:
                self.clientPage = f.read()
        return self.clientPage

    def sendHeader(self, contentType: str) -> None:
        self.send_response(200)
        self.send_header("Content-type", contentType)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()


HTTPServer(("", 8000), MyServer).serve_forever()
