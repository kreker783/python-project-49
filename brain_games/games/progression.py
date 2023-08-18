from random import randint, choice
from brain_games.engine.logic import game_loop


def start_game():
    return game_loop(game)


def game():
    result, progression = pick_element(get_progression(generate()))

    return result, progretion


def generate():
    start_number = randint(1, 100)
    difference = randint(1, 10)
    return start_number, difference


def get_progression(a, d, n=9):
    result = [a]
    for i in range(1, n+1):
        a = a + d
        result.append(a)
    return result


def pick_element(progression):
    element = choice(progression)
    index = progression.index(element)
    progression[index] = '..'
    return element, " ".join(str(i) for i in progression)
