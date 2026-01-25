# --------------------------------------
#  Cloud Config
#
# Author : Arnau Alabau Serra
# Date   : 23/01/2026
# --------------------------------------

import os

# AWS IoT
AWS_IOT_ENDPOINT = "abcd1234-ats.iot.eu-west-1.amazonaws.com"
THING_NAME = "TFM_MET_RPI_01"

# Certificate Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CERT_PATH = os.path.join(BASE_DIR, "cloud", "certs")

ROOT_CA = os.path.join(CERT_PATH, "root-CA.crt")
DEVICE_CERT = os.path.join(CERT_PATH, "device.pem.crt")
PRIVATE_KEY = os.path.join(CERT_PATH, "private.pem.key")

# Topics MQTT
TOPICS = {
    "light": "sensors/luz/1",
    "temp": "sensors/temp/1",
    "hum": "sensors/hum/1",
    "motion": "sensors/mov/1"
}