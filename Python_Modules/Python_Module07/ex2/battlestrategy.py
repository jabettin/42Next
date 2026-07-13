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

    def _require_valid(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature._name}' for this {type(self).__name__.lower()}")


class InvalidStrategyError(Exception):
    ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        self._require_valid(creature)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        self._require_valid(creature)
        print(creature.attack())
        print(creature.heal())
