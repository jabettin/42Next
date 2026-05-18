#!/usr/bin/env python3

import random

ALL_ACHIEVEMENTS = [
    "First Steps", "Speed Runner", "Untouchable", "Survivor",
    "Boss Slayer", "World Savior", "Master Explorer", "Treasure Hunter",
    "Collector Supreme", "Crafting Genius", "Strategist", "Unstoppable",
    "Sharp Mind", "Hidden Path Finder", "Dragon Slayer", "Night Owl",
    "Team Player",
]

def gen_player_achievements() -> set[str]:
    count = random.randint(5, 9)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main() -> None:
    print('=== Achievement Tracker System ===')
    players: dict[str, set[str]] = {
        'Alice': gen_player_achievements(),
        'Bob': gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan': gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set(ALL_ACHIEVEMENTS)
    player_sets = list(players.values())

    all_unlocked: set[str] = set()
    for achievements in player_sets:
        all_unlocked = all_unlocked.union(achievements)

if __name__ == '__main__':
    main()