#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, initial_height: float, initial_age: int) -> None:
        self.name = name
        self.initial_height = initial_height
        self.initial_age = initial_age
    def show(self) -> None:
        print(f"Created: {self.name}: {self.initial_height}cm, {self.initial_age} days old")
    def grow(self) -> None:
        self.initial_height += 0.8

if __name__ == '__main__':
    plants = {
        "Rose": Plant("Rose", 25.0, 21),
        "Sunflower": Plant("Sunflower", 44.3, 19),
        "Cactus": Plant("Cactus", 33.1, 30),
        "Lilly": Plant("Lilly", 13.5, 18),
        "Poppy": Plant("Poppy", 15.2, 24),
    }
    print("=== Plant Factory Output ===")
    for plant in plants.values():
        plant.show()




