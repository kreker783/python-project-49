from random import randint
from brain_games.engine.logic import game_loop


def start_game():
    return game_loop(game)


def game():
    number = generate()
    result = is_prime(number)

    return result, number


def generate():
    return randint(1, 100)


def is_prime(x):
    for i in range(2, int(x/2)):
        if (x % i) == 0:
            return "no"
    return "yes"
