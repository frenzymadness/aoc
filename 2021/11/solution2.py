from collections import deque

def generate_neighboors(x, y):
    """Generates all possible neighbors within the map"""
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            if (nx == x and ny == y) or nx < 0 or ny < 0 or nx >= len(octo) or ny >= len(octo[0]):
                continue
            yield (nx, ny)

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

octo = [[int(n) for n in line] for line in lines]

for round in range(1000):
    flashed = []
    to_flash = deque()
    for x in range(len(octo)):
        for y in range(len(octo[0])):
            octo[x][y] += 1
            if octo[x][y] > 9:
                to_flash.append((x, y))

    while len(to_flash) > 0:
        x, y = to_flash.popleft()
        flashed.append((x, y))
        for nx, ny in generate_neighboors(x, y):
            octo[nx][ny] += 1
            if octo[nx][ny] > 9 and (nx, ny) not in flashed and (nx, ny) not in to_flash:
                to_flash.append((nx, ny))

    if len(flashed) == len(octo) * len(octo[0]):
        print(round + 1)
        break
    
    for x, y in flashed:
        octo[x][y] = 0
