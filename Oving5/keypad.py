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
        for row in range(0,4):
        #for row in self.rowpins:
            GPIO.output(self.rowpins[row], GPIO.HIGH)
            for col in range(0,3):
            #for col in self.colpins:
                if self.poll_button(self.colpins[col]):
                    GPIO.output(self.rowpins[row], GPIO.LOW)
                    return self.signals[row][col]

            GPIO.output(self.rowpins[row], GPIO.LOW)
        return None

    def poll_button(self, col):
        for i in range(0, 20):
            if GPIO.input(col) != GPIO.HIGH:
                return False
            time.sleep(.010)
        return True

