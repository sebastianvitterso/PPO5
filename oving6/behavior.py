class Behavior:
    def __init__(self, bbcon, sensobs, halt_request, priority):
        self.bbcon = bbcon
        self.sensobs = sensobs
        self.motor_recommendations = []
        self.active_flag = False
        self.halt_request = halt_request
        self.priority = priority
        self.match_degree = 0
        self.weight = 0

    # Dersom en oppførsel er aktiv, skal den vurdere om den skal deaktivere seg selv
    def consider_deactivation(self):
        pass
    
    # Dersom en oppførsel er inaktiv, skal den vurdere som den skal aktivere seg selv
    def consider_activation(self):
        pass

    # Hovedgrensesnitt mellom bbcon og behaviour
    def update(self):
        # Oppdater activity status her

        self.sense_and_act()

        self.weight = self.match_degree * self.priority

    # Gjør beregninger for å produsere motoranbefalinger og oppdatere match_degree
    def sense_and_act(self):
        pass

