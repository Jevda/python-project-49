"""Command Line Interface functions."""

import prompt


def welcome_user():
    """Ask user's name and greet them."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
