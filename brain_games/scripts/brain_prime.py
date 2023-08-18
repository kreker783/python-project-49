from brain_games.engine.cli import game_process
from brain_games.games.prime import start_game


def main():
    start_mess = 'Answer "yes" if given number is prime'
    game_process(f'{start_mess}. Otherwise answer "no".', start_game())


if __name__ == "__main__":
    main()
