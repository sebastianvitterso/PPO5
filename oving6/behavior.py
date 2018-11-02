import random

class Behavior:
    def __init__(self, bbcon, sensobs, halt_request, priority):
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.motor_recommendations = None
        self.active_flag = False
        self.halt_request = halt_request
        self.priority = priority
        self.match_degree = 0
        self.weight = 0

    def __str__(self):
        return type(self).__name__

    # Dersom en oppførsel er aktiv, skal den vurdere om den skal deaktivere seg selv
    def consider_deactivation(self):
        pass
    
    # Dersom en oppførsel er inaktiv, skal den vurdere som den skal aktivere seg selv
    def consider_activation(self):
        pass

    # Hovedgrensesnitt mellom bbcon og behaviour
    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()
        
        self.sense_and_act()

        self.weight = self.match_degree * self.priority

    # Gjør beregninger for å produsere motoranbefalinger og oppdatere match_degree
    def sense_and_act(self):
        pass


class NoneBehavior(Behavior):
    def __init__(self, bbcon, sensobs, halt_request, priority):
        Behavior.__init__(self, bbcon, sensobs, halt_request, priority)


class ForwardBehavior(Behavior):
    def __init__(self, bbcon, sensobs, halt_request, priority):
        Behavior.__init__(self, bbcon, sensobs, halt_request, priority)

    def consider_deactivation(self):
        '''if (putTest):  # hva er testen?
            self.bbcon.deactivate_behavior(self)
            self.active_flag = False
        else:
            pass'''
        pass

    def consider_activation(self):
        '''if (putTest):  # hva er testen?
            self.bbcon.activate_behavior(self)
            self.active_flag = True
        else:
            pass'''
        pass

    def sense_and_act(self):  # ForwardBehavior er veldig dum, så bruker ikke sanseinput
        self.motor_recommendations = ('F', 0.3)
        self.match_degree = 1


class AvoidCollisionBehavior(Behavior):
    def __init__(self, bbcon, sensobs, halt_request, priority):
        Behavior.__init__(self, bbcon, sensobs, halt_request, priority)

    def consider_deactivation(self):
        '''if (putTest):  # hva er testen?
            self.bbcon.deactivate_behavior(self)
            self.active_flag = False
        else:
            pass'''
        pass

    def consider_activation(self):
        '''if (putTest):  # hva er testen?
            self.bbcon.activate_behavior(self)
            self.active_flag = True
        else:
            pass'''
        pass

    def sense_and_act(self):
        if self.sensobs[0].sensor_value < 10:
            self.match_degree = 1
        else:
            self.match_degree = 0
        self.motor_recommendations = ('L', 30)


class FollowLineBehavior(Behavior):
    def __init__(self, bbcon, sensobs, halt_request, priority):
        Behavior.__init__(self, bbcon, sensobs, halt_request, priority)
        self.threshold = 0.2

    def sense_and_act(self):
        sensor_val = self.sensobs[0].sensor_value
        if sensor_val[0] < self.threshold and sensor_val[5] < self.threshold:
            # svart på begge sider
            self.match_degree = 0.5
            direction = random.choice(['R', 'L'])
            self.motor_recommendations = (direction, 2)
            print("heyah")
        elif sensor_val[0] < self.threshold:
            self.match_degree = 1
            self.motor_recommendations = ('L', 2)
        elif sensor_val[5] < self.threshold:
            self.match_degree = 1
            self.motor_recommendations = ('R', 2)
        elif sensor_val[2] < self.threshold and sensor_val[3] < self.threshold:
            self.motor_recommendations = ('F', 0.7)
            self.match_degree = 1
        elif sensor_val[2] < self.threshold:
            self.motor_recommendations = ('L', 1)
            self.match_degree = 1
        elif sensor_val[3] < self.threshold:
            self.motor_recommendations = ('R', 1)
            self.match_degree = 1
        else:
            self.motor_recommendations = ('F', 0.7)
            self.match_degree = 0.2

class FollowGreenFlask(Behavior):
    def __init__(self, bbcon, sensobs, halt_request, priority):
        Behavior.__init__(self, bbcon, sensobs, halt_request, priority)
    
    def sense_and_act(self):
        direction = self.sensobs[0].sensor_value # returnerer verdi fra 1-8, 0 betyr at den ikke ser noe grønt
        
        if direction > 0:
            if direction < 4:
                self.motor_recommendations = ('L', 45)
            elif direction > 5:
                self.motor_recommendations = ('R', 45)
            else:
                self.motor_recommendations = ('F', 0.5)

            self.match_degree = 0.9
        else:
            self.match_degree = 0.2
            self.motor_recommendations = ('R', 45)
