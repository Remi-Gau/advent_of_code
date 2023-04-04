import itertools

import numpy as np
from rich import print
from utils import load_input
from utils import turn_into_npa


def get_viewing_distance(is_smaller_tree):
    viewing_distance = 1

    if is_smaller_tree.size == 0:
        viewing_distance = 0
        return viewing_distance

    if np.all(is_smaller_tree):
        viewing_distance = sum(is_smaller_tree)
        return int(viewing_distance)

    if np.any(is_smaller_tree):
        idx_taller_trees = np.where(~is_smaller_tree)
        viewing_distance = idx_taller_trees[0][0]
        return int(viewing_distance) + 1

    return viewing_distance


def main():
    input_data = load_input(test=False)

    grid = turn_into_npa(input_data)

    (nb_rows, nb_cols) = grid.shape

    scenic_score = np.zeros((nb_rows, nb_cols))

    for i, j in itertools.product(range(nb_rows), range(nb_cols)):
        visible = grid < grid[i, j]

        # up
        viewing_distance = [get_viewing_distance(np.flip(visible[: -nb_rows + i, j]))]

        # left
        viewing_distance.append(get_viewing_distance(np.flip(visible[i, : -nb_cols + j])))

        # right
        viewing_distance.append(get_viewing_distance(visible[i, j + 1 :]))

        # down
        viewing_distance.append(get_viewing_distance(visible[i + 1 :, j]))

        scenic_score[i, j] = np.array(viewing_distance).prod()

    print(grid)
    print(scenic_score)

    print(np.max(scenic_score))


if __name__ == "__main__":
    main()
