from collections import deque

def generate_neighboors(x, y):
    """Generates all possible neighbors within the map"""
    combinations = ((x, y-1), (x, y+1), (x-1, y), (x+1, y))
    for nx, ny in combinations:
        if nx < 0 or ny < 0 or nx >= len(cave)*5 or ny >= len(cave[0])*5:
            continue
        yield (nx, ny)

def value(x, y):
    x_tile, x = divmod(x, len(cave))
    y_tile, y = divmod(y, len(cave[0]))

    distance = x_tile + y_tile
    original_value = int(cave[x][y])
    value = original_value + distance

    return value if value <= 9 else value % 9

with open("input.txt") as input_file:
    cave = input_file.read().splitlines()

queue = deque()
queue.append((0, 0))
risk = {(0, 0): 0}
end = ((len(cave)*5)-1, (len(cave[0])*5)-1)

while len(queue) > 0:
    x, y = queue.popleft()

    for nx, ny in generate_neighboors(x, y):
        neigh_risk = risk[(x, y)] + value(nx, ny)
        if (nx, ny) not in risk or neigh_risk < risk[(nx, ny)]:
            risk[(nx, ny)] = neigh_risk
            queue.append((nx, ny))

print(risk[end])
