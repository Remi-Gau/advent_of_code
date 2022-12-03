from pathlib import Path
from rich import print

from utils import load_input

"""
A for Rock, B for Paper, and C for Scissors

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

1 for Rock, 2 for Paper, and 3 for Scissors
"""

win_value = 6
draw_value = 3
lose_value = 0

rock_value = 1
paper_value = 2
scissors_value = 3

verbose = False

input_data = load_input()

def return_shape_score(shape):
    shape_score = 0
    if shape == "A":
        shape_score = rock_value
    elif shape == "B":
        shape_score = paper_value
    elif shape == "C":
        shape_score = scissors_value
    return shape_score

def return_outcome_score(row):
    if row[2] == "X":
        outcome_score = 0
    elif row[2] == "Y":
        outcome_score = 3
    elif row[2] == "Z":
        outcome_score = 6
    return outcome_score


score = []
for row in input_data.splitlines():

    outcome_score = return_outcome_score(row)

    if outcome_score == 0:
        if row[0] == "A":
            shape = "C"
        elif row[0] == "B":
            shape = "A"
        elif row[0] == "C":
            shape = "B"

    elif outcome_score == 3:
        shape = row[0]

    elif outcome_score == 6:
        if row[0] == "A":
            shape = "B"
        elif row[0] == "B":
            shape = "C"
        elif row[0] == "C":
            shape = "A"

    shape_score = return_shape_score(shape)

    score_round = shape_score + outcome_score

    score.append(score_round)

    if verbose:
        print(row)
        print(f"shape score is {shape_score}")
        print(f"outcome score is {outcome_score}")
        print(f"round score is {score_round}")

total_score = sum(score)

print(f"total score is {total_score}")
