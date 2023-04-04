from rich import print
from utils import load_input

"""
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
1 for Rock, 2 for Paper, and 3 for Scissors
"""

draw_conditions = ["C Z", "A X", "B Y"]
win_conditions = ["B Z", "C X", "A Y"]

win_value = 6
draw_value = 3
lose_value = 0

rock_value = 1
paper_value = 2
scissors_value = 3

verbose = False

input_data = load_input()


def return_shape_score(row):
    shape_score = 0
    if row[2] == "X":
        shape_score = rock_value
    elif row[2] == "Y":
        shape_score = paper_value
    elif row[2] == "Z":
        shape_score = scissors_value
    return shape_score


def return_outcome_score(row):
    outcome_score = 0
    if row in draw_conditions:
        outcome_score = draw_value
    elif row in win_conditions:
        outcome_score = win_value
    return outcome_score


score = []
for row in input_data.splitlines():
    shape_score = return_shape_score(row)

    outcome_score = return_outcome_score(row)

    score_round = shape_score + outcome_score

    score.append(score_round)

    if verbose:
        print(row)
        print(f"shape score is {shape_score}")
        print(f"outcome score is {outcome_score}")
        print(f"round score is {score_round}")

total_score = sum(score)

print(f"total score is {total_score}")
