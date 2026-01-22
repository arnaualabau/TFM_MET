# --------------------------------------
#  BH1750 Sensor Library
#
# Author : Arnau Alabau Serra
# Date   : 01/01/2026
# --------------------------------------

import smbus
import time

class BH1750:
    """Class to interface with BH1750 light sensor via I2C."""

    # Default I2C address
    DEFAULT_DEVICE = 0x23  

    # Commands (reserved for future use / datasheet completeness)
    POWER_DOWN = 0x00
    POWER_ON = 0x01
    RESET = 0x07
    ONE_TIME_HIGH_RES_MODE = 0x20

    def __init__(self, device=DEFAULT_DEVICE, bus_num=1):
        """
        Initialize BH1750 sensor.
        :param device: I2C address
        :param bus_num: I2C bus number (1 for Raspberry Pi rev 2+)
        """
        self.device = device
        self.bus = smbus.SMBus(bus_num)

    def _data_to_lux(self, data):
        """Convert 2-byte data to lux value."""
        if len(data) != 2:
            raise ValueError("Invalid data length from sensor")
        return (data[0] << 8 | data[1]) / 1.2

    def read_light(self):
        """
        Read light level from sensor in lux.
        :return: float lux
        """
        try:
            data = self.bus.read_i2c_block_data(self.device, self.ONE_TIME_HIGH_RES_MODE, 2)
            return self._data_to_lux(data)
        except OSError as e:
            print(f"Error reading BH1750 sensor: {e}")
            return None

    def read_light_str(self):
        """Return light level as formatted string."""
        lux = self.read_light()
        if lux is None:
            return "Sensor error"
        return f"Light Level: {lux:.2f} lux"