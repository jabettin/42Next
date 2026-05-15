#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message: str = "Unknown Garden Error"):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"{self.message}"


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown Plant Error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(plant.capitalize())
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering sytem")
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in ["Tomato", "lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors")


if __name__ == '__main__':
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")
