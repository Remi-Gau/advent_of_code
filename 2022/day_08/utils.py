from pathlib import Path


def load_input(test: bool = False):

    input_file = Path(__file__).parent.joinpath("input.txt")
    if test:
        input_file = Path(__file__).parent.joinpath("input_test.txt")

    with input_file.open() as f:
        return f.read().split("\n")
