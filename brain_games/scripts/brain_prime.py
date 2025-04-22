#!/usr/bin/env python
"""Brain Prime game script."""

from brain_games.engine import run_game
from brain_games.games.prime import RULES, generate_round


def main():
    """Run the Brain Prime game."""
    run_game(RULES, generate_round)


if __name__ == '__main__':
    main()
