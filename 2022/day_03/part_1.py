import math
import string

from rich import print
from utils import load_input

"""
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
"""

verbose = False

input_data = load_input()


def find_common_item(row):

    compartment_1 = row[: math.floor(len(row) / 2)]
    compartment_2 = row[math.ceil(len(row) / 2)]
    common_item = str(set(compartment_1) & set(compartment_2))
    common_item = common_item.replace("{", "").replace("}", "").replace("'", "")
    if verbose:
        print(f"Compartment 1: {compartment_1}")
        print(f"Compartment 2: {compartment_2}")
        print(f"Common item: {common_item}")
    assert len(compartment_1) == len(compartment_2)
    assert common_item
    return common_item


def find_common_item_priority(common_item):
    lowercase = list(string.ascii_lowercase)
    if common_item in lowercase:
        return lowercase.index(common_item) + 1
    uppercase = list(string.ascii_uppercase)
    return uppercase.index(common_item) + 27


priorities = []
for row in input_data.splitlines():

    if verbose:
        print(f"\n{row}")

    common_item = find_common_item(row)
    priority = find_common_item_priority(common_item)

    priorities.append(priority)

total_score = sum(priorities)

print(f"total score is {total_score}")
