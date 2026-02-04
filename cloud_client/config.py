# --------------------------------------
#  Cloud Config Constants
#
# Author : Arnau Alabau Serra
# Date   : 23/01/2026
# --------------------------------------

import os

# AWS IoT
AWS_IOT_ENDPOINT = "ado9y35hquln8-ats.iot.us-east-1.amazonaws.com"
THING_NAME = "TFM_MET_RPI_01"
MQTT_PORT = 8883

# Certificate Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CERT_PATH = os.path.join(BASE_DIR, "cloud_client", "certs")

ROOT_CA = os.path.join(CERT_PATH, "root-CA.pem")
DEVICE_CERT = os.path.join(CERT_PATH, "device.pem.crt")
PRIVATE_KEY = os.path.join(CERT_PATH, "private.pem.key")

# Topics MQTT
TOPICS = {
    "data": f"sensors/{THING_NAME}/data"
}