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
    Alice