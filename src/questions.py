# import typer
# import subprocess
from rich import print
from rich.prompt import Prompt
# from PyInquirer import prompt
from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.utils.graphics import Color
import pyfiglet
from creatures import Monster, Player
from encounter import Encounter


def welcome():

    print_big("DnD Within", burn_animation)
    print('''[green bold]Let's create an encounter!''')
    print('[yellow]=================================================[yellow]')
    encounter = create_encounter()
    print(encounter.difficulty)


def create_encounter():

    print_animation("How many players are in the party?")
    players = int(Prompt.ask("[blue bold]>[blue bold]"))
    player_list = []
    for player in range(players):
        print_animation(f"What is player {player + 1}'s name?")
        name = Prompt.ask("[blue bold]>[blue bold]")
        print_animation(f"What is {name}'s level?")
        level = int(Prompt.ask("[blue bold]>[blue bold]"))
        player_list.append(Player(name, level))

    red_print_animation("How many monsters are in this encounter?")
    monsters = int(Prompt.ask("[red bold]>[red bold]"))
    monster_list = []
    for monster in range(monsters):
        name = red_print_animation(
            "What monster would you like to add to the encounter?")
        name = Prompt.ask("[red bold]>[red bold]")
        monster_list.append(Monster(name))

    return Encounter(monster_list, player_list)


def party_info():
    pass


def print_big(text, animation):
    text = pyfiglet.figlet_format(text)
    animation(text)


def input_print_animation(text):
    effect = Print(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.input(frame)


def burn_animation(text):
    effect = Burn(text)
    effect.terminal_config.canvas_width = 200
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


def print_animation(text):
    effect = Print(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


def red_print_animation(text):
    effect = Print(text)
    effect.effect_config.final_gradient_stops = (
        Color("ff0000"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
