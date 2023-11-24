# sensors/air_quality.py
import adafruit_ccs811
import board
import busio
import time

def calculate_aqi(co2, tvoc):
    co2_breakpoints = [(0, 1000), (1001, 2000), (2001, 4000), (4001, 8192)]
    tvoc_breakpoints = [(0, 200), (201, 500), (501, 800), (801, 1187)]
    aqi_breakpoints = [(0, 50), (51, 100), (101, 150), (151, 200)]

    def interpolate(value, low1, high1, low2, high2):
        return ((value - low1) / (high1 - low1)) * (high2 - low2) + low2

    co2_aqi = tvoc_aqi = 0
    for low, high in co2_breakpoints:
        if low <= co2 <= high:
            co2_aqi = interpolate(co2, low, high, *aqi_breakpoints[co2_breakpoints.index((low, high))])
            break

    for low, high in tvoc_breakpoints:
        if low <= tvoc <= high:
            tvoc_aqi = interpolate(tvoc, low, high, *aqi_breakpoints[tvoc_breakpoints.index((low, high))])
            break

    combined_aqi = max(co2_aqi, tvoc_aqi)
    if combined_aqi <= 50:
        return int(combined_aqi), "Good"
    elif combined_aqi <= 100:
        return int(combined_aqi), "Moderate"
    elif combined_aqi <= 150:
        return int(combined_aqi), "Poor"
    else:
        return int(combined_aqi), "Unhealthy"

class AirQualitySensor:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ccs811 = adafruit_ccs811.CCS811(i2c)

    def data_ready(self):
        return self.ccs811.data_ready

    def read(self):
        if self.ccs811.data_ready:
            co2 = self.ccs811.eco2
            tvoc = self.ccs811.tvoc
            aqi, status = calculate_aqi(co2, tvoc)
            return co2, tvoc, aqi, status
        else:
            return None, None, None, None

    def run(self, upload_func):
        while not self.data_ready():
            time.sleep(0.5)  # 等待数据准备好
        while True:
            co2, tvoc, aqi, status = self.read()
            if co2 is not None:
                upload_func({
                    'co2': co2,
                    'tvoc': tvoc,
                    'aqi': aqi,
                    'status': status
                })
            time.sleep(2)  # 每2秒读取一次数据