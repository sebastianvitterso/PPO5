import RPi.GPIO as GPIO
import time
import random


class LED_Board:
    def __init__(self):
        self.pins = [19, 13, 6]
        self.pin_led_states = [
                [1, 0, -1], # 1
                [0, 1, -1], # 2
                [1, -1, 0], # 3
                [0, -1, 1], # 4
                [-1, 1, 0], # 5
                [-1, 0, 1]  # 6
            ]

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in range(0, 3):
            GPIO.setup(self.pins[i], GPIO.OUT)

    def set_pin(self, pin_index, pin_state):
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def clear_leds(self):
        # Skru foerst av alle LEDs
        for i in range(0, 3):
            GPIO.setup(self.pins[i], GPIO.OUT)
            GPIO.output(self.pins[i], GPIO.LOW)

    def light_led(self, led_number):
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)

    #def light_led(self, light):
        #self.clear_leds()
        # Skru paa den valgte LEDen
        #for i in range(0,3):
            #self.set_pin(i, light)

    def flash_all_leds(self):
        for i in range(0, 6):
            for j in range(1, 10000):
                self.light_led(j % 6)
            self.clear_leds()
            time.sleep(.200)
    
    def twinkle_all_leds(self):
        for i in range(0, 60):
            self.light_led(random.randint(0, 5))
            time.sleep(.100)
        self.clear_leds()

    def power_off(self):
        for i in range(0, 6):
            self.light_led(i)
        time.sleep(.400)
        self.clear_leds()
        for i in range(0, 5):
            self.light_led(i)
        time.sleep(.400)
        self.clear_leds()
        for i in range(0, 4):
            self.light_led(i)
        time.sleep(.400)
        self.clear_leds()
        for i in range(0, 3):
            self.light_led(i)
        time.sleep(.400)
        self.clear_leds()
        for i in range(0, 2):
            self.light_led(i)
        time.sleep(.400)
        self.clear_leds()
        self.light_led(0)
        time.sleep(.400)
        self.clear_leds()

    def power_on(self):
        self.twinkle_all_leds()

