# utils/gpio_utils.py
import RPi.GPIO as GPIO

def setup_gpio(pin=17):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    return GPIO
