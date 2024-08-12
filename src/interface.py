# import typer
# import subprocess
from rich.prompt import Prompt
from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.effects.effect_wipe import Wipe
from terminaltexteffects.utils.graphics import Color
import pyfiglet
from PyInquirer import prompt
from creatures import Monster, Player
from encounter import Encounter


def welcome():

    print_big("DnD Within", burn_animation)
    wipe_animation('====================================================')
    green_print_animation('''Let's create your encounter!''')
    wipe_animation('====================================================')
    encounter = create_encounter()
    get_difficulty(encounter)


def creature_question():
    module_list_question = [
        {
            'type': 'list',
            'name': 'creature',
            'message': 'Players or Monsters?',
            'choices': [{'name': 'Players', }, {'name': 'Monsters', }, ],
        }
    ]

    creature_choice = prompt(module_list_question)
    print("[yellow]=============================================[yellow]")
    if creature_choice == 'Players':
        pass
    #     player_question()
    if creature_choice == 'Monsters':
        pass
    #     # monster_question()


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

    wipe_animation('====================================================')

    red_print_animation("How many monsters are in this encounter?")
    monsters = int(Prompt.ask("[red bold]>[red bold]"))
    monster_list = []
    for monster in range(monsters):
        name = red_print_animation(
            "What monster would you like to add to the encounter?")
        name = Prompt.ask("[red bold]>[red bold]")
        monster_list.append(Monster(name))

    wipe_animation('====================================================')

    return Encounter(monster_list, player_list)


def get_difficulty(encounter):
    green_print_animation("The encounter difficulty is . . .")
    print_big(encounter.difficulty, burn_animation)


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
    effect.effect_config.final_gradient_stops = (Color("ff0000"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


def green_print_animation(text):
    effect = Print(text)
    effect.effect_config.final_gradient_stops = (Color("00ff00"))
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)


def wipe_animation(text):
    effect = Wipe(text)
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
