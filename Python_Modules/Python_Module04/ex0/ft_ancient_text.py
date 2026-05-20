#!/usr/bin/env python3

import sys
import typing




def main() -> None:
    with open("Python_Modules/Python_Module04/ex0/text.txt") as f:
        reader = f.read
        print(reader)


if __name__ == '__main__':
    main()
