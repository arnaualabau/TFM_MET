# --------------------------------------
#  Main - Multi Sensor IoT Node
#
# Author : Arnau Alabau Serra
# --------------------------------------

from time import sleep
from datetime import datetime, timezone

from sensors import BH1750, BMP280, VisionSensor
from cloud_client import IoTClient, TOPICS, THING_NAME

# Flag to send the payload to AWS
SEND_TO_AWS = False

# -------------------------
# Sensors initialization
# -------------------------
bh1750_lux_sensor = BH1750(device=0x23)
vision_sensor = VisionSensor(camera_index=0)

# -------------------------
# IoT client initialization
# -------------------------
iot = IoTClient()
iot.connect()


# -------------------------
# Main loop
# -------------------------
try:
    while True:

        # -------- Light Sensor --------
        lux = bh1750_lux_sensor.read_light()

        # -------- Vision Sensor --------
        detections = vision_sensor.capture_and_detect(confidence_threshold=0.5)

        # -------- Build Measurements --------
        measurements = {}

        # Light data
        if lux is not None:
            measurements["light"] = {
                "sensor_id": "bh1750_1",
                "lux": round(lux, 2),
                "unit": "lux"
            }

        # Vision data
        if detections is not None:

            # Count specific objects
            person_count = sum(1 for d in detections if d["class"] == "person")
            phone_count = sum(1 for d in detections if d["class"] == "cell phone")

            measurements["vision"] = {
                "sensor_id": "camera_1",
                "people_detected": person_count,
                "phones_detected": phone_count,
                "raw_detections": detections
            }

        # -------- Publish only if we have data --------
        if measurements:
            payload = {
                "device_id": THING_NAME,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "measurements": measurements
            }

        if SEND_TO_AWS:
            iot.publish(TOPICS["data"], payload)
        else:
            print(f"[DEV MODE] Payload ready to publish:\n{payload}")

        sleep(10)

except KeyboardInterrupt:
    print("\nExiting gracefully...")
    vision_sensor.release()
    iot.disconnect()
