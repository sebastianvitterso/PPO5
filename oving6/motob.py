from motors import Motors


class Motob:
    def __init__(self):
        self.motors = Motors()
        self.value = None

    # Motor recommendation format:
    # (F/B, [0, 1])  - Forward/backward, speed 0-1
    # (L/R, [0, 180]) - Left/right, 0-180 degrees
    def update(self, motor_recommendation):
        print(motor_recommendation)
        if motor_recommendation[0] == 'F':
            self.value = (motor_recommendation[1], motor_recommendation[1])
        elif motor_recommendation[0] == 'B':
            self.value = (-motor_recommendation[1], -motor_recommendation[1])
        elif motor_recommendation[0] == 'R':
            if motor_recommendation[1] == 1:
                self.value = (0.4, 0)
            elif motor_recommendation[1] == 2:
                self.value = (0.4, -0.4)
            elif motor_recommendation[1] == 3:
                self.value = (0.3, -0.3)
            elif motor_recommendation[1] == 4;
                self.value = (0.4, 0)
        elif motor_recommendation[0] == 'L':
            if motor_recommendation[1] == 1:
                self.value = (0, 0.4)
            elif motor_recommendation[1] == 2:
                self.value = (-0.4, 0.4)
            elif motor_recommendation[1] == 3:
                self.value = (-0.3, 0.3)
            elif motor_recommendation[1] == 4:
                self.value = (0, 0.4)

        self.operationalize()

    def operationalize(self):
        self.motors.set_value(self.value)

    def stop(self):
        self.motors.stop()
