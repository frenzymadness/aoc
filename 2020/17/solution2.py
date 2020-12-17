from copy import deepcopy

with open("input.txt") as input_file:
    map = [[[list(l.strip()) for l in input_file.readlines()]]]


def active_around(map, cube):
    w, z, y, x = cube
    result = 0

    w_max, z_max, y_max, x_max = len(map), len(map[0]), len(map[0][0]), len(map[0][0][0])

    for w_move in (1, 0, -1):    
        for z_move in (1, 0, -1):
            for y_move in (1, 0, -1):
                for x_move in (1, 0, -1):
                    if y_move == x_move == z_move == w_move == 0:
                        continue
                    y_neigh = y + y_move
                    x_neigh = x + x_move
                    z_neigh = z + z_move
                    w_neigh = w + w_move
                    if w_neigh < 0 or z_neigh < 0 or y_neigh < 0 or x_neigh < 0 or w_neigh >= w_max or z_neigh >= z_max or y_neigh >= y_max or x_neigh >= x_max:
                        continue
                    result += 1 if map[w_neigh][z_neigh][y_neigh][x_neigh] == "#" else 0

    return result


def draw(map):
    print("X" * 80)
    for wi, w in enumerate(map):
        print(f"Space {wi}")
        for i, z in enumerate(w):
            print(f"Dimenzion {i}")
            for y in z:
                print("".join(y))
    print("X" * 80)


def extend_map(map):
    new_map  = deepcopy(map)
    for wi, w in enumerate(map):
        for zi, z in enumerate(w):
            new_map[wi][zi].insert(0, ["." for _ in range(len(new_map[wi][zi][0]))])
            new_map[wi][zi].append(["." for _ in range(len(new_map[wi][zi][0]))])
            for yi, y in enumerate(new_map[wi][zi]):
                new_map[wi][zi][yi].insert(0, ".")
                new_map[wi][zi][yi].append(".")
        
        maximum = len(new_map[0][0][0])

        new_map[wi].append([list(["." for _ in range(maximum)]) for __ in range(maximum)])
        new_map[wi].insert(0, [list(["." for _ in range(maximum)]) for __ in range(maximum)])

    new_map.append([[list(["." for _ in range(maximum)]) for __ in range(maximum)] for ___ in range(len(new_map[0]))])
    new_map.insert(0, [ [list(["." for _ in range(maximum)]) for __ in range(maximum)] for ___ in range(len(new_map[0]))])

    return new_map

map = extend_map(map)
next_round = deepcopy(map)

# draw(map)

for _ in range(6):
    total_occupied = 0
    for wi, w in enumerate(map):
        for zi, z in enumerate(map[wi]):
            for yi, y in enumerate(z):
                for xi, cell in enumerate(y):
                    occupied = active_around(map, (wi, zi, yi, xi))
                    if cell == "#" and occupied in (2, 3):
                        pass
                    else:
                        next_round[wi][zi][yi][xi] = "."

                    if cell == "." and occupied == 3:
                        next_round[wi][zi][yi][xi] = "#"
                    
                    if next_round[wi][zi][yi][xi] == "#":
                        total_occupied += 1

    # draw(next_round)

    map = extend_map(next_round)
    next_round = deepcopy(map)

    print(f"round {_}")

    # draw(map)

print(total_occupied)
