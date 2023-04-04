from rich import print
from utils import load_input

verbose = False

input_data = load_input()

full_overlap_count = 0
partial_overlap_count = 0

for line in input_data:
    if line == "":
        continue

    elves = line.split(",")

    if verbose:
        print()
        print(line)
        print(elves)

    id_ranges = []

    for elf in elves:
        this_range = set(range(int(elf.split("-")[0]), int(elf.split("-")[1]) + 1))
        id_ranges.append(this_range)

        if verbose:
            print(elf.split("-"))
            print(id_ranges)

    if id_ranges[0].issubset(id_ranges[1]) or id_ranges[1].issubset(id_ranges[0]):
        full_overlap_count += 1

    if len(id_ranges[0] & id_ranges[1]) > 0:
        partial_overlap_count += 1


print(f"Full overlap count:{full_overlap_count}")
print(f"Partial overlap count:{partial_overlap_count}")
