#!/usr/bin/env python3

import sys

INVENTORY = {}

def main() -> None:
    print('=== Inventory System Analysis ===')
    argc = len(sys.argv)
    if argc == 1:
        print('No arguments provided Usage: python3 ft_inventory_system <item_name>:<quantity> ...')
    else:
        for key, value in sys.argv[1:]:
            INVENTORY.key() == str(key)
            INVENTORY.values() == int(value)

if __name__ == '__main__':
    main()