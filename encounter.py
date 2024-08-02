import numpy as np
import pandas as pd
from creatures import Monster


class Encounter:
    def __init__(self, monsters, players=None):
        self.monsters = monsters
        self.players = players
        self.difficulty = self.check_difficulty()

    def check_difficulty(self):
        challenge_rating_strings = [individual_monster.challenge_rating for individual_monster in self.monsters]
        monster_challenge_rating_floats = [self.fraction_to_float(challenge_rating_string) if '/' in challenge_rating_string else float(challenge_rating_string) for challenge_rating_string in challenge_rating_strings]
        return np.sum(monster_challenge_rating_floats)

    
    def get_xp_total(self):
        pass


    def fraction_to_float(self, string):
        divisors = string.split('/')
        return float(divisors[0]) / float(divisors[1])

monsters = [Monster('bandit'), Monster('bandit-captain')]

encounter = Encounter(monsters)

for monster in encounter.monsters:
    print(monster.name)
