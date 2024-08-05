import typer
# import subprocess
from rich import print, input
# from creatures import Monster, Player
# from encounter import Encounter

app = typer.Typer()


@app.command()
def initial_main_menu():
    print('[red bold]WELCOME TO DnD-Within![red bold]')
    print('''Seeing as this is your first time, let's create an encounter!''')
    print('[yellow]=================================================[yellow]')
    create_encounter()


def create_encounter():
    pass


def party_info():
    pass
