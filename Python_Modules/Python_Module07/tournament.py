from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i, (factory_a, factory_b) in enumerate(opponents)
    try:

