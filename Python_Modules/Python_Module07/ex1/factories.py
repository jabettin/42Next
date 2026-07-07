from ex0 import Creature, CreatureFactory
from .capabilities import HealCapability, TransformCapability

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()


class Sproutling(Creature, HealCapability):
    pass


class Bloomelle(Creature, HealCapability):
    pass








