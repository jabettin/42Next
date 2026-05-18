#!/usr/bin/env python3

import math

def get_player_pos() -> tuple:
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
            continue

if __name__ == '__main__':
    print('=== Game Coordinate System ===')
    print()
    print('Get a first set of coordinates')
    result = get_player_pos()
    print(result)
