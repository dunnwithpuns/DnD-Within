from creatures import Monster, Player
from encounter import Encounter


def main():
    monsters = [Monster('bandit'), Monster('harpy')]

    players = [Player('Jack', 2), Player('Bob', 1)]

    encounter = Encounter(monsters, players)

    kaladin = Player('Kaladin', 1)

    print(encounter.total_xp_threshold)


if __name__ == "__main__":
    main()
