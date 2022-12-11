import pandas as pd
from rich import print
from utils import load_input


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


def check_visible_in_row(grid, visibility_grid, i_row_max, i_row, cols: list):

    current_min = 0

    for i_col in cols:

        # once we reach the max, we stop: the rest of the row won't be visible
        if int(grid.loc[i_row, i_col]) == int(i_row_max):
            visibility_grid.loc[i_row, i_col] = True
            return visibility_grid

        # trees on the edge are always visible
        if i_col in [cols[0]]:
            current_min = int(grid.loc[i_row, i_col])
            visibility_grid.loc[i_row, i_col] = True

        elif int(grid.loc[i_row, i_col]) > current_min:
            current_min = int(grid.loc[i_row, i_col])
            visibility_grid.loc[i_row, i_col] = True

    return visibility_grid


def main():

    input_data = load_input(True)

    grid = turn_into_df(input_data)
    visibility_grid = grid.copy()

    row_max = grid.max(axis=1)

    cols = list(grid.columns)
    rows = grid.index

    for i_row in rows:

        if i_row in [rows[0], rows[-1]]:
            set_all_cols_to_true(visibility_grid, i_row, cols)
            continue

        visibility_grid = check_visible_in_row(
            grid, visibility_grid, row_max[i_row], i_row, cols
        )
        visibility_grid = check_visible_in_row(
            grid, visibility_grid, row_max[i_row], i_row, list(reversed(cols))
        )

    print("\ngrid")
    print(grid)

    print("\nvisibility grid")
    print(visibility_grid)


if __name__ == "__main__":
    main()
