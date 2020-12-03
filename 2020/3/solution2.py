from operator import mul
from functools import reduce

START = (0, 0)
SLOPES = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

with open("input.txt") as input_file:
    map = [line.strip() for line in input_file]

rows, cols = len(map), len(map[0])

trees_in_slopes = []

for slope in SLOPES:
    step_col, step_row = slope

    trees = 0
    x, y = START

    while True:
        x += step_col
        y += step_row

        if y >= rows:
            trees_in_slopes.append(trees)
            break

        if map[y][x % cols] == "#":
            trees += 1

print(f"Result: {trees_in_slopes}, multiplied: {reduce(mul, trees_in_slopes)}")
