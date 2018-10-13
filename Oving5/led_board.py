import RPi.GPIO as GPIO
import time

class LED_Board():
    def __init__(self):
        return True;

    def setup(self):
        GPIO.setmode(GPIO.BCM);

    def light_led(self, light):
        return True;

    def flash_all_leds(self, duration):
        return True;
    
    def twinkle_all_leds(self, duration):
        return True;

    def power_off(self):
        return True;

    def power_on(self):
        return True;

