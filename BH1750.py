# --------------------------------------
#  BH1750 file
#
# Author : Arnau Alabau Serra
# Date   : 01/01/2026
#
# --------------------------------------
import smbus
import time


class BH1750:
    DEVICE = 0x23      # Default device I2C address
    POWER_DOWN = 0x00  # No active state
    POWER_ON = 0x01    # Power on
    RESET = 0x07       # Reset data register value
    ONE_TIME_HIGH_RES_MODE = 0x20
    bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

    def __init__(self, device=0x23):
        self.DEVICE = device

    def data_to_decimal(self, data):
        """
        Converts the "data" input 2byte data into decimal.
        :param data:
        :return:
        """
        return ((data[1] + (256 * data[0])) / 1.2)

    def read_light(self):
        """
        Sensor reading.
        :return:
        """
        data = self.bus.read_i2c_block_data(
            self.DEVICE,
            self.ONE_TIME_HIGH_RES_MODE
        )

        return self.data_to_decimal(data)

    def read_light_format_string(self):
        """
        Return lux level in String format.
        :return:
        """
        lux = self.read_light()
        str_lux = 'Light Level : ' + str(lux) + " lux"

        return str_lux
