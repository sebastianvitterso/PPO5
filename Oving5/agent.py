from led_board import *
from keypad import *


class Agent:

    def __init__(self):
        self.passcode_location = "passcode.txt"
        self.passcode_login = ""
        self.passcode_change1 = ""
        self.passcode_change2 = ""
        self.override_signal = 0
        self.selected_led = 0
        self.led_duration = ""
        self.led_board = LED_Board()
        self.key_pad = Keypad()

        self.led_board.setup()

    def set_override(self, num):
        self.override_signal = num

    def get_next(self):  # henter/venter på signal fra keypad
        if self.override_signal == 0:
            while True:
                signal = self.key_pad.get_signal()
                if signal is not None:
                    return signal
        elif self.override_signal == 1: # med mindre fsm har sendt override, og venter på en verification av login
            var = self.verify_login_2()
            self.override_signal = 0
            return var
        else:
            return "Override signal not 0 or 1" # skal ikke skje.

    def pass_function(self, char):  # tom funksjon, ikke brukt, men brukt i debug
        pass

    def reset_pw_acc1(self, char):  # kalles naar man skrur paa maskina
        self.led_board.power_on()
        self.passcode_login = ""

    def append_digit(self, char):  # legg til et tall i passordforsoeket
        self.passcode_login += char

    def verify_login(self, char):  # sjekk passordlogin
        self.override_signal = 1

    def verify_login_2(self): # kjoreres når overriden er satt til 1
        file = open(self.passcode_location, 'r')
        current_passcode = file.read().strip()
        file.close()
        if self.passcode_login == current_passcode: # hvis rett
            self.led_board.twinkle_all_leds()
            return "Y"
        else:   # hvis feil
            self.led_board.flash_all_leds()
            return "N"

    def reset_agent(self, char):  # hvis feil
        self.led_board.power_off()
        self.passcode_login = ""
        self.passcode_change1 = ""
        self.passcode_change2 = ""

    def fully_activate_agent(self, char):  # hvis rett
        self.led_board.twinkle_all_leds()
        print("Access Granted!")

    def reset_change_1(self, char):  # runs when you try to change, inputting first time, but cancel it.
        self.passcode_change1 = ""

    def reset_change_2(self, char):  # runs when you try to change, inputting second time, but cancel it.
        self.passcode_change2 = ""

    def append_digit_change_1(self, char):  # append digit to first passwordchange
        self.passcode_change1 += char

    def append_digit_change_2(self, char):  # append digit to second passwordchange
        self.passcode_change2 += char

    def verify_change_inputs(self, char):  # verifies the two change-inputs, if they are the same, change the file
        if self.passcode_change1 == self.passcode_change2:
            self.led_board.twinkle_all_leds()
            file = open(self.passcode_location, 'w')
            file.write(self.passcode_change1)
            file.close()
            # self.passcode_saved = self.passcode_change1
        else:
            self.led_board.flash_all_leds()
            self.reset_both_changers("")

    def reset_both_changers(self, char):  # when cancelling passcode-change, this fires
        self.led_board.flash_all_leds()
        self.reset_change_1("")
        self.reset_change_2("")

    def select_led(self, char):  # from input, select led from 1-6
        self.selected_led = int(char)-1
        print("Turning on LED.")

    def append_duration(self, char):  # from input, append (stringwise) the duration of led-light
        self.led_duration += char

    def execute_led(self, char):  # from previous settings, fire led.
        print("Turned on LED ", str(self.selected_led), " for ", str(self.led_duration), " seconds.")
        duration = int(self.led_duration)

        self.led_duration = ""

        self.led_board.light_led(self.selected_led)
        time.sleep(duration)
        self.led_board.clear_leds()
        print("Turned off LED.")

    def clear_duration(self, char):  # fired upon cancelling led-light.
        self.led_board.flash_all_leds()
        self.led_duration = ""

    def logout(self, char):  # logout by two pound signs
        self.led_board.power_off()
        print("Logout Succesful!")

    def verify_logout(self, char):  # after first pound sign
        print("Are you sure you want to log out?")

    def cancel_logout(self, char):  # if no second pound sign
        print("Logout cancelled!")


class AgentProxy(Agent):  # only used for debug

    def __init__(self):
        Agent.__init__(self)

    def get_next(self):
        if self.override_signal == 0:
            return str(input("Skriv inn et tall som skal gis til FSM: "))
        elif self.override_signal == 1:
            var = self.verify_login_2()
            self.override_signal = 0
            return var
        else:
            return "Override signal not 0 or 1"


