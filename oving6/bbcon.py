from arbitrator import Arbitrator
import time
from behavior import *
from motob import Motob
from sensob import *
from reflectance_sensors import ReflectanceSensors
from irproximity_sensor import IRProximitySensor
from ultrasonic import Ultrasonic

class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator(self)
        self.setup()

    def setup(self):
        rs = ReflectanceSensors()
        #ir = IRProximitySensor()
        us = Ultrasonic()
        rsob = ReflectanceSensob(rs)
        #irob = IRProximitySensob()
        usob = UltrasonicSensob(us)
        self.add_sensob(rsob)
        self.add_sensob(usob)
        forwardb = ForwardBehavior()
        self.add_behavior(forwardb)


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
