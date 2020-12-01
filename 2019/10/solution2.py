from decimal import Decimal, DecimalException
from itertools import cycle
import math

def lin_equ(p1, p2):
    """Line encoded as l=(x,y)."""
    try:
        m = Decimal((p2[1] - p1[1])) / Decimal(p2[0] - p1[0])
    except DecimalException:
        return None, None
    c = (p2[1] - (m * p2[0]))
    return m, c

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

with open("test6.txt") as input_file:
    lines = input_file.readlines()
lines = [line.strip() for line in lines]

width = len(lines[0])
height = len(lines)

asteroids = []
for y in range(height):
    for x in range(width):
        if lines[y][x] == "#":
            asteroids.append((x, y))

# print(asteroids)
station = (8, 3)

# assert station in asteroids
# asteroids.remove(station)

p1 = [(x, 0) for x in range(station[0], width)]
p2 = [(width, y) for y in range(0, height)]
p3 = [(x, height) for x in range(width, 0, -1)]
p4 = [(0, y) for y in range(height, 0, -1)]
p5 = [(x, 0) for x in range(0, station[0])]

margins = [*p1, *p2, *p3, *p4, *p5]
equations = [lin_equ(station, point) for point in margins]

# print(margins)

for point, eq in zip(margins, equations):
    print(point, eq)
    to_remove = []
    if len(asteroids) == 0:
        break
    for asteroid in asteroids:
        if asteroid[0] not in range(min(station[0], point[0]), max(station[0], point[0])+1) or asteroid[1] not in range(min(station[1], point[1]), max(station[1], point[1])+1):
            continue
        if eq[0] is not None:
            if asteroid[1] == eq[0]*asteroid[0] + eq[1]:
                to_remove.append(asteroid)
                continue
        else:
            if  station[0] == asteroid[0] == point[0] and (station[1] < asteroid[1] < point[1] or station[1] > asteroid[1] > point[1]):
                to_remove.append(asteroid)
                continue
    if to_remove:
        to_remove.sort(key=lambda x: distance(station, x))
        print(f"to remove {to_remove}")
        asteroids.remove(to_remove[0])
