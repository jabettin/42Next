#!/usr/bin/env python3

import abc
import typing


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def ingest(self, data: Any) -> None:
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