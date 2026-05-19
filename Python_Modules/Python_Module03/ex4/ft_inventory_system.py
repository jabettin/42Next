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
        print(f"Got inventory: {INVENTORY}")
        inventory_keys = list(INVENTORY.keys())
        print(f"Item list: {inventory_keys}")
        total_values = sum(INVENTORY.values())
        print(f"Total quantity of the {len(inventory_keys)} items: {total_values}")
        for item, quantity in INVENTORY.items():
            print(f"Item {item} represents {round(quantity / total_values * 100, 1)}%")
        max_item, max_qty = list(INVENTORY.items())[0]
        min_item, min_qty = list(INVENTORY.items())[0]
        for item, quantity in INVENTORY.items():
            if  quantity > max_qty:
                max_item = item
                max_qty = quantity
            if quantity < min_qty:
                min_item = item
                min_qty = quantity
        print(f"Item most abundant: {max_item} with quantity {max_qty}")
        print(f"Item least abundant: {min_item} with quantity {min_qty}")
        INVENTORY.update({'magic_item': 1})
        print(f"Updated inventory: {INVENTORY}")


if __name__ == '__main__':
    main()
