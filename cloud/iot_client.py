# --------------------------------------
#  IoT Client
#
# Author : Arnau Alabau Serra
# Date   : 23/01/2026
# --------------------------------------

import paho.mqtt.client as mqtt
import json
from cloud.config import AWS_IOT_ENDPOINT, CA_CERT, DEVICE_CERT, PRIVATE_KEY

class IoTClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.tls_set(ca_certs=CA_CERT,
                            certfile=DEVICE_CERT,
                            keyfile=PRIVATE_KEY)
        self.client.connect(AWS_IOT_ENDPOINT, 8883)

    def publish(self, topic, payload):
        """
        Publica un diccionario como JSON en el topic especificado.
        """
        self.client.publish(topic, json.dumps(payload))