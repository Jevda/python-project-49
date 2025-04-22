"""Brain Calculator game logic."""

import operator
import random

# Правила игры
RULES = 'What is the result of the expression?'

# Допустимые операторы и соответствующие им функции
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

MIN_NUMBER = 1    # Минимальное число
MAX_NUMBER = 25   # Максимальное число (можно выбрать другое)


def generate_round():
    """Generates expression string and the correct answer."""
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    op_symbol, op_function = random.choice(list(OPERATORS.items()))

    question = f"{num1} {op_symbol} {num2}"
    correct_answer = str(op_function(num1, num2))

    return question, correct_answer
