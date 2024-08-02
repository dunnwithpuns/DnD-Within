import numpy as np
import pandas as pd

# file paths
dnd_monsters_path = "tables/dnd_monsters.csv"
cr_xp_table_path = "tables/cr_xp_table.csv"


all_monsters = pd.read_csv(dnd_monsters_path)
all_monster_challenge_rating = pd.Series(all_monsters['cr'].values, index=all_monsters['name'].values, name='challenge rating')

cr_to_xp_table = pd.read_csv(cr_xp_table_path)
cr_to_xp_series = pd.Series(cr_to_xp_table['xp'].values, index=cr_to_xp_table['cr'].values, name='Challenge Rating x XP')


class Monster:
    def __init__(self, name):
        self.name = name
        self.challenge_rating = self.get_challenge_rating()
        self.xp = self.get_xp()

    def get_challenge_rating(self):
        return all_monster_challenge_rating[self.name]

    def get_xp(self):
        return cr_to_xp_series[self.challenge_rating]


class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_xp_threshold(self):
        pass
