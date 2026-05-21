#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: ft_ancient_text.py <file>')
        return

    filename: str = sys.argv[1]
    f: typing.IO[str] | None = None

    print('=== Cyber Archives Recovery ===')
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename)
        print('---')
        print(f.read(), end='')
        print('---')
    except OSError as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if f is not None:
            f.close()
            print(f"File '{filename}' closed.")

    


if __name__ == '__main__':
    main()
