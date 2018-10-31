import RPi.GPIO as GPIO
import time
import random


class LED_Board:
    def __init__(self):
        # Output pins
        self.pins = [19, 13, 6]
        # Pin states
        self.pin_led_states = [
                [1, 0, -1], # 1
                [0, 1, -1], # 2
                [1, -1, 0], # 3
                [0, -1, 1], # 4
                [-1, 1, 0], # 5
                [-1, 0, 1]  # 6
            ]

    # GPIO setup for hver pin
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in range(0, 3):
            GPIO.setup(self.pins[i], GPIO.OUT)

    # Sett en pin til riktig state
    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    # Skru av alle leds
    def clear_leds(self):
        # Skru foerst av alle LEDs
        for i in range(0, 3):
            GPIO.setup(self.pins[i], GPIO.OUT)
            GPIO.output(self.pins[i], GPIO.LOW)

    # Skru paa en LED
    def light_led(self, led_number):
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)

    # Flash leds som feilmelding
    def flash_all_leds(self):
        for i in range(0, 6):
            for j in range(1, 10000):
                self.light_led(j % 6)
            self.clear_leds()
            time.sleep(.200)
    
    # Blinke alle leds som positiv tilbakemelding
    def twinkle_all_leds(self):
        for i in range(0, 20):
            self.light_led(random.randint(0, 5))
            time.sleep(.100)
        self.clear_leds()

    # lysshow naar man skrur av
    def power_off(self):
        for i in range(6, 0, -1):
            for dur in range(0, 10000):
                for j in range(0, i):
                    self.light_led(j)
        self.clear_leds()

    # lysshow naar man skrur paa
    def power_on(self):
        for i in range(1, 7):
            for j in range(0, 10000):
                for k in range(0, i):
                    self.light_led(k)

        self.clear_leds()

