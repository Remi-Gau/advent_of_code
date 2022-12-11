from pathlib import Path

import numpy as np
import pandas as pd


def load_input(test: bool = False):

    input_file = Path(__file__).parent.joinpath("input.txt")
    if test:
        input_file = Path(__file__).parent.joinpath("input_test.txt")

    with input_file.open() as f:
        return f.read().split("\n")


def turn_into_df(input_data):

    data = {}

    for row in input_data:

        if row == "":
            continue

        for i, col in enumerate(row):
            if i not in data:
                data[i] = []
            data[i].append(col)

    grid = pd.DataFrame(data)

    return grid


def turn_into_npa(input_data):

    data = [[int(x) for x in row] for row in input_data if row != ""]

    return np.array(data)
