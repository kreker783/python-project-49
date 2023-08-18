import prompt

name = ''


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")


def game_ending(game_result):
    if game_result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


def game_process(message, game):
    welcome_user()

    print(message)

    if game():
        game_ending()
