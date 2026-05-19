#!/usr/bin/env python3

import random

PLAYERS = [
    'Alice',
    'bob',
    'Charlie',
    'dylan',
    'Emma',
    'Gregory',
    'john',
    'kevin',
    'Liam',
]


def main() -> None:
    print('=== Game Data Alchemist ===')
    print()
    print(f"Inital list of players: {PLAYERS}")
    print()
    capitalized = [name.capitalize() for name in PLAYERS]
    print(f"New list with all names capitalized: {capitalized}")
    print()
    only_capital = [name for name in PLAYERS if name[0].isupper()]
    print(f'New list of capitalized names only: {only_capital}')
    print()
    score_dict = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {score_dict}")
    print()
    score_avg = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {score_avg}")
    high_scores = {
        name: score_dict[name]
        for name in capitalized
        if score_dict[name] > score_avg
        }
    print(f'High scores: {high_scores}')


if __name__ == '__main__':
    main()
