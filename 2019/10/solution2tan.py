from decimal import Decimal, DecimalException
from itertools import cycle
from math import atan, sqrt, degrees, tan, radians

def lin_equ(p1, p2):
    """Line encoded as l=(x,y)."""
    try:
        m = Decimal((p2[1] - p1[1])) / Decimal(p2[0] - p1[0])
    except DecimalException:
        return None, None
    c = (p2[1] - (m * p2[0]))
    return m, c

def distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

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
station = (11, 13)
if station in asteroids:
    asteroids.remove(station)
asteroids_count = len(asteroids)
complete = []

for asteroid in asteroids:
    eq = lin_equ(station, asteroid)
    if eq[0] == None:
        if asteroid[1] < station[1]:
            deg = 0
        else:
            deg = 180
    else:
        deg = degrees(atan(eq[0])) +90

    if asteroid[0] < station[0]:
        deg += 180

    dist = distance(station, asteroid)
    complete.append((asteroid, eq, deg, dist))

by_deg = {}

for c in complete:
    print(c)
    ast, *_, deg, dist = c
    if deg in by_deg:
        by_deg[deg].append((ast, dist))
    else:
        by_deg[deg] = [(ast, dist)]

removed = []

while True:
    for k, v in sorted(by_deg.items(), key=lambda x: x[0]):
        print(k, v)
        for ast, dist in sorted(v, key=lambda x: x[1]):
            print(ast, dist)
            by_deg[k].remove((ast, dist))
            removed.append(ast)
            break
    if len(removed) == asteroids_count:
        break
    print(len(removed), asteroids_count)

import pdb; pdb.set_trace()

print(removed[199])
