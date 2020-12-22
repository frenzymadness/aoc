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

while p0 and p1:
    c1, c2 = p0.popleft(), p1.popleft()
    if c1 > c2:
        p0.extend((c1, c2))
    else:
        p1.extend((c2, c1))

result = 0
for i, c in enumerate(chain(reversed(p0), reversed(p1)), start=1):
    result += i * c

print(result)
