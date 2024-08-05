from creatures import Monster, Player
from encounter import Encounter


def main():

    num_players_input = int(input("How many players are in the party? "))
    num_mosnter_input = int(input("How many monsters are in this encounter? "))
    players = []
    monsters = []

    for player in range(num_players_input):
        name = input(f"Please enter player {player + 1}'s character name: ")
        level = int(
            input(f"Please enter player {player + 1}'s character level: "))
        players.append(Player(name, level))

    for monster in range(num_mosnter_input):
        name = input("Which monster would you like to add to the encounter? ")
        num = int(input(f"How many {name}'s would you like to add? "))
        for i in range(num):
            monsters.append(Monster(name))

    encounter = Encounter(monsters, players)

    print(f'Chracater XP Thresholds: \n{encounter.total_xp_threshold}')
    print(f'Encounter difficulty: {encounter.difficulty}')
    print(f'Adjusted combat XP: {encounter.total_monster_xp}')


if __name__ == "__main__":
    main()
