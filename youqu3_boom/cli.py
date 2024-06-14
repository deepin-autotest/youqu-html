import os


def cli():
    os.system("pipenv --python 3")
    os.system("pipenv run pip install -r requirements.txt")


if __name__ == '__main__':
    cli()
