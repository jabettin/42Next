#!/usr/bin/env python3
import json

class Plant:
    def __init__(
        self, name: str, height: float, age: int
    ) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, "
              f"{self.age} days old")

    def grow(self) -> None:
        self.height += 0.8


def factory(data: list[dict]) -> list[Plant]:
    result = []
    for x in data:
        obj = Plant(**x)
        result.append(obj)
    return result


if __name__ == '__main__':
    with open("/home/jabettin/Desktop/GitHub/Python_Modules/Python_Module01/ex3/plants.json") as f:
        plant_data = json.load(f)

    print("raw from file: ", plant_data)
    print()

    plants = factory(plant_data)
    print("after factory: ", plants)
    print()


    print("=== Plant Factory Output ===")
    for x in plants:
        x.show()
