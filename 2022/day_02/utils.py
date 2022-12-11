from pathlib import Path


def load_input():

    input_file = Path(__file__).parent.joinpath("input.txt")

    with input_file.open() as f:
        return f.read()
