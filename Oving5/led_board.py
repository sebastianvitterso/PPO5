import RPi.GPIO as GPIO
import time

class LED_Board():
    def __init__(self):
        self.pins = [18, 23, 24];
        self.pin_led_states = [
                [1, 0, -1], # A
                [0, 1, -1], # B
                [-1, 1, 0], # C
                [-1, 0, 1], # D
                [1, -1, 0], # E
                [0, -1, 1]  # F
            ];

    def setup(self):
        GPIO.setmode(GPIO.BCM);
        for i in range(0, 6):
            GPIO.setup(i, GPIO.OUT);

    def light_led(self, light):
        GPIO.ouput(light, GPIO.HIGH);

    def flash_all_leds(self, duration):
        for i in range(0, 6):
            self.light_led(i);
    
    def twinkle_all_leds(self, duration):
        return True;

    def power_off(self):
        return True;

    def power_on(self):
        return True;

