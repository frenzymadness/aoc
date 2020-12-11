from copy import deepcopy

with open("input.txt") as input_file:
    map = [list(l.strip()) for l in input_file.readlines()]


def occupied_around(map, seat):
    r, c = seat
    result = 0

    r_max, c_max = len(map), len(map[0])

    for r_move in (1, 0, -1):
        for c_move in (1, 0, -1):
            if r_move == c_move == 0:
                continue
            r_neigh = r + r_move
            c_neigh = c + c_move
            if r_neigh < 0 or c_neigh < 0 or r_neigh >= r_max or c_neigh >= c_max:
                continue

            result += 1 if map[r_neigh][c_neigh] == "#" else 0

    return result


def draw(map):
    print("X" * 80)
    for r in map:
        print("".join(r))
    print("X" * 80)


# draw(map)

next_round = deepcopy(map)


while True:
    total_occupied = 0
    for ri, row in enumerate(map):
        for ci, cell in enumerate(row):
            occupied = occupied_around(map, (ri, ci))
            if cell == "L" and occupied == 0:
                next_round[ri][ci] = "#"
            elif cell == "#" and occupied >= 4:
                next_round[ri][ci] = "L"
            
            if cell == "#":
                total_occupied += 1

    if map == next_round:
        print(total_occupied)
        break

    map = deepcopy(next_round)

    # draw(map)
