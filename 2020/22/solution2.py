from collections import deque
from itertools import chain

p0 = deque()
p1 = deque()

with open("input.txt") as input_file:
    fill = p0
    for line in input_file:
        if line.startswith("Player"):
            continue
        if line.strip() == "":
            fill = p1
            continue
        fill.append(int(line.strip()))

def play(p0, p1):
    history = []
    while p0 and p1:
        game_str = ",".join(map(str, p0)) + "-" + ",".join(map(str, p1))
        if game_str in history:
            return 0
        else:
            history.append(game_str)

        c1, c2 = p0.popleft(), p1.popleft()
        if c1 <= len(p0) and c2 <= len(p1):
            winner = play(deque(list(p0)[:c1]), deque(list(p1)[:c2]))
            if winner == 0:
                p0.extend((c1, c2))
            else:
                p1.extend((c2, c1))
        elif c1 > c2:
            p0.extend((c1, c2))
        else:
            p1.extend((c2, c1))

    return 0 if len(p0) > 0 else 1

play(p0, p1)

result = 0
for i, c in enumerate(chain(reversed(p0), reversed(p1)), start=1):
    result += i * c

print(result)
