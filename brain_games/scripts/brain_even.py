from brain_games.engine.cli import game_process
from brain_games.games.even import start_game


def main():
    message = 'Answer "yes" if the number is even, otherwise answer "no".',
    game_process(message, start_game)


if __name__ == "__main__":
    main()
