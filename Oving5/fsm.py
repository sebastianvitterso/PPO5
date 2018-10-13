import re
from inspect import isfunction
from agent import*

class FSM:
    def __init__(self):
        self.agent = AgentProxy()
        self.states = [[Rule("Wakeup", 0, 1, signal_is_digit , self.agent.reset_pw_acc1())]]
        self.current_state = 0
        self.current_signal = None;
    
    def add_rule(self, name, state1, state2, signal, action):
        new_rule = Rule(name, state1, state2, signal, action);
        self.states[state1].append(new_rule);

    def get_next_signal(self):
        self.current_signal = self.agent.get_next();

    def run_rules(self):
        for rule in self.states[self.current_state]:
            if self.apply_rule(rule):
                self.fire_rule(rule);
                return;

    def apply_rule(self, rule):
        # Her må vi legge til logikk for å sjekke om regelen skal brukes
        if self.current_state == rule.state1:
            if rule.symbol(self.current_signal):
                return True;
            
        return False;

    def fire_rule(self, rule):
        self.current_state = rule.state2;
        # Her må vi gjøre noe for å kalle regelen sin handling
        rule.action(self.agent, self.current_symbol);

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

def signal_is_digit(signal):
    return 48 <= ord(signal) <= 57;

def signal_is_asterisk(signal):
    return ord(signal) == 42;

def signal_is_pound(signal):
    return ord(signal) == 35;

if __name__ == "__main__":
    fsm = FSM()



