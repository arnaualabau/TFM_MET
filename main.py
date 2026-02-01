# --------------------------------------
#  Test sensor.
#
# Author : Arnau Alabau Serra
# Date   : 01/01/2026
# --------------------------------------

from time import sleep
from datetime import datetime, timezone

from sensors import BH1750, BMP280
from cloud_client import IoTClient, TOPICS

# -------------------------
# Sensors initialization
# -------------------------
bh1750_lux_sensor = BH1750(device=0x23)

# -------------------------
# IoT client initialization
# -------------------------
iot =  IoTClient()
iot.connect()

# -------------------------
# Main loop
# -------------------------
try:
    while True:
        lux = bh1750_lux_sensor.read_light()

        if lux is not None:
            payload = {
                "device_id": THING_NAME,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "measurements": {
                    "light": {
                        "sensor_id": "bh1750_1",
                        "lux": round(lux, 2),
                        "unit": "lux"
                    }
                }
            }

            iot.publish(TOPICS["light"], payload)
            print(f"Published payload:\n{payload}")

        sleep(5)
except KeyboardInterrupt:
    print("\nExiting gracefully...")
    iot.disconnect()