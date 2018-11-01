from arbitrator import Arbitrator
import time
from behavior import Behavior
from motob import Motob
from sensob import Sensob
from reflectance_sensors import ReflectanceSensors

class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator(self)
        self.setup()

    def setup(self):
        m = motob()
        ps = sensob()
        ir = sensob()


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
        for sensob in self.sensobs:
            sensob.update()

        for behavior in self.behaviors:
            behavior.update()

        self.arbitrator.choose_action_deterministic()

        for motob in self.motobs:
            motob.update()

        time.sleep(.05)

        for sensob in self.sensobs:
            sensob.reset()
        '''
        - Update all relevant sensobs
        - Update all behaviors
        - Invoke arbitrator (self.arbitrator.choose_action)
        - Update all motobs
        - Wait
        - Reset sensobs
        '''


if __name__ == "__main__":
    b = BBCON()
