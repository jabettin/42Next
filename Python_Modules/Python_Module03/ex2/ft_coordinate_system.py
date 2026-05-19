#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(',')
        if len(parts) == 3:
            try:
                converted = []
                for part in parts:
                    converted.append(float(part))
                return (converted[0], converted[1], converted[2])
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
        else:
            print("Invalid syntax")


if __name__ == '__main__':
    print('=== Game Coordinate System ===')
    print()
    print('Get a first set of coordinates')
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: {(x1, y1, z1)}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {round(math.sqrt(x1**2 + y1**2 + z1**2), 4)}")
    print()
    print('Get a second set of coordinates')
    x2, y2, z2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)}")
