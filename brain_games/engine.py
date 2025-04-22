"""General game engine."""

import prompt

ROUNDS_COUNT = 3  # Используем константу вместо "магического числа" 3


def run_game(rules, generate_round_data):
    """
    Runs a generic game loop.

    Args:
        rules: The rules of the game to be displayed.
        generate_round_data: A function that generates question and correct answer
                             for a single round. It should return a tuple:
                             (question_string, correct_answer_string).
    """
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(rules)

    for _ in range(ROUNDS_COUNT):  # Цикл на количество раундов
        question, correct_answer = generate_round_data()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при первой ошибке

    # Если цикл завершился без ошибок
    print(f"Congratulations, {name}!")
