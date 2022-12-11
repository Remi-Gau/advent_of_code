import pandas as pd
from rich import print
from utils import load_input

input_data = load_input()


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


def set_all_cols_to_true(grid, i_row, cols):
    for i_col in cols:
        grid.loc[i_row, i_col] = True


def check_visible_in_row(grid, i_row_max, i_row, cols: list):

    current_min = 0

    for i_col in cols:

        if grid.loc[i_row, i_col] is True:
            continue

        # trees on the edge are always visible
        if i_col in [cols[0], cols[-1]]:
            grid.loc[i_row, i_col] = True

        # once we reach the max, we stop: the rest of the row won't be visible
        elif int(grid.loc[i_row, i_col]) == int(i_row_max):
            grid.loc[i_row, i_col] = True
            return grid

        elif int(grid.loc[i_row, i_col]) > current_min:
            grid.loc[i_row, i_col] = True
            current_min = grid.loc[i_row, i_col]

    return grid


def main():

    grid = turn_into_df(input_data)

    row_max = grid.max(axis=0)

    cols = list(grid.columns)
    rows = grid.index

    for i_row in rows:

        if i_row in [rows[0], rows[-1]]:
            set_all_cols_to_true(grid, i_row, cols)
            continue

        grid = check_visible_in_row(grid, row_max[i_row], i_row, cols)
        grid = check_visible_in_row(grid, row_max[i_row], i_row, list(reversed(cols)))

    print(grid)


if __name__ == "__main__":
    main()
