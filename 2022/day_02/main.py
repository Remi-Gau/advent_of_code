from pathlib import Path
from rich import print

"""
A for Rock, B for Paper, and C for Scissors
X for Rock, Y for Paper, and Z for Scissors
1 for Rock, 2 for Paper, and 3 for Scissors
"""

win_value = 6
draw_value = 3
lose_value = 0

rock_value = 1
paper_value = 2
scissors_value = 3

draw_conditions = ["C Z", "A X", "B Y"]
win_conditions = ["B Z", "C X", "A Y"]

verbose = False

input_file = Path(__file__).parent.joinpath("input.txt")

with input_file.open() as f:
    input_data = f.read()

score = []
for row in input_data.splitlines():

    print(row)

    shape_score = 0
    outcome_score = 0

    if row[2] == "X":
        shape_score = rock_value
    elif row[2] == "Y":
        shape_score = paper_value
    elif row[2] == "Z":
        shape_score = scissors_value
    print(f"shape score is {shape_score}")

    if row in draw_conditions:
        outcome_score = draw_value
    elif row in win_conditions:
        outcome_score = win_value
    print(f"outcome score is {outcome_score}")

    score_round = shape_score + outcome_score
    print(f"round score is {score_round}")

    score.append(score_round)

total_score = sum(score)

print(f"total score is {total_score}")
