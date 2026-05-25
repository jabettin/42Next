#!/usr/bin/env python3

import abc
import typing


class DataProcessor(ABC):
    pass


class NumericProcessor(DataProcessor):
    pass


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass

def main() -> None:
    pass


if __name__ == '__main__':
    main()