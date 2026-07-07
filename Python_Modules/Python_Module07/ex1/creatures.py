from ex0 import Creature
from .capabilities import HealCapability, TransformCapability


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


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stabilizes its form."

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        else:
            return f"{self._name} attacks normally."


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")
        HealCapability.__init__(self)

    def heal(self) -> str:
        return f"{self._name} heals itself for a small amount"

    def attack(self) -> str:
        return f"{self._name} uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def heal(self) -> str:
        return f"{self._name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self._name} uses Petal Dance!"
