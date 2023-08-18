from random import sample
from math import gcd
from brain_games.engine.logic import game_loop


def start_game():
    return game_loop(game)


def game():
    first_number, second_number = generate()
    result = get_result(first_number, second_number)

    expression = str(f"{first_number} {second_number}")

    return result, expression


def generate():
    return sample(range(1, 100), 2)


def get_result(x, y):
    return gcd(x, y)
