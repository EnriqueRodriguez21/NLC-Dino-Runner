from dino_runner.utils.constants import (
    SHIELD, SHIELD_TYPE, HAMMER, HAMMER_TYPE
)
from dino_runner.components.power_ups.power_ups.powerup import PowerUp


class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(Shield, self).__init__(self.image, self.type)


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super(Hammer, self).__init__(self.image, self.type)
