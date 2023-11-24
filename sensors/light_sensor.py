# sensors/light_sensor.py
import adafruit_tsl2561
import board
import busio

class LightSensor:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_tsl2561.TSL2561(i2c)

    def read(self):
        return self.sensor.lux
