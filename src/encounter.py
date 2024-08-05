import numpy as np
import pandas as pd


class Encounter:
    def __init__(self, monsters, players=None):
        self.monsters = monsters
        self.players = players
        self.total_monster_xp = int(self.get_total_xp())

        self.total_xp_threshold = self.get_total_xp_threshold()
        self.easy_xp = self.total_xp_threshold['Easy']
        self.medium_xp = self.total_xp_threshold['Medium']
        self.hard_xp = self.total_xp_threshold['Hard']
        self.deadly_xp = self.total_xp_threshold['Deadly']

        self.difficulty = self.get_difficulty()

    def get_total_xp(self):
        monster_xp = [int(monster.xp) for monster in self.monsters]
        raw_xp_total = np.sum(monster_xp)

        if len(self.monsters) == 1:
            return raw_xp_total
        if len(self.monsters) == 2:
            return raw_xp_total * 1.5
        if 3 <= len(self.monsters) <= 6:
            return raw_xp_total * 2
        if 7 <= len(self.monsters) <= 10:
            return raw_xp_total * 2.5
        if 11 <= len(self.monsters) <= 14:
            return raw_xp_total * 3
        if len(self.monsters) >= 15:
            return raw_xp_total * 4

    def get_total_xp_threshold(self):
        player_thresholds = [player.xp_threshold for player in self.players]
        total_thresholds = pd.Series()
        for threshold in player_thresholds:
            if total_thresholds.empty:
                total_thresholds = threshold
            else:
                total_thresholds += threshold

        return total_thresholds

    def get_difficulty(self):
        if self.total_monster_xp <= self.easy_xp:
            return "Easy"
        if self.total_monster_xp <= self.medium_xp:
            return "Medium"
        if self.total_monster_xp <= self.hard_xp:
            return "Hard"
        else:
            return "Deadly"
