# sensors/temperature_humidity.py
import adafruit_dht
import board
import time

class TemperatureHumiditySensor:
    def __init__(self):
        self.sensor = adafruit_dht.DHT22(board.D4)

    def read(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity
            return temperature, humidity
        except RuntimeError as error:
            time.sleep(2)
            return None, None
