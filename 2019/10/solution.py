from decimal import Decimal, DecimalException

def lin_equ(p1, p2):
    """Line encoded as l=(x,y)."""
    try:
        m = Decimal((p2[1] - p1[1])) / Decimal(p2[0] - p1[0])
    except DecimalException:
        return None, None
    c = (p2[1] - (m * p2[0]))
    return m, c

with open("input.txt") as input_file:
    lines = input_file.readlines()
lines = [line.strip() for line in lines]

width = len(lines[0])
height = len(lines)

asteroids = []
for y in range(height):
    for x in range(width):
        if lines[y][x] == "#":
            asteroids.append((x, y))

print(asteroids)

see = {}

for asteroid in asteroids:
    rest = list(asteroids)
    rest.remove(asteroid)
    see[asteroid] = set()
    for second_asteroid in rest:
        # print(asteroid, second_asteroid)
        m, c = lin_equ(asteroid, second_asteroid)
        # print(f"ast1 {asteroid} and ast2 {second_asteroid} have {m} {c}")
        to_check = list(rest)
        to_check.remove(second_asteroid)
        for blocker in to_check:
            if blocker[0] not in range(min(asteroid[0], second_asteroid[0]), max(asteroid[0], second_asteroid[0])+1) or blocker[1] not in range(min(asteroid[1], second_asteroid[1]), max(asteroid[1], second_asteroid[1])+1):
                continue
            if m is not None:
                if blocker[1] == m*blocker[0] + c:
                    print(f"{blocker} BLOCKS {asteroid} and {second_asteroid}, eq: {m}, {c}")
                    break
                else:
                    print(f"{blocker} is not between {asteroid} and {second_asteroid}, eq: {m}, {c}")
            else:
                if  asteroid[0] == blocker[0] == second_asteroid[0] and (asteroid[1] < blocker[1] < second_asteroid[1] or asteroid[1] > blocker[1] > second_asteroid[1]):
                    print(f"{blocker} BLOCKS {asteroid} and {second_asteroid}")
                    break
                else:
                    print(f"{blocker} is not between {asteroid} and {second_asteroid}")
        else:
            print(f"Blocker not found: {asteroid} sees {second_asteroid}")
            see[asteroid].add(second_asteroid)

maximum = 0
ast = None
for k, v in see.items():
    print(f"asteroid {k} sees {len(v)} other asteroids")
    if len(v) > maximum:
        maximum = len(v)
        ast = k

print(maximum, k)
