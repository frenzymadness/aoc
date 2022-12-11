from pathlib import Path

here = Path(__file__).parent


def move_head(direction, position):
    if direction == "R":
        return position[0]+1, position[1]
    elif direction == "L":
        return position[0]-1, position[1]
    elif direction == "U":
        return position[0], position[1]+1
    else:
        return position[0], position[1]-1


def move_knot(knot1, knot2):
    dist_x, dist_y = distances(knot1, knot2)
    knot2_x, knot2_y = knot2
    if dist_x > 0:
        knot2_x += 1
    elif dist_x < 0:
        knot2_x -= 1
    if dist_y > 0:
        knot2_y += 1
    elif dist_y < 0:
        knot2_y -= 1
    
    return knot2_x, knot2_y


def should_move_knot(knot1, knot2):
    dist_x, dist_y = distances(knot1, knot2)
    dist_x, dist_y = abs(dist_x), abs(dist_y)
    return dist_x >= 2 or dist_y >= 2 or dist_x + dist_y > 2


def distances(knot1, knot2):
    dist_x = knot1[0] - knot2[0]
    dist_y = knot1[1] - knot2[1]
    return dist_x, dist_y


def display(knots):
    max_x = max([x + 3 for x, y in knots] + [3])
    min_x = min([x - 3 for x, y in knots] + [-3])
    max_y = max([y + 3 for x, y in knots] + [3])
    min_y = min([y - 3 for x, y in knots] + [-3])
    print("X" * 10)
    for y in range(max_y, min_y-1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) in knots:
                print(knots.index((x, y)), end="")
            elif (x, y) == (0, 0):
                print("s", end="")
            else:
                print(".", end="")
        print()


with open(here / "input") as file:
    content = file.read()

knots = [(0, 0)] * 10
tail_history = set()

display(knots)

for line in content.splitlines():
    direction, count = line.split()
    for _ in range(int(count)):
        knots[0] = move_head(direction, knots[0])
        for i in range(1, 10):
            if should_move_knot(knots[i-1], knots[i]):
                knots[i] = move_knot(knots[i-1], knots[i])
        tail_history.add(knots[-1])
        #display(knots)

print(len(tail_history))
