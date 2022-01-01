from copy import deepcopy 

def print_map(map):
    for row in map:
        for c in row:
            print(c, end="")
        print()

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

map = []

for line in lines:
    map.append(list(line))

rounds = 0

print_map(map)

while True:
    rounds += 1
    changed = False

    new_map = deepcopy(map)

    # Move east
    for row in range(len(map)):
        for col in range(len(map[row])):
            next_col = col + 1 if col + 1 < len(map[row]) else 0
            if map[row][col] == '>' and map[row][next_col] == ".":
                new_map[row][next_col] = '>'
                new_map[row][col] = "."
                changed = True

    map = new_map
    new_map = deepcopy(map)

    # Move south
    for row in range(len(map)):
        next_row = row + 1 if row + 1 < len(map) else 0
        for col in range(len(map[row])):
            if map[row][col] == 'v' and map[next_row][col] == ".":
                new_map[row][col] = "."
                new_map[next_row][col] = 'v'
                changed = True

    map = new_map

    print(rounds)

    if not changed:
        break
