#!/usr/bin/env python
"""Main script for brain-games."""

from brain_games.cli import welcome_user  # Импортируем функцию


def main():
    """Run user greeting."""
    welcome_user()  # Вызываем импортированную функцию


if __name__ == '__main__':
    main()
