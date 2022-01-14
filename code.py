import board
import rainbowio
from adafruit_hid.keyboard import Keyboard
import usb_hid
from adafruit_neokey.neokey1x4 import NeoKey1x4
import busio
import keymap
from stateful_key import StatefulKey

# choose a colour for keys when idle
IDLE_COLOUR = (51, 51, 255)

# choose a keymap
bindings = keymap.teams

# create the I2C bus
i2c_bus = busio.I2C(board.SCL1, board.SDA1)

# set up the virtual keyboard
keyboard = Keyboard(usb_hid.devices)

# connect the neo key
neokey = NeoKey1x4(i2c_bus)

# set up a debouncer for each keys
keys = [StatefulKey(neokey, 3 - i) for i in range(4)]

# set an iteration count to use to get rainbow colours on key press
iteration = 0

# set the key pixels to their initial colour
for i in range(4):
    neokey.pixels[i] = IDLE_COLOUR

while True:
    iteration = (iteration + 1) % 255
    for i in range(4):
        keys[i].update()
        if keys[i].fell:
            print("Button {} fell".format(i))
            keyboard.press(*bindings[i])
            neokey.pixels[3 - i] = rainbowio.colorwheel(iteration)
        if keys[i].rose:
            print("Button {} rose".format(i))
            keyboard.release(*bindings[i])
            neokey.pixels[3 - i] = IDLE_COLOUR
