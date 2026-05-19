#!/usr/bin/env python3

import sys


def main() -> None:
    INVENTORY = {}
    print('=== Inventory System Analysis ===')
    argc = len(sys.argv)
    if argc == 1:
        print('No arguments provided Usage: python3'
              'ft_inventory_system <item_name>:<quantity> ...')
    else:
        for arg in sys.argv[1:]:
            parts = arg.split(':')
            if parts[0] in INVENTORY:
                print(f"Redundant item '{parts[0]}' - discarding")
                continue
            if len(parts) != 2:
                print(f"Error - invalid parameter '{arg}'")
                continue
            try:
                int(parts[1])
            except ValueError as e:
                print(f"Quantity error for '{parts[0]}': {e}")
                continue
            INVENTORY[parts[0]] = int(parts[1])


if __name__ == '__main__':
    main()
