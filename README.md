# remote-keyboard
python http server and Javascript client sends key-code or unicode string.

## Server

python script boots the http server.
Server waits requests.
Requests contains keycodes and shift, ctrl, alt, meta keys status.

ex)
```
curl http://localhost:8000/send?key=a&shift=1
```

(not implemented) Server deliver client page.
- Server returns client html page, if path is empty.
- If path is `webcome`, server returns QR code .png image to input httpd server address, like `http://192.168.1.2/`.
  - You display this page on server machine and read QR code to open the page on client machine (e.g. smart phone).

## Client

The single html page sends http request to server.
Requests contains keycodes and meta key status.
If you want, use `curl` or similar tools to send request.

## Dependency

- pynput

## Install

1. Clone this project or download.
2. Install python3.
3. Install dependencies. Like ... `pip install pynput`. Add `--user` is you need.

## Run

1. Run script. `python3 remote-keyboard-server.py`
2. (not implemented) Access `http://localhost:8000/` by browser on same machine. Then QR code image will be displayed.
3. Read QR code by phone camera to open client page.

