from random import sample, choice
from operator import add, mul, sub
from brain_games.engine.logic import game_loop


def start_game():
    return game_loop(game)


def game():
    first_number, second_number, operation = generate()
    result = operation(first_number, second_number)

    expression = get_expression(first_number, second_number, operation)

    if result < 0:
        result = str(result)

    return result, expression


def generate():
    first_number, second_number = sample(range(1, 100), 2)
    operation = choice([add, sub, mul])
    return first_number, second_number, operation


def get_expression(first_number, second_number, op):
    if op == add:
        expr = f"{first_number} + {second_number}"
    elif op == sub:
        expr = f"{first_number} - {second_number}"
    else:
        expr = f"{first_number} * {second_number}"

    return expr
