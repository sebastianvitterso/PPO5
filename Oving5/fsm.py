import re
from inspect import isfunction


class FSM:
    def __init__(self):
        self.states = [[Rule("Wakeup", 0, 1, r"\d" , reset_password_accumulator)]]
        self.current_state = 0
        self.current_signal


class Rule:
    def __init__(self, name, state1, state2, signal, action):
        self.name = name
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action

    def __str__(self):
        print(self.name + str(self.state1) + "->" + str(self.state2) + str(self.signal) + str(self.action))


if __name__ == "__main__":
    fsm = FSM()

