
class Agent:

    def __init__(self, keypad, ledboard):
        self.keypad = keypad
        self.ledboard = ledboard
        self.passcode_saved = "1234"
        self.passcode_login = ""
        self.passcode_change1 = ""
        self.passcode_change2 = ""

    def get_next(self):  # må kanskje modifiseres, om keypad kun gir tilbake col/row
        while True:
            if self.keypad.current_keypress is not None:
                return self.keypad.current_keypress

    def pass_function(self): # a0
        pass

    def reset_pw_acc1(self):  # a1
        self.passcode_login = ""

    def append_digit(self, char):  # a2
        self.passcode_login += char

    def verify_login(self):  # a3
        if self.passcode_login == self.passcode_saved:
            # lysshow
            return "Y"
        else:
            # blinkelys
            return "N"

    def reset_agent(self):  # a4
        self.passcode_login = ""
        self.passcode_change1 = ""
        self.passcode_change2 = ""

    def fully_activate_agent(self):  # a5
        # lysshow
        pass

    def reset_change_1(self):  # a6
        self.passcode_change1 = ""

    def reset_change_2(self):  # a7
        self.passcode_change2 = ""

    def append_digit_change_1(self, char):  # a8
        self.passcode_change1 += char

    def append_digit_change_2(self, char):  # a9
        self.passcode_change2 += char

    def verify_change_inputs(self):  # a10
        if self.passcode_change1 == self.passcode_change2:
            # lysshow
            self.passcode_saved = self.passcode_change1
        else:
            # blinkelys
            self.reset_both_changers()

    def reset_both_changers(self):  # a11
        # blinkelys
        self.reset_change_1()
        self.reset_change_2()


class AgentProxy(Agent):

    def __init__(self):
        super(Agent, self).__init__(None, None)

    def get_next(self):
        return input("Skriv inn et tall som skal gis til FSM: ")


