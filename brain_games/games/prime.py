"""Brain Prime game logic."""

import random

# Правила игры
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1    # Минимальное число для вопроса
MAX_NUMBER = 100  # Максимальное число для вопроса


def is_prime(number):
    """Checks if a number is prime."""
    if number < 2:  # Числа меньше 2 не являются простыми
        return False
    # Проверяем делители от 2 до квадратного корня из числа
    # Если находится делитель, число не простое
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    # Если делителей не найдено, число простое
    return True


def generate_round():
    """Generates a number and the correct answer ('yes' or 'no')."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer
