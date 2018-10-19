#  import re
#  from inspect import isfunction
from agent import*


class FSM:
    def __init__(self):
        self.agent = Agent()
        self.states = []
        self.current_state = 0
        self.current_signal = ""
    
    def add_rule(self, name, state1, state2, signal, action):
        while len(self.states) <= state1:
            self.states.append([])
        new_rule = Rule(name, state1, state2, signal, action)
        self.states[state1].append(new_rule)

    def get_next_signal(self):
        self.current_signal = self.agent.get_next()

    def run_rules(self):
        for rule in self.states[self.current_state]:
            if self.apply_rule(rule):
                self.fire_rule(rule)
                return

    def apply_rule(self, rule):
        # Her maa vi legge til logikk for aa sjekke om regelen skal brukes
        if self.current_state == rule.state1:
            if rule.signal(self.current_signal):
                return True
            
        return False

    def fire_rule(self, rule):
        self.current_state = rule.state2
        # Her maa vi gjoere noe for aa kalle regelen sin handling
        rule.action(self.current_signal)

    def main_loop(self):
        while True:
            print("Current state: " + str(self.current_state))
            print("Current signal: " + str(self.current_signal))
            self.get_next_signal()
            self.run_rules()
            print("Current input-sequence: " + self.agent.passcode_login)


class Rule:
    def __init__(self, name, state1, state2, signal, action):
        self.name = name
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action

    def __str__(self):
        return self.name + " " + str(self.state1) + " -> " + str(self.state2) + str(self.signal) + str(self.action)


def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57


def signal_is_asterisk(signal):
    return ord(signal) == 42


def signal_is_pound(signal):
    return ord(signal) == 35


def give_true(signal):
    return True


def signal_is_Y(signal):
    return ord(signal) == ord("Y")


def signal_is_N(signal):
    return ord(signal) == ord("N")


def signal_is_led_number(signal):
    return 49 <= ord(signal) <= 54


if __name__ == "__main__":
    fsm = FSM()
    fsm.add_rule("Wakeup", 0, 1, signal_is_digit, fsm.agent.reset_pw_acc1)
    fsm.add_rule("AppendDigit", 1, 1, signal_is_digit, fsm.agent.append_digit)
    fsm.add_rule("GoToVerify", 1, 2, signal_is_asterisk, fsm.agent.verify_login)
    fsm.add_rule("GoToStart", 1, 0, give_true, fsm.agent.reset_agent)
    fsm.add_rule("Successverify", 2, 3, signal_is_Y, fsm.agent.fully_activate_agent)
    fsm.add_rule("FailureVerify", 2, 0, signal_is_N, fsm.agent.reset_agent)

    fsm.add_rule("Select LED", 3, 4, signal_is_led_number, fsm.agent.select_led)
    fsm.add_rule("Choose duration", 4, 4, signal_is_digit, fsm.agent.append_duration)
    fsm.add_rule("Execute LED action", 4, 3, signal_is_asterisk, fsm.agent.execute_led)
    fsm.add_rule("Cancel LED action", 4, 3, signal_is_pound, fsm.agent.clear_duration)

    fsm.add_rule("Change password", 3, 5, signal_is_asterisk, fsm.agent.pass_function)
    fsm.add_rule("Append digits to new password", 5, 5, signal_is_digit, fsm.agent.append_digit_change_1)
    fsm.add_rule("Finish new password", 5, 6, signal_is_asterisk, fsm.agent.pass_function)
    fsm.add_rule("Cancel password change in state 1", 5, 3, give_true, fsm.agent.reset_both_changers)
    fsm.add_rule("Enter password again", 6, 6, signal_is_digit, fsm.agent.append_digit_change_2)
    fsm.add_rule("Verify passwords match", 6, 3, signal_is_asterisk, fsm.agent.verify_change_inputs)
    fsm.add_rule("Cancel password change in state 2", 6, 3, give_true, fsm.agent.reset_both_changers)

    fsm.add_rule("Verify Logout", 3, 7, signal_is_pound, fsm.agent.verify_logout)
    fsm.add_rule("Logout final", 7, 0, signal_is_pound, fsm.agent.logout)
    fsm.add_rule("Cancel Logout", 7, 3, give_true, fsm.agent.cancel_logout)

    fsm.main_loop()



