from arbitrator import Arbitrator
import time
from behavior import *
from motob import Motob
from sensob import *
from reflectance_sensors import ReflectanceSensors
from irproximity_sensor import IRProximitySensor
from ultrasonic import Ultrasonic
from camera import Camera


class BBCON:
    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motob = Motob()
        self.arbitrator = Arbitrator(self)
        self.setup()

    def setup(self):
        #Forward Behavior
        forwardb = ForwardBehavior(self, [], False, 0.2)
        self.add_behavior(forwardb)
        self.activate_behavior(forwardb)

        #LineBehavior
        rs = ReflectanceSensors()
        rsob = ReflectanceSensob(rs)
        lineb = FollowLineBehavior(self, [rsob], False, 0.9)
        self.add_behavior(lineb)
        self.activate_behavior(lineb)
        self.add_sensob(rsob)

        camera = Camera()
        followgreenb = FollowGreenFlask(self, [camera], False, 0.9)


        #Avoid Collision
        #us = Ultrasonic()
        #usob = UltrasonicSensob(us)
        #self.add_sensob(usob)
        #avoidb = AvoidCollisionBehavior(self, [usob], False, 0.8)
        #self.add_behavior(avoidb)
        #self.activate_behavior(avoidb)

        #ir = IRProximitySensor()
        #irob = IRProximitySensob()


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

        motor_recommendation = self.arbitrator.choose_action_deterministic()

        self.motob.update(motor_recommendation)

        time.sleep(.1)

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

    def stop(self):
        self.motob.stop()


if __name__ == "__main__":
    b = BBCON()
    time.sleep(2)
    while True:
        b.run_one_timestep()
