from parse import search
from rich import print
from utils import load_input


input_data = load_input()


def stack_count(stacks):
    return sum(len(stacks[key]) for key in stacks)


def get_initial_stacks():

    stacks = {str(x): [] for x in range(1, 10)}

    for line in input_data:

        if line == "":
            continue

        if line.startswith("["):
            start_index = 1
            for x in range(9):
                index = start_index + 4 * x
                if line[index] != " ":
                    stacks[str(x + 1)].insert(0, line[index])

    return stacks


def main():

    stacks = get_initial_stacks()

    initial_nb_crates = stack_count(stacks)

    print(initial_nb_crates)

    for line in input_data:

        if line.startswith("move"):
            instructions = search("move {move} from {from} to {to}", line).named

            for _ in range(int(instructions["move"])):
                stacks[instructions["to"]].append(stacks[instructions["from"]].pop(-1))

            assert stack_count(stacks) == initial_nb_crates

    print(stacks)

    results = [stacks[str(x)][-1] for x in range(1, 10)]

    print("".join(results))


if __name__ == "__main__":
    main()
