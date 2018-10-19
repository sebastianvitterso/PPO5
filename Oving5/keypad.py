import RPi.GPIO as GPIO
import time


class Keypad:
    def __init__(self):
        # Initialiser GPIO
        GPIO.setmode(GPIO.BCM)

        # Pins som keypaden bruker for rader og kolonner
        self.rowpins = [18, 23, 24, 25]
        self.colpins = [17, 27, 22]

        # Initialiser pins
        for row in self.rowpins:
            GPIO.setup(row, GPIO.OUT)

        for column in self.colpins:
            GPIO.setup(column, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Signaler som skal sendes ut for hver knapp
        self.signals = [['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9'],
                        ['*', '0', '#']]
    
    # Hent signal fra keypaden
    def get_signal(self):
        # Gaa gjennom alle rader og kolonner og sjekk om 
        # noen av knappene er trykket inn.
        for row in range(0,4):
            GPIO.output(self.rowpins[row], GPIO.HIGH)
            for col in range(0,3):
                if self.poll_button(self.colpins[col]):
                    GPIO.output(self.rowpins[row], GPIO.LOW)
                    return self.signals[row][col]

            GPIO.output(self.rowpins[row], GPIO.LOW)
        return None

    # Poll en knapp 20 ganger med 10ms mellomrom for a fjerne jitter
    def poll_button(self, col):
        for i in range(0, 20):
            if GPIO.input(col) != GPIO.HIGH:
                return False
            time.sleep(.010)
        return True

