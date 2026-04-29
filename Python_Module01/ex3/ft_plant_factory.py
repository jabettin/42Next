#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, initial_height: float, initial_age: int) -> None:
        self.name = name
        self.initial_height = initial_height
        self.initial_age = initial_age
    def show(self) -> None:
        print(f"Created: {self.name}: {self.initial_height}cm, {self.initial_age} days old")

if __name__ == '__main__':
    rose = Plant("Rose", 25.0, 21)
    sunflower = Plant("Sunflower", 44.3, 19)
    cactus = Plant("Cactus", 33.1, 30)
    lilly = Plant("Lilly", 13, 18)
    poppy = Plant("Poppy", 15, 24)
    print("=== Plant Factory Output ===")
    rose.show()
    sunflower.show()
    cactus.show()
    lilly.show()
    poppy.show()




