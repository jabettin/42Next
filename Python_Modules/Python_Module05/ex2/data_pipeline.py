#!/usr/bin/env python3

from typing import Any, Protocol
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    name: str = ""

    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception('Improper numeric data')
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._data.append((self._rank, str(item)))
            self._rank += 1


class TextProcessor(DataProcessor):
    name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception('Improper text data')
        items = data if isinstance(data, list) else [data]
        for item in items:
            self._data.append((self._rank, item))
            self._rank += 1


class LogProcessor(DataProcessor):
    name = "Log Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and
                all(isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items())
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception('Improper log data')
        items = data if isinstance(data, list) else [data]
        for item in items:
            log_str = f"{item['log_level']}: {item['log_message']}"
            self._data.append((self._rank, log_str))
            self._rank += 1


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(f"{proc.name}: total {proc._rank} items processed, "
                  f"fremaining: {len(proc._data)} on processor")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    ds = DataStream()
    np = NumericProcessor()
    lp = LogProcessor()
    tp = TextProcessor()
    ds.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    ds.register_processor(np)
    print()
    batch: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'user wil is connected'}
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()
    print()
    print("Registering other data processors")
    ds.register_processor(tp)
    ds.register_processor(lp)
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()
    print()
    print("Consume some elements from the "
          "data processors: Numeric 3, Text 2, log 1")
    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    for _ in range(1):
        lp.output()
    ds.print_processors_stats()


if __name__ == '__main__':
    main()
