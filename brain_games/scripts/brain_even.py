#!/usr/bin/env python
"""Brain Even game script."""

from brain_games.engine import run_game
from brain_games.games.even import RULES, generate_round


def main():
    """Run the Brain Even game."""
    run_game(RULES, generate_round)


if __name__ == '__main__':
    main()
