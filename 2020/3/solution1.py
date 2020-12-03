START = (0, 0)
STEP_ROW = 1
STEP_COL = 3

with open("input.txt") as input_file:
    map = [line.strip() for line in input_file]

rows, cols = len(map), len(map[0])
trees = 0
x, y = START

while True:
    x += STEP_COL
    y += STEP_ROW

    if y >= rows:
        break

    if map[y][x % cols] == "#":
        trees += 1

print(f"Total trees: {trees}")
