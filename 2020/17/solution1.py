from copy import deepcopy

with open("input.txt") as input_file:
    map = [[list(l.strip()) for l in input_file.readlines()]]


def active_around(map, cube):
    z, y, x = cube
    result = 0

    z_max, y_max, x_max = len(map), len(map[0]), len(map[0][0])

    for z_move in (1, 0, -1):
        for y_move in (1, 0, -1):
            for x_move in (1, 0, -1):
                if y_move == x_move == z_move == 0:
                    continue
                y_neigh = y + y_move
                x_neigh = x + x_move
                z_neigh = z + z_move
                if z_neigh < 0 or y_neigh < 0 or x_neigh < 0 or z_neigh >= z_max or y_neigh >= y_max or x_neigh >= x_max:
                    continue

                result += 1 if map[z_neigh][y_neigh][x_neigh] == "#" else 0

    return result


def draw(map):
    print("X" * 80)
    for i, z in enumerate(map):
        print(f"Dimenzion {i}")
        for y in z:
            print("".join(y))
    print("X" * 80)


def extend_map(map):
    new_map  = deepcopy(map)
    for zi, z in enumerate(map):
        new_map[zi].insert(0, ["." for _ in range(len(new_map[zi][0]))])
        new_map[zi].append(["." for _ in range(len(new_map[zi][0]))])
        for yi, y in enumerate(new_map[zi]):
            new_map[zi][yi].insert(0, ".")
            new_map[zi][yi].append(".")
    
    maximum = len(new_map[0][0])

    new_map.append([list(["." for _ in range(maximum)]) for __ in range(maximum)])
    new_map.insert(0, [list(["." for _ in range(maximum)]) for __ in range(maximum)])

    return new_map

map = extend_map(map)
next_round = deepcopy(map)

# draw(map)

for _ in range(6):
    total_occupied = 0
    for zi, z in enumerate(map):
        for yi, y in enumerate(z):
            for xi, cell in enumerate(y):
                occupied = active_around(map, (zi, yi, xi))
                if cell == "#" and occupied in (2, 3):
                    pass
                else:
                    next_round[zi][yi][xi] = "."

                if cell == "." and occupied == 3:
                    next_round[zi][yi][xi] = "#"
                
                if next_round[zi][yi][xi] == "#":
                    total_occupied += 1

    map = extend_map(next_round)
    next_round = deepcopy(map)

    # draw(map)

print(total_occupied)
