# -*- coding: utf-8; -*-

from time import sleep
from pyfirmata import Arduino, OUTPUT

class CubeDevice(object):
    green_pins = [5, 9]
    red_pins = [6, 8]

    def __init__(self):
        self.board = None

    def discover(self):
        return [
            '/dev/ttyACM0',
            '/dev/ttyACM1',
        ]

    def _write_pins(self, pins, value):
        for p in pins:
            self.board.digital[p].write(value)

    def go_green(self):
        self._write_pins(self.red_pins, 0)
        self._write_pins(self.green_pins, 1)

    def go_red(self):
        self._write_pins(self.green_pins, 0)
        self._write_pins(self.red_pins, 1)

    def blink(self):
        for i in xrange(5):
            self.go_red()
            sleep(0.1)
            self.go_green()
            sleep(0.1)

    def connect(self, port):
        self.board = Arduino(port)
        for p in self.green_pins + self.red_pins:
            self.board.digital[p].mode = OUTPUT
    
    def disconnect(self):
        if not self.board:
            return
        self._write_pins(self.red_pins, 0)
        self._write_pins(self.green_pins, 0)
