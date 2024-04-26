
class Mist:
    RECOVERY_COOLDOWN = 3
    def __init__(self, active=True, recovery_cooldown=0):
        self.active = active
        self.count_down = recovery_cooldown

    def advance(self):
        if self.count_down > 0:
            self.count_down -= 1
        elif self.count_down == 0:
            self.active = True

    