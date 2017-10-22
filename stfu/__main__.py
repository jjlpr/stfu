import click

from .wavalysis import wav_to_json


@click.command()
@click.argument('input_filename')
def do(input_filename):
    print(wav_to_json(input_filename))


if __name__ == '__main__':
    do()
