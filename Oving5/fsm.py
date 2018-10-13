import re
from inspect import isfunction


class FSM:
    def __init__(self):
        self.states = [[Rule("Wakeup", 0, 1, r"\d" , reset_password_accumulator)]]
        self.current_state = 0
        self.current_signal
    
    def add_rule(self, name, state1, state2, signal, action):
        new_rule = Rule(name, state1, state2, signal, action);
        self.states[state1].append(new_rule);

    def get_next_signal(self):
        return True;

    def run_rules(self):
        return True;

    def apply_rule(self):
        return True;

    def fire_rule(self):
        return True;

    def main_loop(self):
        while True:
            self.current_signal = self.get_next_signal();
            self.run_rules();

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
