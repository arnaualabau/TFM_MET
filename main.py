# --------------------------------------
#  Test sensor.
#
# Author : Arnau Alabau Serra
# Date   : 01/01/2026
# --------------------------------------

from time import sleep
from sensors import BH1750, BMP280
from cloud import IoTClient, TOPICS

# Sensors init
bh1750_lux_sensor = BH1750(device=0x23)

# IoT client init
iot =  IoTClient()
iot.connect()

# Main Loop
try:
    while True:

        lux = lux_sensor.read_light()

        if lux is not None:
            payload = {
                "sensor": "BH1750",
                "lux": round(lux, 2)
            }
            iot.publish(TOPICS["light"], payload)
            print(f"Published: {payload}")
            
        sleep(5)  # esperar 5 segundos entre mediciones
except KeyboardInterrupt:
    print("\nExiting gracefully...")
    iot.disconnect()