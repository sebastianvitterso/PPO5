import RPi.GPIO as GPIO
import time


class Keypad:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        self.rowpins = [18, 23, 24, 25]

        self.colpins = [17, 27, 22]

        for row in self.rowpins:
            GPIO.setup(row, GPIO.OUT)

        for column in self.colpins:
            GPIO.setup(column, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        self.signals = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9'],
                        ['*', '0', '#']]

    def get_signal(self):
        for row in self.rowpins:
            GPIO.output(row, GPIO.HIGH)

            for col in self.colpins:
                if self.poll_button(col):
                    return self.signals[row][col]

            GPIO.output(row, GPIO.LOW)

        return None

    def poll_button(self, col):
        for i in range(0, 20):
            if GPIO.input(col) != GPIO.LOW:
                return False

            time.sleep(20)

        return True

