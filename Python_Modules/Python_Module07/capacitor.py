from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print("base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print("base: ")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print("evolved: ")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


healing_creatures = HealingCreatureFactory()
print("Testing Creature with healing capabilty")
test_healing(healing_creatures)
print()
transform_creatures = TransformCreatureFactory()
print("Testing Creature with transform capability")
test_transform(transform_creatures)
