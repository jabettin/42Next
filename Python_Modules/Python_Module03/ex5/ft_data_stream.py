#!/usr/bin/env python3

import random
from typing import Generator

PLAYERS = [
    "bob",
    "alice",
    "dylan",
    "charlie",
]

ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event


def main() -> None:
    event_gen = gen_event()
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")
    print()
    events = [next(event_gen) for _ in range(10)]
    print(f"Built list of 10 events: {events}")
    print()

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == '__main__':
    main()
