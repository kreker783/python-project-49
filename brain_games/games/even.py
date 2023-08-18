from random import randint
from brain_games.engine.logic import game_loop


def start_game():
    return game_loop(game)


def game():
    number = generate()
    result = is_even(number)

    return result, number


def generate():
    return randint(2, 100)


def is_even(number):
    return "yes" if number % 2 == 0 else "no"
