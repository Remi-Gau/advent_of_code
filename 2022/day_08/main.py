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
    return grid


def check_visible_in_row(grid, visibility_grid, this_max, i_row, cols: list):

    current_min = 0

    for i_col in cols:

        # once we reach the max, we stop: the rest of the row won't be visible
        if grid.loc[i_row, i_col] == this_max:
            visibility_grid.loc[i_row, i_col] = True
            return visibility_grid

        # trees on the edge are always visible
        if i_col in [cols[0]]:
            current_min = grid.loc[i_row, i_col]
            visibility_grid.loc[i_row, i_col] = True

        elif grid.loc[i_row, i_col] > current_min:
            current_min = grid.loc[i_row, i_col]
            visibility_grid.loc[i_row, i_col] = True

        elif visibility_grid.loc[i_row, i_col] is True:
            continue

        else:
            visibility_grid.loc[i_row, i_col] = False

    return visibility_grid


def check_visible_in_col(grid, visibility_grid, this_max, i_col, rows: list):

    current_min = 0

    for i_row in rows:

        # once we reach the max, we stop: the rest of the row won't be visible
        if grid.loc[i_row, i_col] == this_max:
            visibility_grid.loc[i_row, i_col] = True
            return visibility_grid

        # trees on the edge are always visible
        if i_col in [rows[0]]:
            current_min = grid.loc[i_row, i_col]
            visibility_grid.loc[i_row, i_col] = True

        elif int(grid.loc[i_row, i_col]) > int(current_min):
            current_min = grid.loc[i_row, i_col]
            visibility_grid.loc[i_row, i_col] = True

        elif visibility_grid.loc[i_row, i_col] is True:
            continue

        else:
            visibility_grid.loc[i_row, i_col] = False

    return visibility_grid


def main():

    input_data = load_input(test=False)

    grid = turn_into_df(input_data)
    visibility_grid = grid.copy()

    row_max = grid.max(axis=1)
    col_max = grid.max(axis=0)

    cols = list(grid.columns)
    rows = grid.index

    for i_row in rows:

        if i_row in [rows[0], rows[-1]]:
            visibility_grid = set_all_cols_to_true(visibility_grid, i_row, cols)
            continue

        visibility_grid = check_visible_in_row(
            grid, visibility_grid, row_max[i_row], i_row, cols
        )
        visibility_grid = check_visible_in_row(
            grid, visibility_grid, row_max[i_row], i_row, list(reversed(cols))
        )

    for i_col in cols:

        visibility_grid = check_visible_in_col(
            grid, visibility_grid, col_max[i_col], i_col, rows
        )

        visibility_grid = check_visible_in_col(
            grid, visibility_grid, col_max[i_col], i_col, list(reversed(rows))
        )

    # visibility_grid.replace(list(range(10)), value=False, inplace=True)

    print("\ngrid")
    print(grid)

    print("\nvisibility grid")
    print(visibility_grid)

    print("\nnumber of visible trees")
    print(visibility_grid.sum().sum())


if __name__ == "__main__":
    main()
