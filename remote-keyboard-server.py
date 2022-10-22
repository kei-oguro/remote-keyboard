from time import sleep
from pynput.keyboard import Controller, Key
from sys import argv

keyboard = Controller()
with keyboard.pressed(Key.alt):
    keyboard.tap(Key.tab)
sleep(1)
keyboard.type(argv[1] if len(argv) > 1 else "abcあいう")
