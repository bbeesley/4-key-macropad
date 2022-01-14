from adafruit_neokey.neokey1x4 import NeoKey1x4


class StatefulKey:
    def __init__(self, neokey: NeoKey1x4, key: int):
        self.key = key
        self._prev_state = False
        self.fell = False
        self.rose = False
        self.neokey = neokey
        self.key = key

    def update(self):
        state = self.neokey[self.key]
        if state != self._prev_state:
            if state:
                self.rose = False
                self.fell = True
            else:
                self.rose = True
                self.fell = False
            self._prev_state = state
        else:
            self.rose = False
            self.fell = False
