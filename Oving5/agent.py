
class Agent:

    def __init__(self, keypad, ledboard):
        self.keypad = keypad
        self.ledboard = ledboard
        self.passcode_saved = "1234"
        self.passcode_login = ""
        self.passcode_change1 = ""
        self.passcode_change2 = ""
        self.override_signal = 0
        self.selected_led = 0
        self.led_duration = ""

    def set_override(self, num):
        self.override_signal = num

    def get_next(self):  # må kanskje modifiseres, om keypad kun gir tilbake col/row
        if self.override_signal == 0:
            while True:
                if self.keypad.current_keypress is not None:
                    return self.keypad.current_keypress
        elif self.override_signal == 1:
            var = self.verify_login_2()
            self.override_signal = 0
            return var
        else:
            return "Override signal not 0 or 1"

    def pass_function(self, char):  # a0
        pass

    def reset_pw_acc1(self, char):  # a1
        self.passcode_login = ""

    def append_digit(self, char):  # a2
        self.passcode_login += char

    def verify_login(self, char):  # a3
        self.override_signal = 1

    def verify_login_2(self):
        if self.passcode_login == self.passcode_saved:
            # lysshow
            return "Y"
        else:
            # blinkelys
            return "N"

    def reset_agent(self, char):  # a4
        self.passcode_login = ""
        self.passcode_change1 = ""
        self.passcode_change2 = ""

    def fully_activate_agent(self, char):  # a5
        # lysshow
        print("Access Granted!")
        pass

    def reset_change_1(self, char):  # a6
        self.passcode_change1 = ""

    def reset_change_2(self, char):  # a7
        self.passcode_change2 = ""

    def append_digit_change_1(self, char):  # a8
        self.passcode_change1 += char

    def append_digit_change_2(self, char):  # a9
        self.passcode_change2 += char

    def verify_change_inputs(self, char):  # a10
        if self.passcode_change1 == self.passcode_change2:
            # lysshow
            self.passcode_saved = self.passcode_change1
        else:
            # blinkelys
            self.reset_both_changers("")

    def reset_both_changers(self, char):  # a11
        # blinkelys
        self.reset_change_1("")
        self.reset_change_2("")

    def select_led(self, char):
        self.selected_led = int(char)

    def append_duration(self, char):
        self.led_duration += char

    def execute_led(self, char):
        pass

    def clear_duration(self, char):
        pass

    def verify_change_input(self, char):
        pass


class AgentProxy(Agent):

    def __init__(self):
        Agent.__init__(self, None, None)

    def get_next(self):
        if self.override_signal == 0:
            return input("Skriv inn et tall som skal gis til FSM: ")
        elif self.override_signal == 1:
            var = self.verify_login_2()
            self.override_signal = 0
            return var
        else:
            return "Override signal not 0 or 1"


