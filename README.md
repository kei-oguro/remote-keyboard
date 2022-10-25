# remote-keyboard

python http server and Javascript client sends key-code or unicode string.

This is not a security consideration at all. Use carefully.

## Server

python script boots the http server. Server waits requests. Requests contains strings or keycodes with shift, ctrl, alt, meta keys status.

ex)
```
curl http://localhost:8000/send?tap=a&alt=shift
```

- Server returns client html page, if path is empty.
- (not implementd) If path is `webcome`, server returns QR code .png image to input httpd server address, like `http://192.168.1.2:8000/`.
  - You display this page on server machine and read QR code to open the page on client machine (e.g. smart phone).
- Server sends keyboard events for every request it received.

### API

- `/` returns client html page.
- `/tap` sends keyboard event to server machine. It is for unicode string.
  - Argument.
    - str
      - Specify unicode string. Server sends this string to machine running this process.
- `/type` sends keyboard event to server machine. It is for only 1 key input, key-down and key-up. Event contains meta key status. Maybe, you can use this API to press multi keys simultaneously.
  - Arguments.
    - key
      - Specify keycode.
      - Keycodes are listed in https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
    - alt
      - Specify keycode.
      - Usually, alt keys are `shift`, `ctrl`, `alt` and `cmd`. But you can specify non-meta keys to press regular keys.
- `/welcome` not implemented.

The same argument may be specified any number of times.

Mouse event APIs are good idea. But it is not scheduled. 

Separated single key-down and key-up event APIs are not scheduled.

## Client

The single html page sends http request to server.
Requests contains keycodes and meta key status.
If you want, use `curl` or similar tools to send request.

## Dependency

- pynput

## Install

1. Install python3.
2. Install dependencies. Like ... `pip install pynput`. Add `--user` if you need.
3. Clone this project or download.

## Run

1. Run script. `python3 remote-keyboard-server.py`
2. (not implemented) Access `http://localhost:8000/` by browser on same machine. Then QR code image will be displayed.
3. Read QR code by phone camera to open client page.

