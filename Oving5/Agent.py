
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

    def reset_pw_acc1(self):  # a1
        self.passcode_login = ""

    def append_digit(self, char):  # a2
        self.passcode_login += char

    def verify_pw_login(self):  # a3
        boolean = self.passcode_login == self.passcode_saved
        if boolean:
            return "Y"
        else:
            return "N"

    def reset_agent(self):  # a4
        self.passcode_login = ""
        self.passcode_change1 = ""
        self.passcode_change2 = ""

    def fully_activate_agent(self):  # a5
        # lysshow for suksess
        pass




