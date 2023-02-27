# -*- coding: utf-8 -*-

pip3 install board
pip3 install adafruit_bme280
sudo pip install RPi.bme280
sudo apt-get install i2c-tools python-pip
sudo apt-get update
sudo apt-get install git build-essential i2c-tools

sudo apt update
sudo apt install libretech-gpio libretech-dtoverlay
sudo ldto enable i2c-ao
sudo ldto enable i2c-b

import board
from adafruit_bme280 import basic as adafruit_bme280
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
print("\nTemperature: %0.1f C" % bme280.temperature)