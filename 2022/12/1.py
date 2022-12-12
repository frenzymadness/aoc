from pathlib import Path
from string import ascii_lowercase
from collections import deque

here = Path(__file__).parent

with open(here / "input") as file:
    lines = file.readlines()

plan = []
max_r = len(lines) - 1
max_c = len(lines[0].strip()) - 1
dist = {}

for r, line in enumerate(lines):
    plan.append([])
    line = line.strip()
    for c, cell in enumerate(line):
        plan[-1].append(cell)
        if cell == "S":
            start_pos = (r, c)
            dist[start_pos] = 0
        elif cell == "E":
            end_pos = (r, c)

queue = deque([(0, start_pos)])

def value(char):
    if char == "S":
        return 0
    elif char == "E":
        return 25
    return ascii_lowercase.index(char)

while queue:
    steps, pos = queue.popleft()
    r, c = pos
    possible = []
    if r < max_r:
        possible.append((r+1, c))
    if r > 0:
        possible.append((r-1, c))
    if c < max_c:
        possible.append((r, c+1))
    if c > 0:
        possible.append((r, c-1))
    
    for dest in possible:
        dr, dc = dest
        if value(plan[dr][dc]) - value(plan[r][c]) <= 1 and (dr, dc) not in dist:
            dist[(dr, dc)] = steps + 1
            queue.append((steps+1, dest))
    
print(dist[end_pos])
