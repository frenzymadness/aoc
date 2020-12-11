from copy import deepcopy

with open("input.txt") as input_file:
    map = [list(l.strip()) for l in input_file.readlines()]


def occupied_visible(map, seat):
    r, c = seat
    result = 0

    r_max, c_max = len(map), len(map[0])

    for r_move in (1, 0, -1):
        for c_move in (1, 0, -1):
            if r_move == c_move == 0:
                continue
            multiplier = 0
            while True:
                multiplier += 1
                r_neigh = r + r_move * multiplier
                c_neigh = c + c_move * multiplier
                
                if r_neigh < 0 or c_neigh < 0 or r_neigh >= r_max or c_neigh >= c_max:
                    break

                if map[r_neigh][c_neigh] == ".":
                    continue
                
                if map[r_neigh][c_neigh] == "L":
                    break
            
                if map[r_neigh][c_neigh] == "#":
                    result += 1
                    break

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
            occupied = occupied_visible(map, (ri, ci))
            if cell == "L" and occupied == 0:
                next_round[ri][ci] = "#"
            elif cell == "#" and occupied >= 5:
                next_round[ri][ci] = "L"
            
            if cell == "#":
                total_occupied += 1

    if map == next_round:
        print(total_occupied)
        break

    map = deepcopy(next_round)

    # draw(map)
