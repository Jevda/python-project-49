"""Brain Progression game logic."""

import random

# Правила игры
RULES = 'What number is missing in the progression?'

# Параметры прогрессии
MIN_START = 1       # Минимальное стартовое число
MAX_START = 50      # Максимальное стартовое число
MIN_DIFF = 1        # Минимальный шаг прогрессии
MAX_DIFF = 10       # Максимальный шаг прогрессии
MIN_LEN = 5         # Минимальная длина прогрессии
MAX_LEN = 10        # Максимальная длина прогрессии


def generate_round():
    """Generates a progression string with one hidden number
    and the correct answer."""
    start = random.randint(MIN_START, MAX_START)
    diff = random.randint(MIN_DIFF, MAX_DIFF)
    length = random.randint(MIN_LEN, MAX_LEN)

    # Генерируем полную прогрессию
    progression = []
    for i in range(length):
        progression.append(start + i * diff)

    # Выбираем случайный индекс для скрытия
    hidden_index = random.randint(0, length - 1)

    # Запоминаем правильный ответ (скрытое число)
    correct_answer = str(progression[hidden_index])

    # Заменяем скрытое число на ".." для вопроса
    # Преобразуем числа в строки   # <--- Перенеси комментарий сюда
    progression_question = [str(num) for num in progression]
    progression_question[hidden_index] = ".."
    question = " ".join(progression_question)

    return question, correct_answer
