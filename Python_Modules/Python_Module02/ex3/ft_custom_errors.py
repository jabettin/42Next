#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"{self.message}"

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)

def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError as: {e}")

def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        raise WaterError("Not Enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError as {e}")

def test_garden_error() -> None:
    print("Testing catching all the garden errors...")
    for error in [PlantError("The tomato plant is wilting!"),
                  WaterError("Not enough water in the tank!")]:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError as: {e}")


if __name__ == '__main__':
    print ("=== Custom garden Errors Demo ===")
    test_plant_error()
    print()
    test_water_error()
    print()
    test_garden_error()
    print()
    print("All custom error types work correctly!")
