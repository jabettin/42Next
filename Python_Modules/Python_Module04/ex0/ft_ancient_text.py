#!/usr/bin/env python3

import sys
import typing




def main() -> None:
    argc = len(sys.argv)
    if argc == 2:
        print('=== Cyber Archives Recovery ===')
        try:
            f = open(sys.argv[1])
            print(f"Accessing file '{sys.argv[1]}'")
            print('---')
            print()
            print(f.read())
            print()
            print('---')
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
    else:
        print('Usage: ft_ancient_text.py <file>')

if __name__ == '__main__':
    main()
