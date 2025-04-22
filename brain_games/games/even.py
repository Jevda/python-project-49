"""Brain Even game logic."""

import random

# Правила игры выносим в константу
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1  # Минимальное число для вопроса
MAX_NUMBER = 100  # Максимальное число для вопроса


def is_even(number):
    """Checks if a number is even."""
    return number % 2 == 0


def generate_round():
    """Generates a question (number) and the correct answer ('yes' or 'no')."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
