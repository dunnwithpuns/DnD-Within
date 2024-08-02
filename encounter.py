import numpy as np
import pandas as pd
from creatures import Monster, Player


class Encounter:
    def __init__(self, monsters, players=None):
        self.monsters = monsters
        self.players = players
#        self.total_challenge_rating = self.get_total_challenge_rating()
        self.total_xp = int(self.get_total_xp())

#        self.xp_threshold = self.get_xp_threshold()
#        self.difficulty = self.get_difficulty()

#    def get_total_challenge_rating(self):
#        challenge_rating_strings = [monster.challenge_rating for monster in self.monsters]
#        monster_challenge_rating_floats = [self.fraction_to_float(challenge_rating_string) if '/' in challenge_rating_string else float(challenge_rating_string) for challenge_rating_string in challenge_rating_strings]
#        return np.sum(monster_challenge_rating_floats)
        
           
    def get_total_xp(self):
        monster_xp = [int(monster.xp) for monster in self.monsters]
        raw_xp_total = np.sum(monster_xp)

        if len(monsters) == 1:
            return raw_xp_total
        if len(monsters) == 2:
            return raw_xp_total * 1.5
        if 3 <= len(monsters) <= 6:
            return raw_xp_total * 2
        if 7 <= len(monsters) <= 10:
            return raw_xp_total * 2.5
        if 11 <= len(monsters) <= 14:
            return raw_xp_total * 3
        if len(monsters) >= 15:
            return raw_xp_total * 4




    def get_difficulty(self):
        pass


monsters = [Monster('bandit'), Monster('bandit-captain')]

encounter = Encounter(monsters)

print(encounter.total_xp)

