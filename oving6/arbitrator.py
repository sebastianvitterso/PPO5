from random import uniform

class Arbitrator:
    def __init__(self, bbcon):
        self.bbcon = bbcon

    def choose_action_deterministic(self):  # non-stochastic
        chosen_behavior = None
        for behavior in self.bbcon.active_behaviors:
            if behavior.priority > chosen_behavior.priority:
                chosen_behavior = behavior
        temptuple = (chosen_behavior.motor_recommendations, chosen_behavior.halt_request)
        return temptuple

    def choose_action_stochastic_linear(self):
        chosen_behavior = None
        range_top = 0
        for behavior in self.bbcon.active_behaviors:
            range_top += behavior.priority
        if range_top == 0:
            temptuple = (None, None)
            return temptuple
        random_choice = uniform(0, range_top)
        num = 0
        for behavior in self.bbcon.active_behaviors:
            num += behavior.priority
            if num >= random_choice:
                temptuple = (behavior.motor_recommendations, behavior.halt_request)
                return temptuple
        # if we dont get there, something is wrong.
        temptuple = (None, None)
        return temptuple



