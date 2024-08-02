import numpy as np
import pandas as pd

user_input = ["dretch", "bandit"]

all_monsters = pd.read_csv('dnd_monsters.csv')

all_monster_challenge_rating = pd.Series(all_monsters['cr'].values, index=all_monsters['name'].values, name='challenge rating')

def convert_fraction_string_to_float(string):
    divisors = string.split('/')
    return float(divisors[0]) / float(divisors[1])


input_monster_cr = all_monster_challenge_rating[user_input].values

user_monster_challenge_rating = [convert_fraction_string_to_float(n) for n in input_monster_cr]

print(user_monster_challenge_rating)
