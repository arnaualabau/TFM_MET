# --------------------------------------
#  Test sensor.
#
# Author : Arnau Alabau Serra
# Date   : 01/01/2026
# --------------------------------------

from time import sleep
from sensors import BH1750, BMP280
from cloud import IoTClient, TOPICS

bh1750_lux_sensor = BH1750(device=0x23)

try:
    while True:
        print(bh1750_lux_sensor.read_light_str())
        sleep(1)
except KeyboardInterrupt:
    print("\nExiting gracefully...")