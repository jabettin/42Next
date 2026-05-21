#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    argc = len(sys.argv)
    if argc == 2:
        print('=== Cyber Archives Recovery ===')
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            f = open(sys.argv[1])
            filename = sys.argv[1]
            print('---')
            print()
            print(f.read())
            print()
            print('---')
        except OSError as e:
            print(f"Error opening file '{filename}': {e}")
        print(f"File {filename} closed.")
        finally:
            f.close(filename)
    else:
        print('Usage: ft_ancient_text.py <file>')


if __name__ == '__main__':
    main()
