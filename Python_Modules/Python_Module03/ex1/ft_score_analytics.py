#!/usr/bin/env python3

import sys


if __name__ == '__main__':
    print('=== Player Score Analytics ===')
    argc = len(sys.argv)
    scores = []
    if argc == 1:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        for arg in sys.argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if len(scores) == 0:
            print("No scores provided."
                  "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        else:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {round(sum(scores) / len(scores), 1)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
