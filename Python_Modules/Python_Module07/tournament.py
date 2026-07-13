from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i, (factory_a, strategy_a) in enumerate(opponents):
        for factory_b, strategy_b in opponents[i + 1:]:
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")
            try:
                

