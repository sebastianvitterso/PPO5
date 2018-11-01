from motors import Motors
class Motob:
    def __init__(self):
        self.motors = Motors()
        self.motors.setup()
        self.value = None

    
    # Motor recommendation format:
    # (F/B, [0, 1])  - Forward/backward, speed 0-1
    # (L/R, [0, 180]) - Left/right, 0-180 degrees
    def update(self, motor_recommendation):
        if motor_recommendation[0] == 'F':
            self.value = (motor_recommendation[1], motor_recommendation[1])
        else if motor_recommendation[0] == 'B':
            self.value = (-motor_recommentaion[1], -motor_recommendation[1])
        else if motor_recommendation[0] == 'R':
            self.value = (0.5, 0)
        else if motor_recommendation[0] == 'L':
            self.value = (0, 0.5)

        self.operationalize()

    def operationalize(self):
        self.motors.set_value(self.value)
             
