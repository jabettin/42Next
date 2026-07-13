from ex0 import Creature
from ex1 import HealCapability, TransformCapability

class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal"

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike!"
        else:
            return f"{self._name} attacks normally."