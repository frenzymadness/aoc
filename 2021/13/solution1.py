from collections import defaultdict
import re

def print_paper(paper):
    rows = max([x[1] for x in paper])
    cols = max([x[0] for x in paper])
    for row in range(rows+1):
        for col in range(cols+1):
            if (col, row) in paper:
                print("#", end="")
            else:
                print(".", end="")
        print()

def fold_paper(paper, axis, index):
    new_paper = set()
    for col, row in paper:
        if row > index and axis == "y":
            row = index - (row - index)
        elif col > index and axis == "x":
            col = index - (col - index)
        new_paper.add((col, row))

    return new_paper

paper = set()
instructions = []

with open("input.txt") as input_file:
    for line in input_file:
        line = line.strip()
        if not line:
            break
        col, row = [int(n) for n in line.split(",")]
        paper.add((col, row))

    for line in input_file:
        if match := re.match(r"fold along (x|y)=(\d+)", line):
            axis, n = match.groups()
            instructions.append((axis, int(n)))

for axis, index in instructions:
    paper = fold_paper(paper, axis, index)
    print(len(paper))
    break
