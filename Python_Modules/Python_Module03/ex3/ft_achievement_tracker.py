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
    print()

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()

    all_achievements: set[str] = set(ALL_ACHIEVEMENTS)
    player_sets = list(players.values())

    all_unlocked: set[str] = set()
    for achievements in player_sets:
        all_unlocked = all_unlocked.union(achievements)
    print(f"All distinct achievements: {all_unlocked}")
    print()

    common = player_sets[0]
    for achievements in player_sets[1:]:
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")
    print()

    for name, achievements in players.items():
        others_union: set[str] = set()
        for other_name, other_set in players.items():
            if other_name != name:
                others_union = others_union.union(other_set)
        exclusive = achievements.difference(others_union)
        print(f"Only {name} has: {exclusive}")
    print()

    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == '__main__':
    main()
