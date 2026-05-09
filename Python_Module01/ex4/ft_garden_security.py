#!/usr/bin/env python3
class Plant:
    name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"Plant created: {self.name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")


if __name__ == '__main__':
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-1)
    print(f"Current state: {rose.name}: {rose.get_height()}cm, {rose.get_age()} days old")
