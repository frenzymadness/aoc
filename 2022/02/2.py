from pathlib import Path

here = Path(__file__).parent

xyz_to_score = {"X": 1, "Y": 2, "Z": 3}
to_draw = {"A": "X", "B": "Y", "C": "Z"}
to_loose = {"A": "Z", "B": "X", "C": "Y"}
to_win = {"A": "Y", "B": "Z", "C": "X"}
for_result = {"X": to_loose, "Y": to_draw, "Z": to_win}
result_score = {"X": 0, "Y": 3, "Z": 6}

total_score = 0

with open(here / "input") as input:
    for line in input:
        comp, result = line.split()
        me = for_result[result][comp]
        score = result_score[result]
        score += xyz_to_score[me]
        total_score += score

print(total_score)
