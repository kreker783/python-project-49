def validate(result, answer):
    if str(result) == str(answer):
        print("Correct!")
        return True

    print(f'{answer} is wrong answer ;(. Correct answer was {result}.')
    return False


def get_answer(question):
    print(f"Question: {question}")
    answer = input("Your answer: ")

    if answer.isdigit():
        answer = int(answer)

    return answer


def game_loop(game):
    count = 0
    while count < 3:
        result, expression = game()

        validation = validate(result, get_answer(expression))

        if validation:
            count += 1
        else:
            return False
    return True
