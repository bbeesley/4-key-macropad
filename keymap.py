from adafruit_hid.keycode import Keycode

# non standard keycodes
VOLUME_UP = 0x80
VOLUME_DOWN = 0x81
MUTE = 0x7F

teams = (
    [
        Keycode.COMMAND,
        Keycode.SHIFT,
        Keycode.M,
    ],
    [
        Keycode.COMMAND,
        Keycode.SHIFT,
        Keycode.O,
    ],
    [VOLUME_DOWN],
    [VOLUME_UP],
)
wasd = ([Keycode.W], [Keycode.A], [Keycode.S], [Keycode.D])
