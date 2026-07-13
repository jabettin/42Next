from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        ...

    @abstractmethod
    def act(self) -> None:
        ...


    class NormalStrategy(BattleStrategy):
        def act(self) -> None:
            creature

    
    class AggressiveStrategy(BattleStrategy):
        ...

    
    class DefensiveStrategy(BattleStrategy):
        ...

    
