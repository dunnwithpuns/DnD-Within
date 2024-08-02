import numpy as np
import pandas as pd

user_input = ["dretch", "bandit"]

all_monsters = pd.read_csv('dnd_monsters.csv')

all_monster_challenge_rating = pd.Series(all_monsters['cr'].values, index=all_monsters['name'].values, name='challenge rating')

xp_table = pd.read_csv('cr_xp_table.csv') 

def fraction_string_to_float(string):
    divisors = string.split('/')
    return float(divisors[0]) / float(divisors[1])

def fraction_float_to_string(float_value):
    pass

converted_input_monster_challenge_rating = [fraction_string_to_float(cr) for cr in all_monster_challenge_rating[user_input].values] 

