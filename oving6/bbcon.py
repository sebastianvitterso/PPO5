from arbitrator import *
import time

class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator(self)


    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior in self.behaviors and behavior not in self.active_behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        for sensob in sensobs:
            sensob.update()

        for behavior in behaviors:
            behavior.update()

        self.arbitrator.choose_action_deterministic()

        for motob in motobs:
            motob.update()

        time.sleep(.05)

        for sensob in sensobs:
            sensob.reset()
        '''
        - Update all relevant sensobs
        - Update all behaviors
        - Invoke arbitrator (self.arbitrator.choose_action)
        - Update all motobs
        - Wait
        - Reset sensobs
        '''
