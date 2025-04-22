"""Brain GCD game logic."""

import math  # Импортируем модуль math для функции gcd
import random

# Правила игры
RULES = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1    # Минимальное число
MAX_NUMBER = 100  # Максимальное число


def generate_round():
    """Generates two numbers and the correct GCD."""
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{num1} {num2}"
    # Используем math.gcd для нахождения НОД
    correct_answer = str(math.gcd(num1, num2))

    return question, correct_answer
