import string

from rich import print
from utils import load_input

"""
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
"""

verbose = True

input_data = load_input()


def find_common_item(group):
    elf_1 = group[0]
    elf_2 = group[1]
    elf_3 = group[2]

    common_item = str(set(elf_1) & set(elf_2) & set(elf_3))
    common_item = common_item.replace("{", "").replace("}", "").replace("'", "")

    if verbose:
        print(f"group: {group}")
        print(f"Common item: {common_item}\n")

    assert common_item
    return common_item


def find_common_item_priority(common_item):
    lowercase = list(string.ascii_lowercase)
    if common_item in lowercase:
        return lowercase.index(common_item) + 1
    uppercase = list(string.ascii_uppercase)
    return uppercase.index(common_item) + 27


priorities = []
group = []
elf_counter = 0
for row in input_data.splitlines():
    if verbose:
        print(f"row: {row}")

    group.append(row)

    if len(group) == 3:
        common_item = find_common_item(group)
        priority = find_common_item_priority(common_item)
        priorities.append(priority)
        group = []

total_score = sum(priorities)

print(f"total score is {total_score}")
