import RPi.GPIO as GPIO
import time
import random


class LED_Board:
    def __init__(self):
        self.pins = [19, 13, 6]
        self.pin_led_states = [
                [1, 0, -1], # A
                [0, 1, -1], # B
                [-1, 1, 0], # C
                [-1, 0, 1], # D
                [1, -1, 0], # E
                [0, -1, 1]  # F
            ]

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in range(0, 6):
            GPIO.setup(self.pins[i], GPIO.OUT)

    def clear_leds(self):
        # Skru foerst av alle LEDs
        for i in range(0, 3):
            GPIO.output(self.pins[i], GPIO.LOW)


    def light_led(self, light):
        self.clear_leds()
        # Skru paa den valgte LEDen
        for i in self.pin_led_states[light]:
            GPIO.ouput(i, GPIO.HIGH)

    def flash_all_leds(self, duration):
        for i in range(0, 5):
            for j in range(1, 100):
                self.light_led(j % 6)
            self.clear_leds()
            time.sleep(.200)
    
    def twinkle_all_leds(self, duration):
        for i in range(0, 10):
            self.light_led(random.randint(0, 6))
            time.sleep(.100)

    def power_off(self):
        return True

    def power_on(self):
        return True

