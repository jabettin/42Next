from abc import ABC, abstractmethod


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        return f"{self._name} attacks normally"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self._transformed = True

    def revert(self) -> str:
        self._transformed = False

    def attack(self) -> str:
        if self._transformed == True:
            return f"{self._name} attacks normally"
        else:
            return f"{self._name} unleashes a devastating morph strike"

def testmorph(creature_a: Morphagon):
    creature_a = Morphagon()
    print(creature_a.describe())
    print(creature_a.attack())
    print(creature_a.transform())
    print(creature_a.attack())
    print(creature_a.revert())
    print(creature_a.attack())
def main():
    testmorph()
if __name__ == '__main__':
    main()
