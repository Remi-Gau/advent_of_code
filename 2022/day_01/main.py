from pathlib import Path

from rich import print

verbose = False

input_file = Path(__file__).parent.joinpath("input.txt")

with input_file.open() as f:
    input_data = f.read()

elves = []
this_elf = []
for row in input_data.splitlines():

    if row == "":
        elves.append(sum(this_elf))
        if verbose:
            print(this_elf)
            print(sum(this_elf))
        this_elf = []

    else:
        this_elf.append(int(row))

if verbose:
    print(elves)

print(f"max value is {max(elves)}")
