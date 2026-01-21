# --------------------------------------
#  Test sensor.
#
# Author : Arnau Alabau Serra
# Date   : 01/01/2026
#
# --------------------------------------
from time import sleep
from BH1750 import BH1750

sensor = BH1750()

while True:
    print(sensor.read_light_format_string())
    sleep(1)
