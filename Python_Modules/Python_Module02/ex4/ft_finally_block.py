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


def water_plant(plant_name: str):
    if islower(plant_name):
        raise PlantError(f"Caught PlantError: Invalid plant name to water: {plant_name}")

def test_watering_system() -> None:
    print("Opening watering system")
    for plants in [water_plant("Tomato"), water_plant("Lettuce"), water_plant("Carrots")]:
        try:
