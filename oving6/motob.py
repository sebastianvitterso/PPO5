from motors import Motors
class Motob:
    def __init__(self):
        self.motors = Motors()
        self.value = None

    def update(self, motor_recommendation):
        self.value = motor_recommendation
        self.operationalize()

    def operationalize(self):
        
