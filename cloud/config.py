# --------------------------------------
#  Cloud Config
#
# Author : Arnau Alabau Serra
# Date   : 23/01/2026
# --------------------------------------

AWS_IOT_ENDPOINT = "your-iot-endpoint.amazonaws.com"
CA_CERT = "certs/root-CA.crt"
DEVICE_CERT = "certs/device-cert.pem"
PRIVATE_KEY = "certs/private-key.pem"

TOPICS = {
    "light": "sensors/luz/1",
    "temp": "sensors/temp/1",
    "hum": "sensors/hum/1",
    "motion": "sensors/mov/1"
}