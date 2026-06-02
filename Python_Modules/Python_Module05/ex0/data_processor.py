#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    def output(self) -> tuple[int, str]:
        pass



class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._rank: int = 0

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception ('Improper numeric data')
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._data.append(str(item))
            self._rank += 1
        

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)










class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass

def main() -> None:
    print('=== Code Nexus - Data Processor ===')
    print()
    print('Testing Numeric Processor...')
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    try:
        np.ingest('foo')
    except Exception as e:
        print(f"Got exception: {e}")
    np.ingest([1, 2, 3, 4, 5])
    for _ in range(4):
        np.output()

if __name__ == '__main__':
    main()