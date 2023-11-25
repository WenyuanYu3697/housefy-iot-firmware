# main.py
from firebase.firebase_service import FirebaseService
from sensors.air_quality import AirQualitySensor
from sensors.light_sensor import LightSensor
from sensors.temperature_humidity import TemperatureHumiditySensor
from display.oled_display import OLEDDisplay
from utils.gpio_utils import setup_gpio
import threading
import time

def main():
    # Initialize Firebase Service
    firebase_service = FirebaseService('/home/pi/Desktop/CombinedScripts/housefyFirmware/housefyPrivateKey.json', 'https://housefybackend-environment-default-rtdb.firebaseio.com/')

    # Initialize sensors
    air_quality_sensor = AirQualitySensor()
    light_sensor = LightSensor()
    temp_hum_sensor = TemperatureHumiditySensor()

    # Initialize OLED display
    oled_display = OLEDDisplay()

    # set up GPIO
    gpio = setup_gpio()

    def sensor_task():
        while True:
            # read data from sensors
            co2, tvoc, aqi, aqi_status = air_quality_sensor.read()
            lux = light_sensor.read()
            temperature, humidity = temp_hum_sensor.read()

            # organize data, and then upload Firebase
            data = {
                'co2': co2,
                'tvoc': tvoc,
                'aqi': aqi,
                'aqi_status': aqi_status,
                'lux': lux,
                'temperature': temperature,
                'humidity': humidity
            }
            firebase_service.upload_to_firebase(data)

            # update OLED display
            oled_display.update(aqi, aqi_status, lux, temperature, humidity)
            time.sleep(5)

    # 启动传感器读取和数据上传的线程
    sensor_thread = threading.Thread(target=sensor_task)
    sensor_thread.start()

    try:
        # 主线程保持运行，可以添加其他的任务或逻辑
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("程序已被用户中断")

if __name__ == '__main__':
    main()
