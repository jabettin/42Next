#!/usr/bin/env python3
class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.__class__._Stats()
    class _Stats:
        def __init__(self):
            self._grow = 0
            self._age = 0
            self._show = 0

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, {self._show} show")

    @staticmethod
    def more_than_year(age: int) -> bool:
        return age >= 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)
    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._Stats._show += 1

    def grow(self, amount: float = 0.8) -> None:
        self._height = round(self._height + amount, 1)
        self._stats._grow += 1

    def age(self, days: int = 1) -> None:
        self._age += days
        self._stats._age += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


    def bloom(self) -> None:
        print(f"[asking the {self._name.lower()} to bloom]")
        self._bloomed = True

class Tree(Plant):
    class _Stats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self._shade = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade} shade")

    def __init__(self, name: str, height: float, age: int, diameter: float) -> None:
        super().__init__(name, height, age)
        self._diameter = diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self._name.lower()} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._diameter}cm wide.")
        self._stats._shade += 1

class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")
        


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 20, 15, "blue")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print()
