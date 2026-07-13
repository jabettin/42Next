from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class InvalidStrategyError(Exception):
    ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isisnstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self._is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature._name}' for this aggressive strategy")
        print(creaure.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isisnstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self._is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature._name}' for this defensive strategy")
        print(creature.attack())
        print(creature.heal())
