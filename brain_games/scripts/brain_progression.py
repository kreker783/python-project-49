from brain_games.engine.cli import game_process
from brain_games.games.progression import start_game


def main():
    game_process('What number is missing in the progression?', start_game)


if __name__ == "__main__":
    main()
