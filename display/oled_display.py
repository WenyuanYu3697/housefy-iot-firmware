# display/oled_display.py
import qwiic_oled_display
import time

class OLEDDisplay:
    def __init__(self):
        self.display = qwiic_oled_display.QwiicOledDisplay()
        self.display.begin()
        self.display.clear(self.display.PAGE)

    def update(self, aqi, aqi_status, lux, temperature, humidity):
        self.display.clear(self.display.PAGE)
        self.display.set_cursor(0, 0)
        self.display.print(f"AQI: {aqi if aqi is not None else 'N/A'}, Status: {aqi_status if aqi_status is not None else 'N/A'}")
        self.display.set_cursor(0, 10)
        self.display.print(f"Lux Level: {lux:.2f} lux" if lux is not None else "Lux: N/A")
        self.display.set_cursor(0, 20)
        self.display.print(f"Temp: {temperature:.1f}C" if temperature is not None else "Temp: N/A")
        self.display.print(f", Hum: {humidity:.1f}%" if humidity is not None else ", Hum: N/A")
        self.display.display()