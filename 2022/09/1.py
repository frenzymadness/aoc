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


def move_tail(head, tail):
    dist_x, dist_y = distances(head, tail)
    tail_x, tail_y = tail
    if dist_x > 0:
        tail_x += 1
    elif dist_x < 0:
        tail_x -= 1
    if dist_y > 0:
        tail_y += 1
    elif dist_y < 0:
        tail_y -= 1
    
    return tail_x, tail_y


def should_move_tail(head, tail):
    dist_x, dist_y = distances(head, tail)
    dist_x, dist_y = abs(dist_x), abs(dist_y)
    return dist_x >= 2 or dist_y >= 2 or dist_x + dist_y > 2


def distances(head, tail):
    dist_x = head[0] - tail[0]
    dist_y = head[1] - tail[1]
    return dist_x, dist_y


def display(head, tail):
    max_x = max(head[0]+3, tail[0]+3, 3)
    min_x = min(head[0]-3, tail[0]-3, -3)
    max_y = max(head[1]+3, tail[1]+3, 3)
    min_y = min(head[1]-3, tail[1]-3, -3)
    print("X" * 10)
    for y in range(max_y, min_y-1, -1):
        for x in range(min_x, max_x + 1):
            if (x, y) == head:
                print("H", end="")
            elif (x, y) == tail:
                print("T", end="")
            elif (x, y) == (0, 0):
                print("s", end="")
            else:
                print(".", end="")
        print()


with open(here / "input") as file:
    content = file.read()

head = 0, 0
tail = 0, 0
tail_history = set()

display(head, tail)

for line in content.splitlines():
    direction, count = line.split()
    for _ in range(int(count)):
        head = move_head(direction, head)
        if should_move_tail(head, tail):
            tail = move_tail(head, tail)
        tail_history.add(tail)
        # display(head, tail)

print(len(tail_history))
