#!/usr/bin/env python
"""Brain GCD game script."""

from brain_games.engine import run_game
from brain_games.games.gcd import RULES, generate_round


def main():
    """Run the Brain GCD game."""
    run_game(RULES, generate_round)


if __name__ == '__main__':
    main()
