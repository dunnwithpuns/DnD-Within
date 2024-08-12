import typer
# import subprocess
from PyInquirer import prompt
from rich import print

app = typer.Typer()


@app.command()
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


if __name__ == "__main__":
    app()
