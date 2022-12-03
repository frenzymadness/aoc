from pathlib import Path

here = Path(__file__).parent

xyz_to_score = {"X": 1, "Y": 2, "Z": 3}
draw_combs = ("AX", "BY", "CZ")
win_comb = ("AY", "BZ", "CX")

def calculate_score(line):
    comp, me = line.split()
    score = xyz_to_score[me]

    if (comp + me) in win_comb:
        score += 6
    elif (comp + me) in draw_combs:
        score += 3
    
    return score


total_score = 0

with open(here / "input") as input:
    for line in input:
        total_score += calculate_score(line)

print(total_score)
