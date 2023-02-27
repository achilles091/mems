# -*- coding: utf-8 -*-

import board
from adafruit_bme280 import basic as adafruit_bme280
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
print("\nTemperature: %0.1f C" % bme280.temperature)
