from creatures import Monster, Player
from encounter import Encounter


def main():
    monsters = [Monster('bandit'), Monster('harpy')]

    players = [Player('Jack', 2), Player('Kaladin', 2), Player('Bob', 1)]

    encounter = Encounter(monsters, players)


    print(f'Chracater XP Thresholds: \n{encounter.total_xp_threshold}')
    print(f'Adjusted combat XP: {encounter.total_xp}')


if __name__ == "__main__":
    main()
