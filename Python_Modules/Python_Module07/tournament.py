from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy, InvalidStrategyError,)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i, (factory_a, strategy_a) in enumerate(opponents):
        for factory_b, strategy_b in opponents[i + 1:]:
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print("now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
            print()


print("Tournament 0 (basic)")
opponents = [
    (FlameFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
]
print("[ (Flameling+Normal), (Healing+Defensive) ]")
battle(opponents)
print()
print("Tournament 1 (error)")
opponents = [
    (FlameFactory(), AggressiveStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
]
print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
battle(opponents)
print()
print("Tournament 2 (multiple)")
opponents = [
    (AquaFactory(), NormalStrategy()),
    (HealingCreatureFactory(), DefensiveStrategy()),
    (TransformCreatureFactory(), AggressiveStrategy())
]
print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
battle(opponents)
