# --------------------------------------
#  IoT Client
#
# Author : Arnau Alabau Serra
# Date   : 23/01/2026
# --------------------------------------

import ssl
import json
import time
import paho.mqtt.client as mqtt

from cloud import AWS_IOT_ENDPOINT, THING_NAME, ROOT_CA, DEVICE_CERT, PRIVATE_KEY, MQTT_PORT


class IoTClient:
    def __init__(self):
        self.client = mqtt.Client(client_id=THING_NAME)

        # TLS Config
        self.client.tls_set(
            ca_certs=ROOT_CA,
            certfile=DEVICE_CERT,
            keyfile=PRIVATE_KEY,
            tls_version=ssl.PROTOCOL_TLSv1_2
        )

        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect

    def connect(self):
        print("Connecting to AWS IoT...")
        self.client.connect(AWS_IOT_ENDPOINT, MQTT_PORT)
        self.client.loop_start()
        time.sleep(1)

    def publish(self, topic, payload: dict):
        message = json.dumps(payload)
        self.client.publish(topic, message)
        print(f"Published to {topic}: {message}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    @staticmethod
    def _on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to AWS IoT ✔️")
        else:
            print(f"Connection failed (rc={rc})")

    @staticmethod
    def _on_disconnect(client, userdata, rc):
        print("Disconnected from AWS IoT")
