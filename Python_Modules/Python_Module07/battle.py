#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


flame_factory = FlameFactory()
aqua_factory = AquaFactory()
print("Testing factory")
test_factory(flame_factory)
print()
print("Testing factory")
test_factory(aqua_factory)
print()


def test_battle(fctry_a: CreatureFactory, fctry_b: CreatureFactory) -> None:
    creature_a = fctry_a.create_base()
    creature_b = fctry_b.create_base()
    print(creature_a.describe())
    print("vs.")
    print(creature_b.describe())
    print("fight!")
    print(creature_a.attack())
    print(creature_b.attack())


print("Testing battle")
test_battle(flame_factory, aqua_factory)
