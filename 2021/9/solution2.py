import math


def generate_neighboors(x, y):
    """Generates all possible neighbors within the map"""
    neigh = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]        
    result = []
    for nx, ny in neigh:
        if nx < 0 or ny < 0 or nx >= len(map) or ny >= len(map[0]):
            continue
        result.append((nx, ny))

    return result


def get_area(x, y):
    """Recursively search throught neigbors and count total area"""
    if map[x][y] == "9" or (x, y) in visited_points:
        return 0
    visited_points.append((x, y))
    sum = 1
    for nx, ny in generate_neighboors(x, y):
        sum += get_area(nx, ny)
    return sum


with open("input.txt") as input_file:
    map = input_file.read().splitlines()


low_points = []
visited_points = []

for x in range(len(map)):
    for y in range(len(map[0])):
        for nx, ny in generate_neighboors(x, y):
            if map[nx][ny] <= map[x][y]:
                break
        else:
            low_points.append((x, y))

basins = []
for x, y in low_points:
    basins.append(get_area(x, y))

highest = sorted(basins, reverse=True)[:3]

print(math.prod(highest))
