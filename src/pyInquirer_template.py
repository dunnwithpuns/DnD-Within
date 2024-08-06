import typer
import subprocess
from PyInquirer import prompt
from rich import print

app = typer.Typer()


@app.command()
def create_directory():
    module_list_question = [
        {
            'type': 'list',
            'name': 'username',
            'message': 'Select any one username',
            'choices': [
                    {
                        'name': 'Eddie',
                    },
                {
                        'name': 'Hughie',
                    },
                {
                        'name': 'Matthew',
                    },
                {
                        'name': 'Harvey',
                    },
            ],
        }
    ]

    username = prompt(module_list_question)
    print("[yellow]=============================================[yellow]")
    print("[green bold]Enter folder name :[green bold]")
    folder_name = input()

    subprocess.run(
        f"mkdir {folder_name}_created_by_{username['username']}", shell=True
    )


if __name__ == "__main__":
    app()
