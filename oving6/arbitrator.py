
class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self): # non-stochastic
        chosen_behavior = None
        for behavior in self.bbcon.active_behaviors:
            if behavior.priority > chosen_behavior.priority:
                chosen_behavior = behavior


