from brain_games.engine.cli import game_process
from brain_games.games.gcd import start_game


def main():
    message = 'Find the greatest common divisor of given numbers.'
    game_process(message, start_game)


if __name__ == "__main__":
    main()
