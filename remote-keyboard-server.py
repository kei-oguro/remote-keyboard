from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, List
from urllib.parse import parse_qs, urlparse
from pynput.keyboard import Controller, Key

_keyboard = Controller()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/tap":
            self.tap(parse_qs(parsed.query))
        elif parsed.path == "/type":
            self.type(parse_qs(parsed.query))
        elif parsed.path == "/welcome":
            self.displayAddress()
        elif parsed.path == "/":
            self.displayClientPage()
        else:
            self.send_error(404, f"Unknown resource address {parsed.path}")

    def type(self, query: Dict[str, List[str]]) -> None:
        """文字列をキーボードから入力する"""
        self.sendHeader("text/plain")
        if strings := query.get("str"):
            for string in strings:
                _keyboard.type(string)

    def tap(self, query: Dict[str, List[str]]) -> None:
        """キーを1つ押す。"""
        self.sendHeader("text/plain")
        alts = [self.convertKey(alt) for alt in query.get("alt") or []]
        for alt in alts:
            _keyboard.press(alt)
        if keys := query.get("key"):
            for key in keys:
                _keyboard.tap(key)
        for alt in alts:
            _keyboard.release(alt)

    def convertKey(self, keyName: str) -> Key:
        """Keyメンバの名前の文字列から値を返す。一覧は以下。
        https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
        """
        return Key.__getitem__(keyName)

    def displayAddress(self) -> None:
        self.send_error(404, "not implemented, yet.")
        # self.sendHeader("image/jpeg")
        # todo: convert address into QR code.

    def displayClientPage(self) -> None:
        self.sendHeader("text/html")
        self.wfile.write(self.GetClientPage())

    def GetClientPage(self) -> bytes:
        with open("remote-keyboard-client.html", "rb") as f:
            return f.read()

    def sendHeader(self, contentType: str) -> None:
        self.send_response(200)
        self.send_header("Content-type", contentType)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()


HTTPServer(("", 8000), MyServer).serve_forever()
