import machine
import utime

analog_value = machine.ADC(0)

while True:
    reading = analog_value.read_u16()
    print("adc: ", reading)
    utime.sleep(0.2)