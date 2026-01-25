# TFM_MET - Assessing Comfort in Educational Environments

This project uses environmental sensors (BH1750) connected to a Raspberry Pi, and sends the data to AWS IoT Core using MQTT.

---

## Project Software Structure

```
TFM_MET/
├─ sensors/           # Sensor libraries (BH1750, etc.)
├─ cloud_client/      # MQTT client for AWS IoT and configuration
├─ main.py            # Main script that reads sensors and publishes to the cloud
├─ requirements.txt   # Python dependencies
└─ venv/              # Virtual environment (not versioned)
```

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd TFM_MET
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your AWS IoT certificates in `cloud_client/certs/`.

---

## AWS IoT Configuration

- Create a Thing in AWS IoT Core
- Generate certificates (Device Certificate, Private Key, Root CA)
- Save them in `cloud_client/certs/`
- Configure the paths and endpoint in `cloud_client/config.py`

---

## Usage

With the virtual environment active:

```bash
python main.py
```

- The script reads the sensors and publishes the data to AWS IoT.
- You can monitor the messages in the MQTT test console in AWS IoT Core.

---

## Notes

- Always activate the virtual environment before running the project.
- Keep the `certs/` folder excluded from Git to protect the AWS credentials.

